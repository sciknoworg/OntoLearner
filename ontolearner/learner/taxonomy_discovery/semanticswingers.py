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
the parent for each child. Two selectors are provided:

* ``"embedding"`` (default) — fully offline/deterministic; the most *general* candidate
  (highest mean similarity to the vocabulary) is chosen as parent. No API key needed.
* ``"openai"`` — the competition champion; an OpenAI chat model picks the parent from
  the retrieved candidates. Enabled only when an ``api_key`` is supplied (never hard-coded).

The team's finding is that the *encoder* is the bottleneck for this task, so the default
encoder is ``mixedbread-ai/mxbai-embed-large-v1`` (a clean, no-fine-tuning +0.03 over MiniLM).
"""
from __future__ import annotations

import os
from typing import Any, List, Optional

import numpy as np
from sentence_transformers import SentenceTransformer

from ...base import AutoLearner


class SemanticSwingersTaxonomyLearner(AutoLearner):
    """Embedding-retrieval taxonomy induction with a swappable parent selector.

    Args:
        embedding_model: SentenceTransformer id used to embed type labels. Defaults to
            ``mixedbread-ai/mxbai-embed-large-v1`` (the team's champion encoder).
        top_k: Number of candidate parents retrieved per child before selection.
        selector: ``"embedding"`` (offline heuristic) or ``"openai"`` (LLM selection).
        openai_model: Chat model id used when ``selector="openai"``.
        api_key: OpenAI API key. If ``None``, falls back to the ``OPENAI_API_KEY`` env
            var; if still unset, the learner silently degrades to the embedding selector.
        device: Torch device for the encoder.
    """

    def __init__(
        self,
        embedding_model: str = "mixedbread-ai/mxbai-embed-large-v1",
        top_k: int = 30,
        selector: str = "embedding",
        openai_model: str = "gpt-4.1-mini",
        api_key: Optional[str] = None,
        device: str = "cpu",
    ) -> None:
        """Initialise the learner and record configuration (no I/O yet)."""
        super().__init__()
        self.embedding_model = embedding_model
        self.top_k = top_k
        self.selector = selector
        self.openai_model = openai_model
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
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

    def _select_openai(self, nodes: List[str], sim: np.ndarray) -> List[dict]:
        """Champion selector: an OpenAI chat model picks the parent from candidates."""
        from openai import OpenAI

        client = OpenAI(api_key=self.api_key)
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
                model=self.openai_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=32,
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
        use_openai = self.selector == "openai" and self.api_key
        return self._select_openai(nodes, sim) if use_openai else self._select_embedding(nodes, sim)
