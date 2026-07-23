# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Semantic-Swingers Task A (flagship) learner (LLMs4OL 2026): joint text2onto + taxonomy-discovery.

ONE learner class, TWO hooks, dispatched via ``AutoLearner.fit``/``predict``'s ``task`` string:

* ``_text2onto`` — the team's competition champion: retrieval-augmented generation (RAG, top-k
  document exemplars) with a LoRA fine-tuned ``Qwen/Qwen3.5-9B`` (RA-FT), extracting
  ``[subject, relation, object]`` triples per document and projecting them onto OntoLearner's
  native ``{"terms": [...], "types": [...]}`` shape. This is a document-driven generative method
  (needs source text), unlike Task B/C's classification-style selectors.
* ``_taxonomy_discovery`` — reuses :class:`~ontolearner.learner.taxonomy_discovery.semanticswingers.
  SemanticSwingersTaxonomyLearner` **by composition** (delegation, not a rewrite). The native
  OntoLearner taxonomy-discovery harness hands the learner a bare type *vocabulary* with no source
  text (see ``AutoLearner.tasks_data_former``'s default reshaping for that task), so the RAG+FT
  generator — which needs document text to extract triples from — cannot serve that invocation
  path; the team's proven embedding-retrieval taxonomy inducer is the right tool there instead.
  Expect the native taxonomy-discovery F1 reported by this hook to differ from the team's joint
  ``graph_similarity`` score (val_20 RA-FT k10 = 0.6688) — that figure scores a *different*,
  combined metric (term/type/edge overlap together) on the team's own document corpus, not
  OntoLearner's standalone taxonomy metric on a vocabulary-only benchmark ontology. A gap here is
  an expected apples-to-oranges artifact, not a regression.

Model portability background (``docs/ontolearner-native-integration-poc.md`` in the team's main
repo, section "Model portability"): ``Qwen/Qwen3.5-9B`` uses the ``qwen3_5``/``qwen3_next`` hybrid
(dense + linear-attention) architecture, which no *released* ``transformers`` version registers as
of 2026-07-09 — only ``transformers`` installed from git source does. Loading the base model plus
the team's PEFT LoRA adapter **unmerged** (never a manually fused/merged checkpoint — that route
was tried and abandoned after producing incoherent output despite a byte-identical state dict) is
the exact recipe already used to produce every graded Task A result the team has, and is the one
implemented here.
"""
from __future__ import annotations

import ast
import json
import os
import re
from typing import Any, Dict, List, Optional, Tuple

from ...base import AutoLearner, AutoRetriever
from ..taxonomy_discovery.semanticswingers import SemanticSwingersTaxonomyLearner

#: Exact transformers commit verified (2026-07-09) to (a) register `qwen3_5`/`qwen3_next` in
#: `CONFIG_MAPPING` and (b) load base `Qwen/Qwen3.5-9B` + the team's PEFT adapter producing
#: coherent, on-topic triple extraction on a real held-out document (not just a token count).
#: Never float `@main` — the qwen3_5 modeling code is young enough that semantics have already
#: drifted once between dev snapshots (see the POC doc's fused-checkpoint post-mortem).
_VERIFIED_TRANSFORMERS_COMMIT = "1f2fd05824a7ef71a767a122ebd7526ca4e55e40"
_PIP_INSTALL_LINE = (
    f'pip install "transformers @ git+https://github.com/huggingface/transformers.git'
    f'@{_VERIFIED_TRANSFORMERS_COMMIT}" "peft>=0.19" "accelerate>=1.0"'
)

_SYSTEM_PROMPT = (
    "You are an expert ontology engineer. Extract a primitive ontology from the document as "
    "triples [subject, relation, object].\n"
    "RULES:\n"
    "1. Extract Terms (instances) and Types (classes).\n"
    "2. Dominant relations: 'is-a' (subclassing), 'instance-of' or 'type' (term typing), "
    "'equivalent class' (synonyms), 'disjoint with', 'part_of'/'has part'. Use these exact "
    "labels; reuse consistent labels.\n"
    "3. WARNING: Most texts only contain taxonomic definitions. Do NOT extract semantic "
    "relationships unless explicitly demanded by strict logical constraints. If there are no "
    "relations other than 'is-a', do not invent them.\n"
    "4. Direction matters: emit Child -> is-a -> Parent.\n"
    'Output ONLY JSON {"triples": [[subject, relation, object], ...]}; entities grounded in '
    "the text."
)
_NOTHINK_SUFFIX = "<|im_start|>assistant\n<think>\n\n</think>\n\n"
_TYPING_RELATIONS = {"is-a", "instance-of", "type"}

# HuggingFace repo ids for the two published PEFT adapters (private until competition submission
# 2026-07-26; override via the `adapter` constructor arg with a local path in the meantime, e.g.
# the team's `data/ft/_runners/raft_adapter/final`).
_ADAPTER_REPOS = {
    "raft": "datagero/qwen3.5-9b-raft-taska",
    "baseft": "datagero/qwen3.5-9b-baseft-taska",
}


def _require_qwen35_transformers() -> None:
    """Fail loudly and actionably if the installed transformers doesn't know qwen3_5.

    Lazy import guard (RWTH/g4f optional-dep precedent): the git-source transformers requirement
    is NOT added to OntoLearner's core ``pyproject.toml`` — it is heavy (build-from-source), a
    moving target, and only this one learner needs it. Callers see a clear, copy-pasteable fix.
    """
    try:
        from transformers.models.auto.configuration_auto import CONFIG_MAPPING
    except ImportError as e:  # pragma: no cover - transformers itself missing
        raise ImportError(
            "SemanticSwingersText2OntoLearner requires transformers with qwen3_5/qwen3_next "
            f"support, but transformers is not importable at all. Install it with:\n"
            f"  {_PIP_INSTALL_LINE}"
        ) from e
    if "qwen3_5" not in CONFIG_MAPPING:
        raise ImportError(
            "SemanticSwingersText2OntoLearner requires a transformers build that registers the "
            "'qwen3_5' architecture (Qwen/Qwen3.5-9B's model type). No released transformers "
            "version ships this yet (verified 2026-07-09) — install from git source, pinned to "
            "the commit this learner was validated against:\n"
            f"  {_PIP_INSTALL_LINE}\n"
            "(see docs/ontolearner-native-integration-poc.md in the team's main repo for the "
            "full portability investigation)."
        )


def _parse_triples_json(text: str) -> List[Any]:
    """Robust JSON/markdown-fence extraction of a ``{"triples": [...]}`` payload.

    Ported (self-contained, no cross-repo import) from the team's ``src/experiments/
    triple_utils.py::_parse`` — kept intentionally small so the fork carries no dependency on the
    private llms4ol-2026 competition repo.
    """
    if not isinstance(text, str) or not text:
        return []
    m = re.search(r"`{3}(?:json)?\s*([\s\S]*?)\s*`{3}", text, re.IGNORECASE)
    body = m.group(1).strip() if m else text
    if not m:
        a, b = body.find("["), body.rfind("]")
        if a != -1 and b != -1:
            body = body[a : b + 1]
    for loader in (json.loads, ast.literal_eval):
        try:
            d = loader(body)
            if isinstance(d, dict):
                d = d.get("triples", [])
            if isinstance(d, list):
                return d
        except Exception:
            continue
    return []


def _to_triples(items: List[Any]) -> List[Tuple[str, str, str]]:
    """Coerce parsed triple items (list-of-3 or dict shapes) into clean ``(s, r, o)`` tuples."""
    out: List[Tuple[str, str, str]] = []
    for t in items or []:
        if isinstance(t, dict):
            s = t.get("subject", t.get("head", t.get("source", "")))
            r = t.get("relation", t.get("predicate", t.get("type", "")))
            o = t.get("object", t.get("tail", t.get("target", "")))
        elif isinstance(t, (list, tuple)) and len(t) == 3:
            s, r, o = t
        else:
            continue
        s, r, o = str(s).strip(), str(r).strip().lower(), str(o).strip()
        if s and r and o:
            out.append((s, r, o))
    return out


def _reasoning_off(model: Optional[str]) -> Dict[str, Any]:
    """Disable a thinking model's hidden reasoning pass (qwen3.x over an OpenAI-compatible API).

    Left on, qwen3.x spends the whole ``max_tokens`` budget reasoning and returns empty content,
    so nothing parses. No-op for other models. Mirrors the Task B/C learners.
    """
    if str(model or "").startswith("qwen3"):
        return {"extra_body": {"reasoning_effort": "none"}}
    return {}


class SemanticSwingersText2OntoLearner(AutoLearner):
    """RAG + LoRA-fine-tuned Qwen3.5-9B triple extractor, serving text2onto and taxonomy-discovery.

    Args:
        adapter: ``"raft"`` (retrieval-aware fine-tune, the competition champion — trained with
            exemplars baked into the prompt, wants ``top_k > 0`` at inference) or ``"baseft"``
            (standard fine-tune, trained without exemplars — best used retrieval-free,
            ``top_k=0``). Either may also be a local filesystem path or a HuggingFace repo id to
            a PEFT adapter directory, overriding the published default for that name.
        base_model_id: HuggingFace id of the frozen base model the adapter was trained on.
        top_k: Number of retrieved training-document exemplars baked into the generation prompt
            (RA-FT's regime; ``0`` degrades to zero-shot, base-FT's regime).
        retriever_model_id: SentenceTransformer id used to embed documents for exemplar retrieval.
        max_new_tokens: Generation budget per document.
        device: Torch device string (``"cpu"``, ``"cuda"``, ``"mps"``, ...). CPU works but is
            slow without the ``fla``/``causal-conv1d`` fast kernels (GPU-only); see the class
            docstring's model-portability note.
        taxonomy_kwargs: Extra keyword arguments forwarded to the composed
            :class:`SemanticSwingersTaxonomyLearner` used for the ``_taxonomy_discovery`` hook.
    """

    _OLLAMA_BASE_URL = "http://localhost:11434/v1"
    _DEFAULT_LLM = {"openai": "gpt-4.1-mini", "ollama": "qwen3.5-nothink:9b"}

    def __init__(
        self,
        adapter: str = "raft",
        base_model_id: str = "Qwen/Qwen3.5-9B",
        backend: str = "peft",
        llm_model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        top_k: int = 10,
        retriever_model_id: str = "sentence-transformers/all-MiniLM-L6-v2",
        max_new_tokens: int = 1500,
        device: str = "cpu",
        taxonomy_kwargs: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialise the learner and record configuration (no I/O, no model load yet)."""
        super().__init__()
        self.adapter = _ADAPTER_REPOS.get(adapter, adapter)
        self.base_model_id = base_model_id
        self.backend = backend
        self.llm_model = llm_model or self._DEFAULT_LLM.get(backend)
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if base_url is None and backend == "ollama":
            base_url = self._OLLAMA_BASE_URL
        self.base_url = base_url
        self.top_k = top_k
        self.retriever_model_id = retriever_model_id
        self.max_new_tokens = max_new_tokens
        self.device = device

        self._model: Optional[Any] = None
        self._tokenizer: Optional[Any] = None
        self._retriever = AutoRetriever()
        self._train_docs: List[Dict[str, Any]] = []  # {"doc_id", "text", "triples"}

        # Composition, not rewrite: the native taxonomy-discovery invocation gives us a bare
        # type vocabulary (no document text), so it gets the team's proven embedding-retrieval
        # inducer verbatim rather than a second copy of the generative pipeline.
        self._taxonomy_learner = SemanticSwingersTaxonomyLearner(**(taxonomy_kwargs or {}))

    def tasks_data_former(self, data: Any, task: str, test: bool = False) -> Any:
        """Pass the raw data through unchanged for both hooks (run with ``ontologizer_data=False``).

        ``_text2onto`` expects ``{"documents": [...], "terms2docs": {...}, "terms2types": {...}}``
        (mirrors the ``alexbek`` text2onto learner's contract); ``_taxonomy_discovery`` expects
        the native ``OntologyData`` object the composed :class:`SemanticSwingersTaxonomyLearner`
        already knows how to read.
        """
        return data

    def load(self, model_id: Optional[str] = None, **kwargs: Any) -> None:
        """Load the base model + PEFT adapter (lazily; only once).

        Called by ``LearnerPipeline`` as ``load(model_id=llm_id)``; a ``model_id`` containing
        ``"/"`` overrides ``base_model_id``, a plain bookkeeping label is ignored (mirrors the
        team's Task B/C learners).
        """
        if self._model is not None:
            return
        if model_id and "/" in model_id and model_id != self.adapter:
            self.base_model_id = model_id

        if self.backend in ("ollama", "openai"):
            # API-served backends need no local weights: the generator is remote.
            self._model = self          # sentinel so `_generate_triples` sees an initialised learner
            self._taxonomy_learner.load(model_id=self.retriever_model_id)
            return

        _require_qwen35_transformers()
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        from peft import PeftModel

        self._tokenizer = AutoTokenizer.from_pretrained(self.base_model_id, trust_remote_code=True)
        base = AutoModelForCausalLM.from_pretrained(
            self.base_model_id,
            dtype=torch.bfloat16,
            trust_remote_code=True,
            low_cpu_mem_usage=True,
        )
        self._model = PeftModel.from_pretrained(base, self.adapter)
        self._model.eval()

        self._taxonomy_learner.load(model_id=self.retriever_model_id)

    # -- shared generation --------------------------------------------------------------------

    def _exemplar_block(self, ex: Dict[str, Any], max_ctx: int = 1000, max_triples: int = 20) -> str:
        """One retrieved training exemplar rendered as a user/assistant turn pair."""
        trips = [list(t) for t in ex["triples"][:max_triples]]
        payload = json.dumps({"triples": trips}, ensure_ascii=False)
        return (
            f"<|im_start|>user\nDocument:\n{ex['text'][:max_ctx]}\n\n"
            f"Extract the ontology triples as JSON.<|im_end|>\n"
            f"<|im_start|>assistant\n{payload}<|im_end|>\n"
        )

    def _build_prompt(self, text: str, exemplars: List[Dict[str, Any]]) -> str:
        ctx = text[:4000]
        ex_block = "".join(self._exemplar_block(e) for e in exemplars)
        user = f"<|im_start|>user\nDocument:\n{ctx}\n\nExtract the ontology triples as JSON.<|im_end|>\n"
        return (
            f"<|im_start|>system\n{_SYSTEM_PROMPT}<|im_end|>\n" + ex_block + user + _NOTHINK_SUFFIX
        )

    @staticmethod
    def _strip_think(text: str) -> str:
        if "</think>" in text:
            text = text.split("</think>", 1)[1]
        return text.strip()

    def _chat_messages(self, text: str, exemplars: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """Same prompt content as ``_build_prompt``, in OpenAI chat-message form.

        The PEFT path renders exemplars into a single ChatML string; API backends want
        structured turns. Content is identical so the two backends stay comparable.
        """
        msgs: List[Dict[str, str]] = [{"role": "system", "content": _SYSTEM_PROMPT}]
        for ex in exemplars:
            payload = json.dumps({"triples": [list(t) for t in ex["triples"][:20]]},
                                 ensure_ascii=False)
            msgs.append({"role": "user",
                         "content": f"Document:\n{ex['text'][:1000]}\n\n"
                                    "Extract the ontology triples as JSON."})
            msgs.append({"role": "assistant", "content": payload})
        msgs.append({"role": "user",
                     "content": f"Document:\n{text[:4000]}\n\n"
                                "Extract the ontology triples as JSON."})
        return msgs

    def _generate_api(self, text: str, exemplars: List[Dict[str, Any]]) -> List[Tuple[str, str, str]]:
        """Generate via an OpenAI-compatible endpoint (``ollama`` or ``openai`` backend)."""
        from openai import OpenAI

        key = self.api_key if self.backend == "openai" else (self.api_key or "ollama")
        client = OpenAI(api_key=key, base_url=self.base_url)
        params: Dict[str, Any] = dict(
            model=self.llm_model,
            messages=self._chat_messages(text, exemplars),
            temperature=0,
            max_tokens=self.max_new_tokens,
            **_reasoning_off(self.llm_model),
        )
        try:
            resp = client.chat.completions.create(response_format={"type": "json_object"}, **params)
        except Exception:
            resp = client.chat.completions.create(**params)
        return _to_triples(_parse_triples_json(
            self._strip_think(resp.choices[0].message.content or "")))

    def _generate_triples(self, text: str, exemplars: List[Dict[str, Any]]) -> List[Tuple[str, str, str]]:
        """Run the generator on one document and return parsed ``(s, r, o)`` triples."""
        if self.backend in ("ollama", "openai"):
            return self._generate_api(text, exemplars)

        import torch

        if self._model is None:
            self.load()
        prompt = self._build_prompt(text, exemplars)
        ids = self._tokenizer(prompt, return_tensors="pt").to(self._model.device)
        with torch.no_grad():
            out = self._model.generate(
                **ids,
                max_new_tokens=self.max_new_tokens,
                do_sample=False,
                pad_token_id=self._tokenizer.eos_token_id,
            )
        decoded = self._tokenizer.decode(out[0][ids["input_ids"].shape[1] :], skip_special_tokens=True)
        return _to_triples(_parse_triples_json(self._strip_think(decoded)))

    def _retrieve_exemplars(self, text: str) -> List[Dict[str, Any]]:
        if self.top_k <= 0 or not self._train_docs:
            return []
        hits = self._retriever.retrieve([text], top_k=self.top_k)[0]
        by_text = {d["text"]: d for d in self._train_docs}
        return [by_text[h] for h in hits if h in by_text]

    # -- _text2onto -----------------------------------------------------------------------------

    @staticmethod
    def _doc_id(d: Dict[str, Any]) -> str:
        return str(d.get("doc_id") or d.get("id") or d.get("docid") or "")

    @staticmethod
    def _doc_text(d: Dict[str, Any]) -> str:
        return str(d.get("text") or d.get("context") or "")

    def _text2onto(self, data: Any, test: bool = False) -> Optional[Dict[str, List[Any]]]:
        """Train mode: index document exemplars. Test mode: extract triples -> {terms, types}.

        The returned dict also carries the raw, unprojected ``"triples"`` under an extra key
        (``[[doc_id, subject, relation, object], ...]``). ``text2onto_metrics`` (OntoLearner's
        native scorer, ``evaluation/metrics.py:81-90``) reads only ``"terms"``/``"types"`` and
        silently ignores unknown keys, and the full dict passes through unchanged to
        ``run_report['predictions']`` (``_learner.py:120``) — so this is purely additive: native
        scoring is identical, and the ~90% ``is-a`` signal the ``{terms, types}`` projection
        would otherwise discard survives in the returned predictions for downstream inspection
        (see ADR-0018 addendum §4 in the team's main repo, ``llms4ol-2026``).
        """
        if not isinstance(data, dict):
            raise ValueError(
                "text2onto expects {'documents': [...], 'terms2docs': {...}, 'terms2types': "
                "{...}} (see AlexbekRAGFewShotLearner's contract)."
            )
        docs = data.get("documents") or data.get("docs") or []
        gold_triples = data.get("triples") or {}  # optional: doc_id -> [[s, r, o], ...]

        if not test:
            self._train_docs = []
            for d in docs:
                did = self._doc_id(d)
                text = self._doc_text(d)
                triples = gold_triples.get(did, [])
                self._train_docs.append({"doc_id": did, "text": text, "triples": triples})
            if self._train_docs:
                self._retriever.load(self.retriever_model_id)
                self._retriever.index([d["text"] for d in self._train_docs])
            return None

        if self._model is None:
            self.load()

        pred_terms: List[Dict[str, str]] = []
        pred_types: List[Dict[str, str]] = []
        pred_triples: List[List[str]] = []
        for d in docs:
            did = self._doc_id(d)
            text = self._doc_text(d)
            exemplars = self._retrieve_exemplars(text)
            triples = self._generate_triples(text, exemplars)

            terms_seen: set = set()
            types_seen: set = set()
            for s, r, o in triples:
                pred_triples.append([did, s, r, o])
                if s not in terms_seen:
                    terms_seen.add(s)
                    pred_terms.append({"doc_id": did, "term": s})
                if r in _TYPING_RELATIONS and o not in types_seen:
                    types_seen.add(o)
                    pred_types.append({"doc_id": did, "type": o})

        return {"terms": pred_terms, "types": pred_types, "triples": pred_triples}

    # -- _taxonomy_discovery (composed, not reimplemented) ---------------------------------------

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[List[Dict[str, str]]]:
        """Delegate to the team's proven embedding-retrieval taxonomy inducer (Task C hook)."""
        return self._taxonomy_learner._taxonomy_discovery(data, test=test)
