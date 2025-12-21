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

import json
import re
from typing import Any, Dict, List, Optional
from collections import defaultdict

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from ...base import AutoLearner, AutoRetriever

class AlexbekRAGFewShotLearner(AutoLearner):
    """
    What it does (2-stage):
      1) doc -> terms
         - retrieve top-k similar TRAIN documents (each has gold OL terms)
         - build a few-shot chat prompt: (doc -> {"terms":[...]}) examples + target doc
         - generate JSON {"terms":[...]} and parse it

      2) term -> types
         - retrieve top-k similar TRAIN terms (each has gold types)
         - build a few-shot chat prompt: (term -> {"types":[...]}) examples + target term
         - generate JSON {"types":[...]} and parse it

    Training behavior (fit):
      - builds two retrieval indices:
          * doc_retriever index over JSON strings of train docs (with "OL" field = gold terms)
          * term_retriever index over JSON strings of train term->types examples

    Prediction behavior (predict):
      - returns a dict compatible with OntoLearner evaluation_report:
          {
            "terms": [{"doc_id": "...", "term": "..."}, ...],
            "types": [{"doc_id": "...", "type": "..."}, ...],
          }

    Expected data format for task="text2onto":
      data = {
        "documents": [ {"id"/"doc_id": str, "title": str, "text": str, ...}, ... ],
        "terms2docs": { term(str): [doc_id(str), ...], ... }
        "terms2types": { term(str): [type(str), ...], ... }
      }

    IMPORTANT:
      - LearnerPipeline calls learner.load(model_id=llm_id). We accept that and override llm_model_id.
      - We override tasks_data_former() so AutoLearner.fit/predict does NOT rewrite text2onto dicts.
      - Device placement: we put the model exactly on the device string the user provides
        ("cpu", "cuda", "cuda:0", "cuda:1", ...). No device_map="auto".
    """

    TERM2TYPES_SYSTEM_PROMPT = (
        "You are an expert in ontology and semantic type classification. Your task is to predict "
        "the semantic types for given terms based on their context and similar examples.\n\n"
        "Given a term, you should predict its semantic types from the domain-specific ontology. "
        "Use the provided examples to understand the patterns and relationships between terms and their types.\n\n"
        "Output your response as a JSON object with the following structure:\n"
        '{\n  "types": ["type1", "type2", ...]\n}\n\n'
        "The types should be relevant semantic categories that best describe the given term."
    )

    DOC2TERMS_SYSTEM_PROMPT = (
        "You are an expert in ontology term extraction.\n\n"
        "TASK: Extract specific, relevant ontology terms from scientific documents.\n\n"
        "INSTRUCTIONS:\n"
        "- The following conversation contains few-shot examples showing correct term extraction patterns\n"
        "- Study these examples carefully to understand the extraction style and approach\n"
        "- Follow the EXACT same pattern and style demonstrated in the examples\n"
        "- Extract only terms that actually appear in the document text\n"
        "- Focus on domain-specific terminology, concepts, and technical terms\n\n"
        "- The first three user-assistant conversation pairs serve as few-shot examples\n"
        "- Each example shows: user provides a document, assistant extracts relevant terms\n"
        "- Pay attention to the extraction patterns and term selection criteria in these examples\n\n"
        "DO:\n"
        "- Extract terms that are EXPLICITLY mentioned in the LAST document\n"
        "- Follow the SAME extraction pattern as shown in examples\n"
        "- Return unique terms without duplicates\n"
        "- Use the same JSON format as demonstrated\n\n"
        "DON'T:\n"
        "- Hallucinate or invent terms not present in last the document\n"
        "- Repeat the same term multiple times\n"
        "- Deviate from the extraction style shown in examples\n\n"
        "OUTPUT FORMAT: Return a JSON object with a single field 'terms' containing a list of extracted terms."
    )

    def __init__(
        self,
        llm_model_id: str,
        retriever_model_id: str = "sentence-transformers/all-MiniLM-L6-v2",
        device: str = "cpu",
        top_k: int = 3,
        max_new_tokens: int = 256,
        max_input_length: int = 2048,
        use_tfidf: bool = False,
        seed: int = 42,
        restrict_to_known_types: bool = True,
        hf_token: str = "",
        local_files_only: bool = False,
        **kwargs: Any,
    ):
        """
        Parameters
        ----------
        llm_model_id:
            HuggingFace model id OR local path to a downloaded model directory.
        retriever_model_id:
            SentenceTransformer model id OR local path to a downloaded SBERT directory.
        device:
            Exact device string to place model on ("cpu", "cuda", "cuda:0", ...).
        top_k:
            Number of retrieved examples for few-shot prompting in each stage.
        max_new_tokens:
            Max tokens to generate for each prompt.
        max_input_length:
            Max prompt length before truncation.
        use_tfidf:
            If docs include TF-IDF suggestions (key "TF-IDF" or "tfidf_terms"), include them in prompts.
        seed:
            Seed for reproducibility.
        restrict_to_known_types:
            If True, append allowed type label list (from training) to system prompt in term->types stage.
            This helps exact-match evaluation by discouraging invented labels.
        hf_token:
            HuggingFace token for gated models (optional).
        local_files_only:
            If True, Transformers will not try to reach the internet (requires local cache / local path).
        """
        super().__init__(**kwargs)

        self.llm_model_id: str = llm_model_id
        self.retriever_model_id: str = retriever_model_id
        self.device: str = device
        self.top_k: int = int(top_k)
        self.max_new_tokens: int = int(max_new_tokens)
        self.max_input_length: int = int(max_input_length)
        self.use_tfidf: bool = bool(use_tfidf)
        self.seed: int = int(seed)
        self.restrict_to_known_types: bool = bool(restrict_to_known_types)
        self.hf_token: str = hf_token or ""
        self.local_files_only: bool = bool(local_files_only)

        self.model: Optional[AutoModelForCausalLM] = None
        self.tokenizer: Optional[AutoTokenizer] = None
        self._loaded: bool = False

        # Internal retrievers (always used in method-1, even in "llm-only" pipeline mode)
        self.doc_retriever = AutoRetriever()
        self.term_retriever = AutoRetriever()

        # Indexed corpora as JSON strings
        self._doc_examples_json: List[str] = []
        self._term_examples_json: List[str] = []

        # Cached allowed type labels (for optional restriction)
        self._allowed_types: List[str] = []

    def tasks_data_former(self, data: Any, task: str, test: bool = False):
        """
        Override base formatter: for task='text2onto' return data unchanged.
        """
        if task == "text2onto":
            return data
        return super().tasks_data_former(data=data, task=task, test=test)

    def load(self, **kwargs: Any):
        """
        Called by LearnerPipeline as: learner.load(model_id=llm_id)

        We accept overrides via kwargs:
          - model_id / llm_model_id
          - device, top_k, max_new_tokens, max_input_length, use_tfidf, seed, restrict_to_known_types
          - hf_token, local_files_only
        """
        model_id = kwargs.get("model_id") or kwargs.get("llm_model_id")
        if model_id:
            self.llm_model_id = str(model_id)

        for k in [
            "device",
            "top_k",
            "max_new_tokens",
            "max_input_length",
            "use_tfidf",
            "seed",
            "restrict_to_known_types",
            "hf_token",
            "local_files_only",
            "retriever_model_id",
        ]:
            if k in kwargs:
                setattr(self, k, kwargs[k])

        if self._loaded:
            return

        torch.manual_seed(self.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.seed)

        dev = str(self.device).strip()
        if dev.startswith("cuda") and not torch.cuda.is_available():
            raise RuntimeError(f"Device was set to '{dev}', but CUDA is not available.")

        dtype = torch.bfloat16 if dev.startswith("cuda") else torch.float32

        tok_kwargs: Dict[str, Any] = {"local_files_only": self.local_files_only}
        if self.hf_token:
            tok_kwargs["token"] = self.hf_token
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.llm_model_id, **tok_kwargs)
        except TypeError:
            tok_kwargs.pop("token", None)
            if self.hf_token:
                tok_kwargs["use_auth_token"] = self.hf_token
            self.tokenizer = AutoTokenizer.from_pretrained(self.llm_model_id, **tok_kwargs)

        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token


        model_kwargs: Dict[str, Any] = {"local_files_only": self.local_files_only}
        if self.hf_token:
            model_kwargs["token"] = self.hf_token

        try:
            self.model = AutoModelForCausalLM.from_pretrained(
                self.llm_model_id,
                dtype=dtype,
                **model_kwargs,
            )
        except TypeError:
            model_kwargs.pop("token", None)
            if self.hf_token:
                model_kwargs["use_auth_token"] = self.hf_token
            self.model = AutoModelForCausalLM.from_pretrained(
                self.llm_model_id,
                torch_dtype=dtype,
                **model_kwargs,
            )

        self.model = self.model.to(dev)

        self.doc_retriever.load(self.retriever_model_id)
        self.term_retriever.load(self.retriever_model_id)

        self._loaded = True


    def _format_doc(self, title: str, text: str, tfidf: Optional[List[str]] = None) -> str:
        """
        Format doc as the retriever query and as the user prompt content.
        """
        s = f"Title: {title}\n\nText:\n{text}"
        if tfidf:
            s += f"\n\nTF-IDF based suggestions: {tfidf}"
        return s

    def _apply_chat_template(self, conversation: List[Dict[str, str]]) -> str:
        """
        Convert conversation into a single prompt string using the tokenizer's chat template if available.
        """
        assert self.tokenizer is not None
        if hasattr(self.tokenizer, "apply_chat_template"):
            return self.tokenizer.apply_chat_template(
                conversation, add_generation_prompt=True, tokenize=False
            )

        parts = []
        for t in conversation:
            parts.append(f"{t['role'].upper()}:\n{t['content']}\n")
        parts.append("ASSISTANT:\n")
        return "\n".join(parts)

    def _extract_first_json_obj(self, text: str) -> Optional[dict]:
        """
        Extract the first valid JSON object from generated text by scanning balanced {...}.
        """
        starts = [i for i, ch in enumerate(text) if ch == "{"]

        for s in starts:
            depth = 0
            for e in range(s, len(text)):
                if text[e] == "{":
                    depth += 1
                elif text[e] == "}":
                    depth -= 1
                    if depth == 0:
                        candidate = text[s : e + 1].strip().replace("\n", " ")
                        try:
                            return json.loads(candidate)
                        except Exception:
                            try:
                                candidate2 = re.sub(r"'", '"', candidate)
                                return json.loads(candidate2)
                            except Exception:
                                pass
                        break
        return None

    def _dedup_clean(self, items: List[str]) -> List[str]:
        """
        Normalize and deduplicate strings (case-insensitive).
        """
        out: List[str] = []
        seen = set()
        for x in items or []:
            if not isinstance(x, str):
                continue
            x2 = re.sub(r"\s+", " ", x.strip())
            if not x2:
                continue
            k = x2.lower()
            if k in seen:
                continue
            seen.add(k)
            out.append(x2)
        return out

    def _doc_id(self, d: Dict[str, Any]) -> str:
        """
        Extract doc_id from common keys: doc_id, id, docid.
        """
        return str(d.get("doc_id") or d.get("id") or d.get("docid") or "")

    def _extract_documents(self, data: Any) -> List[Dict[str, Any]]:
        """
        Accept list-of-docs OR dict with 'documents'/'docs'.
        """
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            if isinstance(data.get("documents"), list):
                return data["documents"]
            if isinstance(data.get("docs"), list):
                return data["docs"]
        raise ValueError("Expected dict with 'documents' (or 'docs'), or a list of docs.")

    def _normalize_terms2docs(self, raw_terms2docs: Any, docs: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """
        Normalize mapping to: term -> [doc_id, ...].

        If caller accidentally provides inverted mapping: doc_id -> [term, ...],
        we detect it (keys mostly match doc_ids) and invert it.
        """
        if not isinstance(raw_terms2docs, dict) or not raw_terms2docs:
            return {}

        doc_ids = {self._doc_id(d) for d in docs}
        doc_ids.discard("")

        keys = list(raw_terms2docs.keys())
        sample = keys[:200]
        hits = sum(1 for k in sample if str(k) in doc_ids)

        if sample and hits >= int(0.6 * len(sample)):
            term2docs: Dict[str, List[str]] = defaultdict(list)
            for did, terms in raw_terms2docs.items():
                did = str(did)
                if did not in doc_ids:
                    continue
                for t in (terms or []):
                    if isinstance(t, str) and t.strip():
                        term2docs[t.strip()].append(did)
            return {t: self._dedup_clean(ds) for t, ds in term2docs.items()}

        norm: Dict[str, List[str]] = {}
        for term, doc_list in raw_terms2docs.items():
            if not isinstance(term, str) or not term.strip():
                continue
            docs_norm = [str(d) for d in (doc_list or []) if str(d)]
            if docs_norm:
                norm[term.strip()] = self._dedup_clean(docs_norm)
        return norm

    def _generate(self, prompt: str) -> str:
        """
        Deterministic single-prompt generation (no sampling).
        Returns decoded completion only.
        """
        assert self.model is not None and self.tokenizer is not None

        enc = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=self.max_input_length,
        )
        enc = {k: v.to(self.model.device) for k, v in enc.items()}

        with torch.no_grad():
            out = self.model.generate(
                **enc,
                max_new_tokens=self.max_new_tokens,
                do_sample=False,
                num_beams=1,
                pad_token_id=self.tokenizer.eos_token_id,
            )

        gen_tokens = out[0][enc["input_ids"].shape[1] :]
        return self.tokenizer.decode(gen_tokens, skip_special_tokens=True).strip()

    def _retrieve_doc_fewshot(self, doc: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Retrieve top-k doc examples (JSON dicts) for few-shot doc->terms prompting.
        """
        q = self._format_doc(doc.get("title", ""), doc.get("text", ""))
        hits = self.doc_retriever.retrieve([q], top_k=self.top_k)[0]

        out: List[Dict[str, Any]] = []
        for h in hits:
            try:
                out.append(json.loads(h))
            except Exception:
                continue
        return out

    def _retrieve_term_fewshot(self, term: str) -> List[Dict[str, Any]]:
        """
        Retrieve top-k term examples (JSON dicts) for few-shot term->types prompting.
        """
        hits = self.term_retriever.retrieve([term], top_k=self.top_k)[0]

        out: List[Dict[str, Any]] = []
        for h in hits:
            try:
                out.append(json.loads(h))
            except Exception:
                continue
        return out

    def _doc_to_terms(self, doc: Dict[str, Any]) -> List[str]:
        """
        Predict terms for a document using few-shot prompting + doc retrieval.
        """
        fewshot = self._retrieve_doc_fewshot(doc)

        convo: List[Dict[str, str]] = [{"role": "system", "content": self.DOC2TERMS_SYSTEM_PROMPT}]

        for ex in fewshot:
            ex_tfidf = ex.get("TF-IDF") or ex.get("tfidf_terms") or []
            convo += [
                {
                    "role": "user",
                    "content": self._format_doc(
                        ex.get("title", ""),
                        ex.get("text", ""),
                        ex_tfidf if self.use_tfidf else None,
                    ),
                },
                {
                    "role": "assistant",
                    "content": json.dumps({"terms": ex.get("OL", [])}, ensure_ascii=False),
                },
            ]

        tfidf = doc.get("TF-IDF") or doc.get("tfidf_terms") or []
        convo.append(
            {
                "role": "user",
                "content": self._format_doc(
                    doc.get("title", ""),
                    doc.get("text", ""),
                    tfidf if self.use_tfidf else None,
                ),
            }
        )

        prompt = self._apply_chat_template(convo)
        gen = self._generate(prompt)
        parsed = self._extract_first_json_obj(gen) or {}
        return self._dedup_clean(parsed.get("terms", []))

    def _term_to_types(self, term: str) -> List[str]:
        """
        Predict types for a term using few-shot prompting + term retrieval.
        """
        fewshot = self._retrieve_term_fewshot(term)

        system = self.TERM2TYPES_SYSTEM_PROMPT
        if self.restrict_to_known_types and self._allowed_types:
            allowed_block = "\n".join(f"- {t}" for t in self._allowed_types)
            system = (
                system
                + "\n\nIMPORTANT CONSTRAINT:\n"
                + "Choose ONLY from the following valid ontology types (do not invent new labels):\n"
                + allowed_block
            )

        convo: List[Dict[str, str]] = [{"role": "system", "content": system}]

        for ex in fewshot:
            convo += [
                {"role": "user", "content": f"Term: {ex.get('term','')}"},
                {
                    "role": "assistant",
                    "content": json.dumps({"types": ex.get("types", [])}, ensure_ascii=False),
                },
            ]

        convo.append({"role": "user", "content": f"Term: {term}"})

        prompt = self._apply_chat_template(convo)
        gen = self._generate(prompt)
        parsed = self._extract_first_json_obj(gen) or {}
        return self._dedup_clean(parsed.get("types", []))

    def _text2onto(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        Train or predict for task="text2onto".

        Returns:
          - training: None
          - prediction: {"terms": [...], "types": [...]}
        """
        if not self._loaded:
            self.load(model_id=self.llm_model_id, device=self.device)

        if not isinstance(data, dict):
            raise ValueError("text2onto expects a dict with documents + mappings.")

        docs = self._extract_documents(data)

        raw_terms2docs = data.get("terms2docs") or data.get("term2docs") or {}
        terms2types = data.get("terms2types") or data.get("term2types") or {}

        terms2docs = self._normalize_terms2docs(raw_terms2docs, docs)

        if not test:
            self._allowed_types = sorted(
                {
                    ty.strip()
                    for tys in (terms2types or {}).values()
                    for ty in (tys or [])
                    if isinstance(ty, str) and ty.strip()
                }
            )

            # build doc->terms from term->docs
            doc2terms: Dict[str, List[str]] = defaultdict(list)
            for term, doc_ids in (terms2docs or {}).items():
                for did in (doc_ids or []):
                    doc2terms[str(did)].append(term)

            # doc few-shot corpus: doc + gold OL terms
            doc_examples: List[Dict[str, Any]] = []
            for d in docs:
                did = self._doc_id(d)
                ex = dict(d)
                ex["doc_id"] = did
                ex["OL"] = self._dedup_clean(doc2terms.get(did, []))
                doc_examples.append(ex)

            # term few-shot corpus: term + gold types
            term_examples = [
                {"term": t, "types": self._dedup_clean(tys)}
                for t, tys in (terms2types or {}).items()
            ]

            # store as JSON strings so retrievers return parseable strings
            self._doc_examples_json = [json.dumps(ex, ensure_ascii=False) for ex in doc_examples]
            self._term_examples_json = [json.dumps(ex, ensure_ascii=False) for ex in term_examples]

            # index retrievers
            self.doc_retriever.index(self._doc_examples_json)
            self.term_retriever.index(self._term_examples_json)
            return None

        doc2terms_pred: Dict[str, List[str]] = {}
        for d in docs:
            did = self._doc_id(d)
            doc2terms_pred[did] = self._doc_to_terms(d)

        unique_terms = sorted({t for ts in doc2terms_pred.values() for t in ts})
        term2types_pred: Dict[str, List[str]] = {t: self._term_to_types(t) for t in unique_terms}

        doc2types_pred: Dict[str, List[str]] = {}
        for did, terms in doc2terms_pred.items():
            tys: List[str] = []
            for t in terms:
                tys.extend(term2types_pred.get(t, []))
            doc2types_pred[did] = self._dedup_clean(tys)

        pred_terms = [{"doc_id": did, "term": t} for did, ts in doc2terms_pred.items() for t in ts]
        pred_types = [{"doc_id": did, "type": ty} for did, tys in doc2types_pred.items() for ty in tys]

        return {"terms": pred_terms, "types": pred_types}
