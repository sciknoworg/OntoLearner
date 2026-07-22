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
"""Semantic-Swingers term-typing learner (LLMs4OL 2026, Task B).

Closed-vocabulary term typing: ``fit`` learns the inventory of allowed type labels
from the train split, and at inference a selector assigns types to each term from
that inventory only. Three selectors are provided (mirroring the team's Task C
taxonomy-discovery learner):

* ``"embedding"`` (default) — fully offline/deterministic; each term gets its
  nearest type label by sentence-embedding cosine similarity. No API key needed.
* ``"openai"`` — the competition champion; an OpenAI chat model classifies terms
  against the closed vocabulary with a precision-biased prompt. Enabled only when
  an ``api_key`` is supplied (never hard-coded).
* ``"ollama"`` — free, local reproduction of the champion: the same classification
  prompt is served by a local Ollama model through its OpenAI-compatible endpoint.
"""
from __future__ import annotations

import json
import os
import re
from typing import Any, Dict, List, Optional

import numpy as np
from sentence_transformers import SentenceTransformer

from ...base import AutoLearner

_SYSTEM = (
    "You are an expert ontology engineer specialising in term-typing. "
    "You are given terms and a closed vocabulary of allowed type labels. "
    "Rules: (1) assign a type only when confident — precision over recall; "
    "(2) a term may have multiple types; "
    "(3) if no allowed type fits, return an empty list for that term; "
    "(4) copy type labels EXACTLY as given, case-sensitive. "
    'Answer as JSON: {"typings": [{"term": "...", "types": ["..."]}]}'
)


def _reasoning_off(model: Optional[str]) -> Dict[str, Any]:
    """Extra request kwargs that disable a thinking model's hidden reasoning pass.

    Qwen3.x served over an OpenAI-compatible endpoint (e.g. Ollama) is a *thinking*
    model: left on, it spends the whole ``max_tokens`` budget on reasoning and returns
    empty content (``finish_reason="length"``, ``content=""``), so the selector parses
    nothing and scores 0. Passing ``reasoning_effort="none"`` via ``extra_body`` turns
    that off — the same fix the competition pipeline applies for the qwen+RAG=0 failure.
    A no-op for non-qwen3 models, so it is always safe to include.
    """
    if str(model or "").startswith("qwen3"):
        return {"extra_body": {"reasoning_effort": "none"}}
    return {}


class SemanticSwingersTermTypingLearner(AutoLearner):
    """Closed-vocabulary term typing with a swappable type selector.

    Args:
        embedding_model: SentenceTransformer id used by the ``"embedding"`` selector.
            Defaults to ``mixedbread-ai/mxbai-embed-large-v1`` (the team's champion encoder).
        selector: ``"embedding"`` (offline nearest-type), ``"openai"`` (champion LLM
            classification), or ``"ollama"`` (local LLM classification, no API key).
        llm_model: Chat model id used by the LLM selectors. Defaults to
            ``gpt-4.1-mini`` for ``"openai"`` and ``llama3.1:8b`` for ``"ollama"``.
        api_key: OpenAI API key for ``selector="openai"``. If ``None``, falls back to
            the ``OPENAI_API_KEY`` env var; if still unset, the learner silently
            degrades to the embedding selector. Ignored by ``"ollama"``.
        base_url: OpenAI-compatible endpoint for the LLM selector. Defaults to the
            local Ollama server (``http://localhost:11434/v1``) when
            ``selector="ollama"``, and to the OpenAI API otherwise.
        max_tokens: Completion budget per LLM request. Thinking models (e.g. Qwen3.5)
            spend reasoning tokens before answering and need a much larger budget.
        batch_size: Number of terms classified per LLM request.
        device: Torch device for the encoder.
    """

    _OLLAMA_BASE_URL = "http://localhost:11434/v1"
    _DEFAULT_LLM = {"openai": "gpt-4.1-mini", "ollama": "llama3.1:8b"}

    def __init__(
        self,
        embedding_model: str = "mixedbread-ai/mxbai-embed-large-v1",
        selector: str = "embedding",
        llm_model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        max_tokens: int = 1024,
        batch_size: int = 20,
        device: str = "cpu",
    ) -> None:
        """Initialise the learner and record configuration (no I/O yet)."""
        super().__init__()
        self.embedding_model = embedding_model
        self.selector = selector
        self.llm_model = llm_model or self._DEFAULT_LLM.get(selector)
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if base_url is None and selector == "ollama":
            base_url = self._OLLAMA_BASE_URL
        self.base_url = base_url
        self.max_tokens = max_tokens
        self.batch_size = batch_size
        self.device = device
        self._encoder: Optional[SentenceTransformer] = None
        self._allowed_types: List[str] = []

    def load(self, model_id: Optional[str] = None, **kwargs: Any) -> None:
        """Load the sentence-embedding encoder.

        Called by ``LearnerPipeline`` as ``load(model_id=llm_id)``. A model id that
        looks like a SentenceTransformer path (contains ``/``) overrides the default;
        a plain bookkeeping label is ignored.
        """
        if model_id and "/" in model_id:
            self.embedding_model = model_id
        self._encoder = SentenceTransformer(self.embedding_model, device=self.device)

    def _select_embedding(self, terms: List[str]) -> List[Dict[str, Any]]:
        """Offline selector: each term gets its nearest type label by cosine similarity."""
        if self._encoder is None:
            self.load()
        type_emb = np.asarray(
            self._encoder.encode(
                self._allowed_types, normalize_embeddings=True, show_progress_bar=False
            )
        )
        term_emb = np.asarray(
            self._encoder.encode(terms, normalize_embeddings=True, show_progress_bar=False)
        )
        sim = term_emb @ type_emb.T
        best = np.argmax(sim, axis=1)
        return [
            {"term": term, "types": [self._allowed_types[int(best[i])]]}
            for i, term in enumerate(terms)
        ]

    def _parse_typings(self, content: str, allowed: set) -> Dict[str, List[str]]:
        """Parse an LLM answer into ``term -> types``, enforcing the closed vocabulary."""
        text = content.strip()
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            match = re.search(r"\{.*\}", text, flags=re.DOTALL)
            if not match:
                return {}
            try:
                payload = json.loads(match.group(0))
            except json.JSONDecodeError:
                return {}
        items = payload.get("typings", payload) if isinstance(payload, dict) else payload
        out: Dict[str, List[str]] = {}
        if not isinstance(items, list):
            return out
        for item in items:
            if not isinstance(item, dict):
                continue
            term = item.get("term")
            types = [t for t in item.get("types", []) if t in allowed]
            if term:
                out[str(term)] = types
        return out

    def _select_llm(self, terms: List[str]) -> List[Dict[str, Any]]:
        """LLM selector: a chat model classifies term batches against the vocabulary.

        Serves both the ``"openai"`` champion and the local ``"ollama"`` fallback —
        the latter is just an OpenAI-compatible endpoint with a placeholder key.
        """
        from openai import OpenAI

        api_key = self.api_key if self.selector == "openai" else (self.api_key or "ollama")
        client = OpenAI(api_key=api_key, base_url=self.base_url)
        allowed = set(self._allowed_types)
        vocab_block = "\n".join(f"- {t}" for t in self._allowed_types)
        preds: List[Dict[str, Any]] = []
        for start in range(0, len(terms), self.batch_size):
            batch = terms[start : start + self.batch_size]
            user = (
                "Terms to classify:\n"
                + "\n".join(f"- {t}" for t in batch)
                + "\n\nAllowed type vocabulary (use ONLY these exact labels):\n"
                + vocab_block
                + "\n\nAssign types to each term. Answer as JSON."
            )
            params: Dict[str, Any] = dict(
                model=self.llm_model,
                messages=[
                    {"role": "system", "content": _SYSTEM},
                    {"role": "user", "content": user},
                ],
                temperature=0,
                max_tokens=self.max_tokens,
                **_reasoning_off(self.llm_model),
            )
            try:
                resp = client.chat.completions.create(
                    response_format={"type": "json_object"}, **params
                )
            except Exception:
                resp = client.chat.completions.create(**params)
            typed = self._parse_typings(resp.choices[0].message.content or "", allowed)
            preds.extend({"term": t, "types": typed.get(t, [])} for t in batch)
        return preds

    def _term_typing(self, data: Any, test: bool = False) -> Optional[List[Dict[str, Any]]]:
        """Train mode: learn the type inventory. Test mode: type each term."""
        if not test:
            self._allowed_types = sorted(set(data))
            return None
        terms = [str(t) for t in data]
        if not terms or not self._allowed_types:
            return [{"term": t, "types": []} for t in terms]
        use_llm = self.selector == "ollama" or (self.selector == "openai" and self.api_key)
        return self._select_llm(terms) if use_llm else self._select_embedding(terms)
