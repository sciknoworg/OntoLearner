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
"""Semantic-Swingers taxonomy-discovery learner (LLMs4OL 2026, Task C).

A retrieval-first taxonomy inducer: a sentence-embedding encoder embeds the type
vocabulary, nearest neighbours become candidate parents, and a selection step picks
the parent for each child. Three selectors are provided:

* ``"embedding"`` (default) — fully offline/deterministic; the most *general* candidate
  (highest mean similarity to the vocabulary) is chosen as parent. No API key needed.
* ``"openai"`` — the competition champion; an OpenAI chat model picks the parent from
  the retrieved candidates. Enabled only when an ``api_key`` is supplied (never hard-coded).
* ``"ollama"`` — free, local reproduction of the champion: the same selection prompt is
  served by a local Ollama model through its OpenAI-compatible endpoint. No API key needed.

The team's finding is that the *encoder* is the bottleneck for this task, so the default
encoder is ``mixedbread-ai/mxbai-embed-large-v1`` (a clean, no-fine-tuning +0.03 over MiniLM).
"""
from __future__ import annotations

import os
from typing import Any, List, Optional

import numpy as np
from sentence_transformers import SentenceTransformer

from ...base import AutoLearner


def _reasoning_off(model: Optional[str]) -> dict:
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


class SemanticSwingersTaxonomyLearner(AutoLearner):
    """Embedding-retrieval taxonomy induction with a swappable parent selector.

    Args:
        embedding_model: SentenceTransformer id used to embed type labels. Defaults to
            ``mixedbread-ai/mxbai-embed-large-v1`` (the team's champion encoder).
        top_k: Number of candidate parents retrieved per child before selection.
        selector: ``"embedding"`` (offline heuristic), ``"openai"`` (champion LLM
            selection), or ``"ollama"`` (local LLM selection, no API key).
        llm_model: Chat model id used by the LLM selectors. Defaults to
            ``gpt-4.1-mini`` for ``"openai"`` and ``llama3.1:8b`` for ``"ollama"``.
        api_key: OpenAI API key for ``selector="openai"``. If ``None``, falls back to
            the ``OPENAI_API_KEY`` env var; if still unset, the learner silently
            degrades to the embedding selector. Ignored by ``"ollama"``.
        base_url: OpenAI-compatible endpoint for the LLM selector. Defaults to the
            local Ollama server (``http://localhost:11434/v1``) when
            ``selector="ollama"``, and to the OpenAI API otherwise.
        max_tokens: Completion budget for the LLM selector. Direct-answering models
            need very little; thinking models (e.g. Qwen3.5) spend reasoning tokens
            before answering and need a much larger budget (512+).
        device: Torch device for the encoder.
    """

    _OLLAMA_BASE_URL = "http://localhost:11434/v1"
    _DEFAULT_LLM = {"openai": "gpt-4.1-mini", "ollama": "llama3.1:8b"}

    def __init__(
        self,
        embedding_model: str = "mixedbread-ai/mxbai-embed-large-v1",
        top_k: int = 30,
        selector: str = "embedding",
        llm_model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        max_tokens: int = 64,
        device: str = "cpu",
    ) -> None:
        """Initialise the learner and record configuration (no I/O yet)."""
        super().__init__()
        self.embedding_model = embedding_model
        self.top_k = top_k
        self.selector = selector
        self.llm_model = llm_model or self._DEFAULT_LLM.get(selector)
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if base_url is None and selector == "ollama":
            base_url = self._OLLAMA_BASE_URL
        self.base_url = base_url
        self.max_tokens = max_tokens
        self.device = device
        self._encoder: Optional[SentenceTransformer] = None

    def load(self, model_id: Optional[str] = None, **kwargs: Any) -> None:
        """Load the sentence-embedding encoder.

        Called by ``LearnerPipeline`` as ``load(model_id=llm_id)``. A model id that looks
        like a SentenceTransformer path (contains ``/``) overrides the default; a plain
        bookkeeping label is ignored.
        """
        if model_id and "/" in model_id:
            self.embedding_model = model_id
        self._encoder = SentenceTransformer(self.embedding_model, device=self.device)

    def tasks_data_former(self, data: Any, task: str, test: bool = False) -> Any:
        """Pass the raw ``OntologyData`` through (run with ``ontologizer_data=False``)."""
        return data

    @staticmethod
    def _nodes(data: Any) -> List[str]:
        """Return the deduped type vocabulary (declared types + edge endpoints)."""
        tt = data.type_taxonomies
        nodes: List[str] = list(tt.types)
        for rel in tt.taxonomies:
            nodes.extend([rel.parent, rel.child])
        seen: set = set()
        out: List[str] = []
        for node in nodes:
            if node not in seen:
                seen.add(node)
                out.append(node)
        return out

    def _select_embedding(self, nodes: List[str], sim: np.ndarray) -> List[dict]:
        """Offline selector: the most general retrieved candidate is the parent.

        Generality is proxied by mean similarity to the whole vocabulary (a central,
        broadly-similar type tends to be a superclass). For each child we keep the top
        candidate that is more general than the child itself.
        """
        generality = sim.mean(axis=1)
        preds: List[dict] = []
        for child_idx, child in enumerate(nodes):
            candidates = np.argsort(-sim[child_idx])[: self.top_k]
            for parent_idx in candidates:
                if parent_idx == child_idx:
                    continue
                if generality[parent_idx] >= generality[child_idx]:
                    preds.append({"parent": nodes[int(parent_idx)], "child": child})
                    break
        return preds

    def _select_llm(self, nodes: List[str], sim: np.ndarray) -> List[dict]:
        """LLM selector: a chat model picks the parent from the retrieved candidates.

        Serves both the ``"openai"`` champion and the local ``"ollama"`` fallback —
        the latter is just an OpenAI-compatible endpoint with a placeholder key.
        """
        from openai import OpenAI

        api_key = self.api_key if self.selector == "openai" else (self.api_key or "ollama")
        client = OpenAI(api_key=api_key, base_url=self.base_url)
        preds: List[dict] = []
        for child_idx, child in enumerate(nodes):
            candidates = [
                nodes[int(i)]
                for i in np.argsort(-sim[child_idx])[: self.top_k]
                if int(i) != child_idx
            ]
            if not candidates:
                continue
            prompt = (
                f"Which of the following is the most likely direct parent (superclass) "
                f"of '{child}'? Answer with exactly one option or 'NONE'.\n"
                + "\n".join(f"- {c}" for c in candidates)
            )
            resp = client.chat.completions.create(
                model=self.llm_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=self.max_tokens,
                **_reasoning_off(self.llm_model),
            )
            answer = (resp.choices[0].message.content or "").strip()
            for cand in candidates:
                if cand.lower() in answer.lower():
                    preds.append({"parent": cand, "child": child})
                    break
        return preds

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[Any]:
        """Retrieval-only method: no training; induce edges at inference."""
        if not test:
            return None
        if self._encoder is None:
            self.load()
        nodes = self._nodes(data)
        emb = np.asarray(
            self._encoder.encode(nodes, normalize_embeddings=True, show_progress_bar=False)
        )
        sim = emb @ emb.T
        use_llm = self.selector == "ollama" or (self.selector == "openai" and self.api_key)
        return self._select_llm(nodes, sim) if use_llm else self._select_embedding(nodes, sim)
