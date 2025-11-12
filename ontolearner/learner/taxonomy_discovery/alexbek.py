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

from typing import Any, Dict, List, Optional, Tuple

import math
import os
import random
import torch
import torch.nn as nn
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

from ...base import AutoLearner


class RMSNorm(nn.Module):
    """Root Mean Square normalization with learnable scale.

    Computes per-position normalization:
        y = weight * x / sqrt(mean(x^2) + eps)

    This variant normalizes over the last dimension and keeps scale as a
    learnable parameter, similar to RMSNorm used in modern transformer stacks.
    """

    def __init__(self, dim: int, eps: float = 1e-6):
        """Initialize the RMSNorm layer.

        Args:
            dim: Size of the last (feature) dimension to normalize over.
            eps: Small constant added inside the square root for numerical
                stability.
        """
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Apply RMS normalization.

        Args:
            x: Input tensor of shape (..., dim).

        Returns:
            Tensor of the same shape as `x`, RMS-normalized over the last axis.
        """
        rms_inv = torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)
        return self.weight * (x * rms_inv)


class CrossAttentionHead(nn.Module):
    """Minimal multi-head *pair* scorer using cross-attention-style projections.

    Given child vector `c` and parent vector `p`:
        q = W_q * c,  k = W_k * p
        score_head = (q_h · k_h) / sqrt(d_head)

    We average the per-head scores and apply a sigmoid to produce a probability.
    This is not a full attention block—just a learnable similarity function.
    """

    def __init__(
        self, hidden_size: int, num_heads: int = 8, rms_norm_eps: float = 1e-6
    ):
        """Initialize projections and per-stream normalizers.

        Args:
            hidden_size: Dimensionality of input embeddings (child/parent).
            num_heads: Number of subspaces to split the projection into.
            rms_norm_eps: Epsilon for RMSNorm stability.

        Raises:
            AssertionError: If `hidden_size` is not divisible by `num_heads`.
        """
        super().__init__()
        assert hidden_size % num_heads == 0, (
            "hidden_size must be divisible by num_heads"
        )
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.dim_per_head = hidden_size // num_heads

        # Linear projections for queries (child) and keys (parent)
        self.query_projection = nn.Linear(hidden_size, hidden_size, bias=False)
        self.key_projection = nn.Linear(hidden_size, hidden_size, bias=False)

        # Pre-projection normalization for stability
        self.query_norm = RMSNorm(hidden_size, eps=rms_norm_eps)
        self.key_norm = RMSNorm(hidden_size, eps=rms_norm_eps)

        # Xavier init helps stabilize training
        nn.init.xavier_uniform_(self.query_projection.weight)
        nn.init.xavier_uniform_(self.key_projection.weight)

    def forward(
        self, child_embeddings: torch.Tensor, parent_embeddings: torch.Tensor
    ) -> torch.Tensor:
        """Score (child, parent) pairs.

        Args:
            child_embeddings: Tensor of shape (batch, hidden_size).
            parent_embeddings: Tensor of shape (batch, hidden_size).

        Returns:
            Tensor of probabilities with shape (batch,), each in [0, 1].
        """
        batch_size, _ = child_embeddings.shape

        # Project and normalize
        queries = self.query_norm(self.query_projection(child_embeddings))
        keys = self.key_norm(self.key_projection(parent_embeddings))

        # Reshape into heads: (batch, heads, dim_per_head)
        queries = queries.view(batch_size, self.num_heads, self.dim_per_head)
        keys = keys.view(batch_size, self.num_heads, self.dim_per_head)

        # Scaled dot-product similarity per head -> (batch, heads)
        per_head_scores = (queries * keys).sum(-1) / math.sqrt(self.dim_per_head)

        # Aggregate across heads -> (batch,)
        mean_score = per_head_scores.mean(-1)

        # Map to probability
        return torch.sigmoid(mean_score)


class AlexbekCrossAttnLearner(AutoLearner):
    """Cross-Attention Taxonomy Learner (inherits AutoLearner).

    Workflow
    - Encode terms with a SentenceTransformer.
    - Train a compact cross-attention head on (parent, child) pairs
      (positives + sampled negatives) using BCE loss.
    - Inference returns probabilities per pair; edges with prob >= 0.5 are
      labeled as positive.

    """

    def __init__(
        self,
        *,
        embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
        device: str = "cpu",
        num_heads: int = 8,
        lr: float = 5e-5,
        weight_decay: float = 0.01,
        num_epochs: int = 1,
        batch_size: int = 256,
        neg_ratio: float = 1.0,  # negatives per positive
        output_dir: str = "./results/",
        seed: int = 42,
        **kwargs: Any,
    ):
        """Configure the learner.

        Args:
            embedding_model: SentenceTransformer model id/path for term encoding.
            device: 'cuda' or 'cpu'. If 'cuda' is requested but unavailable, CPU
                is used.
            num_heads: Number of heads in the cross-attention scorer.
            lr: Learning rate for AdamW.
            weight_decay: Weight decay for AdamW.
            num_epochs: Number of epochs to train the head.
            batch_size: Minibatch size for training and scoring loops.
            neg_ratio: Number of sampled negatives per positive during training.
            output_dir: Directory to store artifacts (reserved for future use).
            seed: Random seed for reproducibility.
            **kwargs: Passed through to `AutoLearner` base init.

        Side Effects:
            Creates `output_dir` if missing and seeds Python/Torch RNGs.
        """
        super().__init__(**kwargs)

        # hyperparameters / settings
        self.embedding_model_id = embedding_model
        self.requested_device = device
        self.num_heads = num_heads
        self.learning_rate = lr
        self.weight_decay = weight_decay
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.negative_ratio = neg_ratio
        self.output_dir = output_dir
        self.seed = seed

        # Prefer requested device but gracefully fall back to CPU
        if torch.cuda.is_available() or self.requested_device == "cpu":
            self.device = torch.device(self.requested_device)
        else:
            self.device = torch.device("cpu")

        # Will be set in load()
        self.embedder: Optional[SentenceTransformer] = None
        self.cross_attn_head: Optional[CrossAttentionHead] = None
        self.embedding_dim: Optional[int] = None

        # Cache of term -> embedding tensor (on device)
        self.term_to_vector: Dict[str, torch.Tensor] = {}

        os.makedirs(self.output_dir, exist_ok=True)
        random.seed(self.seed)
        torch.manual_seed(self.seed)

    def load(self, **kwargs: Any):
        """Load the sentence embedding model and initialize the cross-attention head.

        Args:
            **kwargs: Optional override, supports `embedding_model`.

        Side Effects:
            - Initializes `self.embedder` on the configured device.
            - Probes and stores `self.embedding_dim`.
            - Constructs `self.cross_attn_head` with the probed dimensionality.
        """
        model_id = kwargs.get("embedding_model", self.embedding_model_id)
        self.embedder = SentenceTransformer(
            model_id, trust_remote_code=True, device=str(self.device)
        )

        # Probe output dimensionality using a dummy encode
        probe_embedding = self.embedder.encode(
            ["_dim_probe_"], convert_to_tensor=True, normalize_embeddings=False
        )
        self.embedding_dim = int(probe_embedding.shape[-1])

        # Initialize the cross-attention head
        self.cross_attn_head = CrossAttentionHead(
            hidden_size=self.embedding_dim, num_heads=self.num_heads
        ).to(self.device)

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[Any]:
        """Train or infer taxonomy edges according to the AutoLearner contract.

        Training (`test=False`)
            - Extract positives (parent, child) and the unique term set from `data`.
            - Build/extend the term embedding cache.
            - Sample negatives at ratio `self.negative_ratio`.
            - Train the cross-attention head with BCE loss.

        Inference (`test=True`)
            - Ensure embeddings exist for all terms.
            - Score candidate pairs and return per-pair probabilities and labels.

        Args:
            data: Ontology-like object exposing `type_taxonomies.taxonomies`,
                where each item has `.parent` and `.child` string-like fields.
            test: If True, perform inference instead of training.

        Returns:
            - `None` on training.
            - On inference: List of dicts
              `{"parent": str, "child": str, "score": float, "label": int}`.
        """
        if self.embedder is None or self.cross_attn_head is None:
            self.load()

        if not test:
            positive_pairs, unique_terms = self._extract_parent_child_pairs_and_terms(
                data
            )
            self._ensure_term_embeddings(unique_terms)
            negative_pairs = self._sample_negative_pairs(
                positive_pairs, unique_terms, ratio=self.negative_ratio, seed=self.seed
            )
            self._train_cross_attn_head(positive_pairs, negative_pairs)
            return None
        else:
            candidate_pairs, unique_terms = self._extract_parent_child_pairs_and_terms(
                data
            )
            self._ensure_term_embeddings(unique_terms, append_only=True)
            probabilities = self._score_parent_child_pairs(candidate_pairs)

            predictions = [
                {
                    "parent": parent,
                    "child": child,
                    "score": float(prob),
                    "label": int(prob >= 0.5),
                }
                for (parent, child), prob in zip(candidate_pairs, probabilities)
            ]
            return predictions

    def _ensure_term_embeddings(
        self, terms: List[str], append_only: bool = False
    ) -> None:
        """Encode terms with the sentence embedder and store in cache.

        Args:
            terms: List of unique term strings to embed.
            append_only: If True, only embed terms missing from the cache;
                otherwise (re)encode all provided terms.

        Raises:
            RuntimeError: If called before `load()`.
        """
        if self.embedder is None:
            raise RuntimeError("Call load() before building term embeddings")

        terms_to_encode = (
            [t for t in terms if t not in self.term_to_vector] if append_only else terms
        )
        if not terms_to_encode:
            return

        embeddings = self.embedder.encode(
            terms_to_encode,
            convert_to_tensor=True,
            normalize_embeddings=False,
            batch_size=256,
            show_progress_bar=False,
        )
        for term, embedding in zip(terms_to_encode, embeddings):
            self.term_to_vector[term] = embedding.detach().to(self.device)

    def _pairs_as_tensors(
        self, pairs: List[Tuple[str, str]]
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Convert string pairs into aligned embedding tensors on the correct device.

        Args:
            pairs: List of (parent, child) term strings.

        Returns:
            Tuple `(child_tensor, parent_tensor)` where each tensor has shape
            `(batch, embedding_dim)` and is located on `self.device`.

        Notes:
            This function assumes that all terms in `pairs` are present in
            `self.term_to_vector`. Use `_ensure_term_embeddings` beforehand.
        """
        # child embeddings tensor of shape (batch, dim)
        child_tensor = torch.stack(
            [self.term_to_vector[child] for (_, child) in pairs], dim=0
        ).to(self.device)
        # parent embeddings tensor of shape (batch, dim)
        parent_tensor = torch.stack(
            [self.term_to_vector[parent] for (parent, _) in pairs], dim=0
        ).to(self.device)
        return child_tensor, parent_tensor

    def _train_cross_attn_head(
        self,
        positive_pairs: List[Tuple[str, str]],
        negative_pairs: List[Tuple[str, str]],
    ) -> None:
        """Train the cross-attention head with BCE loss on labeled pairs.

        The dataset is a concatenation of positives (label 1) and sampled
        negatives (label 0). The head is optimized with AdamW.

        Args:
            positive_pairs: List of ground-truth (parent, child) edges.
            negative_pairs: List of sampled non-edges.

        Raises:
            RuntimeError: If the head has not been initialized (call `load()`).
        """
        if self.cross_attn_head is None:
            raise RuntimeError("Head not initialized. Call load().")

        self.cross_attn_head.train()
        optimizer = torch.optim.AdamW(
            self.cross_attn_head.parameters(),
            lr=self.learning_rate,
            weight_decay=self.weight_decay,
        )

        # Build a simple supervised dataset: 1 for positive, 0 for negative
        labeled_pairs: List[Tuple[int, Tuple[str, str]]] = [
            (1, pc) for pc in positive_pairs
        ] + [(0, nc) for nc in negative_pairs]
        random.shuffle(labeled_pairs)

        def iterate_minibatches(
            items: List[Tuple[int, Tuple[str, str]]], batch_size: int
        ):
            """Yield contiguous minibatches of size `batch_size` from `items`."""
            for start in range(0, len(items), batch_size):
                yield items[start : start + batch_size]

        for epoch in range(self.num_epochs):
            epoch_loss_sum = 0.0
            for minibatch in iterate_minibatches(labeled_pairs, self.batch_size):
                labels = torch.tensor(
                    [y for y, _ in minibatch], dtype=torch.float32, device=self.device
                )
                string_pairs = [pc for _, pc in minibatch]
                child_tensor, parent_tensor = self._pairs_as_tensors(string_pairs)

                probs = self.cross_attn_head(child_tensor, parent_tensor)
                loss = F.binary_cross_entropy(probs, labels)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                epoch_loss_sum += float(loss.item()) * len(minibatch)

    def _score_parent_child_pairs(self, pairs: List[Tuple[str, str]]) -> List[float]:
        """Compute probability scores for (parent, child) pairs.

        Args:
            pairs: List of candidate (parent, child) edges to score.

        Returns:
            List of floats in [0, 1] corresponding to the input order.

        Raises:
            RuntimeError: If the head has not been initialized (call `load()`).
        """
        if self.cross_attn_head is None:
            raise RuntimeError("Head not initialized. Call load().")

        self.cross_attn_head.eval()
        scores: List[float] = []
        with torch.no_grad():
            for start in range(0, len(pairs), self.batch_size):
                chunk = pairs[start : start + self.batch_size]
                child_tensor, parent_tensor = self._pairs_as_tensors(chunk)
                prob = self.cross_attn_head(child_tensor, parent_tensor)
                scores.extend(prob.detach().cpu().tolist())
        return scores

    def _extract_parent_child_pairs_and_terms(
        self, data: Any
    ) -> Tuple[List[Tuple[str, str]], List[str]]:
        """Extract (parent, child) edges and the set of unique terms from an ontology-like object.

        The function expects `data.type_taxonomies.taxonomies` to be an iterable
        of objects with `.parent` and `.child` string-like attributes.

        Args:
            data: Ontology-like container.

        Returns:
            A tuple `(pairs, terms)` where:
                - `pairs` is a list of (parent, child) strings,
                - `terms` is a sorted list of unique term strings (parents ∪ children).
        """
        parent_child_pairs: List[Tuple[str, str]] = []
        unique_terms = set()
        for edge in getattr(data, "type_taxonomies").taxonomies:
            parent, child = str(edge.parent), str(edge.child)
            parent_child_pairs.append((parent, child))
            unique_terms.add(parent)
            unique_terms.add(child)
        return parent_child_pairs, sorted(unique_terms)

    def _sample_negative_pairs(
        self,
        positive_pairs: List[Tuple[str, str]],
        terms: List[str],
        ratio: float = 1.0,
        seed: int = 42,
    ) -> List[Tuple[str, str]]:
        """Sample random negative (parent, child) pairs not present in positives.

        Sampling is uniform over the Cartesian product of `terms` excluding
        (x, x) self-pairs and any pair found in `positive_pairs`.

        Args:
            positive_pairs: Known positive edges to exclude.
            terms: Candidate vocabulary (parents ∪ children).
            ratio: Number of negatives per positive to draw.
            seed: RNG seed used for reproducible sampling.

        Returns:
            A list of sampled negative pairs of approximate length
            `int(len(positive_pairs) * ratio)`.
        """
        random.seed(seed)
        term_list = list(terms)
        positive_set = set(positive_pairs)
        negatives: List[Tuple[str, str]] = []
        target_negative_count = int(len(positive_pairs) * ratio)
        while len(negatives) < target_negative_count:
            parent = random.choice(term_list)
            child = random.choice(term_list)
            if parent == child:
                continue
            candidate = (parent, child)
            if candidate in positive_set:
                continue
            negatives.append(candidate)
        return negatives
