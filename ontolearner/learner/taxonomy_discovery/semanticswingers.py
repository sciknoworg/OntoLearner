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
from sentence_transformers import SentenceTransformer, utils

import torch
import torch.nn as nn
import networkx as nx

from ...base import AutoLearner

#: Default parent-selection instruction for the LLM selectors. A template with ``{child}`` and
#: ``{candidates}`` placeholders; override per-instance via the ``selection_prompt`` argument.
_SELECTION_PROMPT = (
    "Which of the following is the most likely direct parent (superclass) of '{child}'? "
    "Answer with exactly one option or 'NONE'.\n{candidates}"
)


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
        selection_prompt: Optional[str] = None,
    ) -> None:
        """Initialise the learner and record configuration (no I/O yet).

        ``selection_prompt`` is the parent-selection instruction for the LLM selectors — a template
        with ``{child}`` and ``{candidates}`` placeholders. Defaults to :data:`_SELECTION_PROMPT`;
        override to change the phrasing / task framing without subclassing.
        """
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
        self.selection_prompt = selection_prompt or _SELECTION_PROMPT
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
            prompt = self.selection_prompt.format(
                child=child, candidates="\n".join(f"- {c}" for c in candidates)
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


class BilinearAdjacencyLayer(nn.Module):
    """1024-D Structural Matrix Layer mapping Child -> Parent asymmetric space."""
    def __init__(self, embedding_dim: int = 1024):
        super().__init__()
        self.W = nn.Linear(embedding_dim, embedding_dim, bias=False)

    def forward(self, child: torch.Tensor, parent: torch.Tensor) -> torch.Tensor:
        transformed_child = self.W(child)
        return torch.sum(transformed_child * parent, dim=-1)


class SemanticSwingersMatrixTaxonomyLearner(SemanticSwingersTaxonomyLearner):
    """Hybrid Structural Matrix + LLM Taxonomy Discovery Learner (Champion Approach)."""

    def __init__(
        self,
        embedding_model: str = "mixedbread-ai/mxbai-embed-large-v1",
        matrix_weights_path: str = "structural_matrix_w_1024_mxbai.pt",
        top_k: int = 10,
        llm_threshold: int = 1000,
        **kwargs
    ) -> None:
        # Pass backend/LLM args up to his constructor
        super().__init__(embedding_model=embedding_model, top_k=top_k, **kwargs)
        self.matrix_weights_path = matrix_weights_path
        self.llm_threshold = llm_threshold
        # Force PyTorch device detection
        self.device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")
        self._structural_layer = None

    def load(self, model_id: Optional[str] = None, **kwargs: Any) -> None:
        """Override load to instantiate PyTorch tensors and the Matrix layer."""
        super().load(model_id, **kwargs) # Loads the standard SentenceTransformer
        
        embedding_dim = self._encoder.get_sentence_embedding_dimension()
        self._structural_layer = BilinearAdjacencyLayer(embedding_dim=embedding_dim).to(self.device)
        
        if os.path.exists(self.matrix_weights_path):
            self._structural_layer.load_state_dict(torch.load(self.matrix_weights_path, map_location=self.device))
            self._structural_layer.eval()

    def _cleanup_graph(self, raw_predictions: List[dict]) -> List[dict]:
        """Enforces DAG rules via NetworkX cycle breaking and Transitive Reduction."""
        if not raw_predictions: return []
        G = nx.DiGraph()
        for p in raw_predictions: G.add_edge(p["parent"], p["child"])
            
        while not nx.is_directed_acyclic_graph(G):
            try:
                cycle = nx.find_cycle(G)
                G.remove_edge(cycle[0][0], cycle[0][1])
            except nx.NetworkXNoCycle:
                break
                
        G_reduced = nx.transitive_reduction(G)
        return [{"parent": str(u), "child": str(v)} for u, v in G_reduced.edges()]

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[Any]:
        """Override the core logic to use the 1024-D Matrix and hybrid fallback."""
        if not test: 
            return None
        if self._encoder is None or self._structural_layer is None: 
            self.load()

        nodes = self._nodes(data) # Reusing his method!
        if not nodes: 
            return []

        # 1. Generate Embeddings for the entire vocabulary
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"Encoding {len(nodes)} concept nodes...")
        
        embeddings = self._encoder.encode(nodes, convert_to_tensor=True, show_progress_bar=False)
        
        raw_preds = []
        # Fallback to Pure Matrix if dataset > llm_threshold to prevent timeout
        use_llm = (len(nodes) <= self.llm_threshold) and (self.selector in ["openai", "ollama"])
        
        for child_idx, child in enumerate(nodes):
            child_vec = embeddings[child_idx]
            
            # Step 1: Semantic Candidate Retrieval (Top 41 to safely exclude self)
            cos_scores = util.cos_sim(child_vec, embeddings)[0]
            top_semantic = torch.topk(cos_scores, k=min(41, len(nodes)))
            
            candidate_indices = [idx for idx in top_semantic[1].tolist() if idx != child_idx]
            if not candidate_indices:
                continue
                
            candidate_vecs = torch.stack([embeddings[idx] for idx in candidate_indices])
            candidates = [nodes[idx] for idx in candidate_indices]
            
            child_vec_expanded = child_vec.unsqueeze(0).repeat(candidate_vecs.size(0), 1)
            
            # Step 2: 1024-D Structural Matrix Scoring
            with torch.no_grad():
                structural_scores = self._structural_layer(child_vec_expanded, candidate_vecs)
                
            # Step 3: Routing (LLM Verification vs. High-Speed Matrix Bypass)
            if use_llm:
                # Send top K structural candidates to LLM selector
                ranked_indices = torch.argsort(structural_scores, descending=True)[:min(self.top_k, len(candidates))]
                top_candidates = [candidates[idx] for idx in ranked_indices]
                parent = self._select_llm_parent(child, top_candidates)
                if parent:
                    raw_preds.append({"parent": parent, "child": child})
            else:
                # Dataset is massive: take the #1 matrix candidate instantly
                best_idx = torch.argmax(structural_scores).item()
                raw_preds.append({"parent": candidates[best_idx], "child": child})

        # Step 4: Clean the graph (Cycle-Breaking + Transitive Reduction)
        return self._cleanup_graph(raw_preds)

    def _select_llm_parent(self, child: str, candidates: List[str]) -> Optional[str]:
        """Helper method to ask the LLM to pick the best parent from the matrix's short-list."""
        from openai import OpenAI
        from ontolearner.learner.taxonomy_discovery.semanticswingers import _reasoning_off
        
        api_key = self.api_key if self.selector == "openai" else (self.api_key or "ollama")
        client = OpenAI(api_key=api_key, base_url=self.base_url)
        
        prompt = self.selection_prompt.format(
            child=child, candidates="\n".join(f"- {c}" for c in candidates)
        )
        try:
            resp = client.chat.completions.create(
                model=self.llm_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=self.max_tokens,
                **_reasoning_off(self.llm_model) # Reuses his Qwen fix!
            )
            answer = (resp.choices[0].message.content or "").strip()
            for cand in candidates:
                if cand.lower() in answer.lower():
                    return cand
        except Exception as e:
            import logging
            logging.getLogger(__name__).error(f"LLM selection failed for {child}: {e}")
        return None
