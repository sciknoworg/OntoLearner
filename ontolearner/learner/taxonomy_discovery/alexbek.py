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
import json
import math
import os
import random
from datetime import datetime
import torch
import torch.nn as nn
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from torch.cuda.amp import GradScaler

from ...base import AutoLearner


class RMSNorm(nn.Module):
    """Root Mean Square normalization with learnable scale."""
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        rms_inv = torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)
        return self.weight * (x * rms_inv)

class CrossAttentionHead(nn.Module):
    """Efficient multi-head cross-attention scorer for parent-child pairs."""
    def __init__(self, hidden_size: int, num_heads: int = 8, rms_norm_eps: float = 1e-6, dropout: float = 0.1):
        super().__init__()
        assert hidden_size % num_heads == 0, "hidden_size must be divisible by num_heads"
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.dim_per_head = hidden_size // num_heads

        self.query_projection = nn.Linear(hidden_size, hidden_size, bias=False)
        self.key_projection = nn.Linear(hidden_size, hidden_size, bias=False)

        self.query_norm = RMSNorm(hidden_size, eps=rms_norm_eps)
        self.key_norm = RMSNorm(hidden_size, eps=rms_norm_eps)

        self.dropout = nn.Dropout(dropout)

        nn.init.xavier_uniform_(self.query_projection.weight)
        nn.init.xavier_uniform_(self.key_projection.weight)

    def forward(self, child_embeddings: torch.Tensor, parent_embeddings: torch.Tensor) -> torch.Tensor:
        """
        Score (child, parent) pairs efficiently.

        Args:
            child_embeddings: (batch_child, hidden_size) or (1, n_terms, hidden_size) for broadcasting
            parent_embeddings: (batch_parent, hidden_size) or (1, n_terms, hidden_size) for broadcasting

        Returns:
            scores: (batch_child, batch_parent) if both are 2D, or appropriate broadcast shape
        """
        # Handle 2D input (standard batch processing)
        if child_embeddings.dim() == 2 and parent_embeddings.dim() == 2:
            batch_size = child_embeddings.shape[0]
            queries = self.query_norm(self.query_projection(child_embeddings))
            keys = self.key_norm(self.key_projection(parent_embeddings))

            queries = self.dropout(queries)
            keys = self.dropout(keys)

            queries = queries.view(batch_size, self.num_heads, self.dim_per_head)
            keys = keys.view(batch_size, self.num_heads, self.dim_per_head)

            per_head_scores = (queries * keys).sum(-1) / math.sqrt(self.dim_per_head)
            mean_score = per_head_scores.mean(-1)
            return torch.sigmoid(mean_score)

        # Handle 3D input for efficient matrix computation
        elif child_embeddings.dim() == 3 and parent_embeddings.dim() == 3:
            n_child = child_embeddings.shape[1]
            n_parent = parent_embeddings.shape[1]

            queries = self.query_norm(self.query_projection(child_embeddings))
            keys = self.key_norm(self.key_projection(parent_embeddings))

            queries = self.dropout(queries)
            keys = self.dropout(keys)

            queries = queries.view(1, n_child, self.num_heads, self.dim_per_head)
            keys = keys.view(1, n_parent, self.num_heads, self.dim_per_head)

            queries = queries.squeeze(0).transpose(1, 2)
            keys = keys.squeeze(0).transpose(1, 2)

            per_head_scores = torch.einsum('chd,phd->cph', queries, keys) / math.sqrt(self.dim_per_head)
            mean_score = per_head_scores.mean(-1)
            return torch.sigmoid(mean_score)


class AlexbekCrossAttnLearner(AutoLearner):
    """
    Cross-Attention Taxonomy Learner - faithful reproduction of Alexbek's approach.

    This implementation follows the original paper's methodology:
    - Computes full NxN pairwise scores for all term pairs
    - Uses threshold-based prediction (0.5 default, or F1-optimized on validation)
    - No candidate pre-filtering (can be optionally enabled for large taxonomies)
    """
    def __init__(
            self,
            *,
            embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
            device: str = "cuda" if torch.cuda.is_available() else "cpu",
            num_heads: int = 8,
            dropout: float = 0.1,
            lr: float = 1e-4,
            weight_decay: float = 0.01,
            num_epochs: int = 10,
            batch_size: int = 256,
            inference_batch_size: int = 512,
            neg_ratio: float = 1.0,
            top_k_candidates: Optional[int] = None,  # None = original behavior (all pairs)
            output_dir: str = "./results/",
            seed: int = 42,
            cache_embeddings: bool = True,
            use_lr_scheduler: bool = True,
            warmup_epochs: int = 1,
            gradient_clip: float = 1.0,
            use_amp: bool = True,
            hard_negative_ratio: float = 0.0,  # 0.0 = original (all random negatives)
            patience: int = 3,
            validation_split: float = 0.1,
            normalize_embeddings: bool = True,
            prediction_threshold: float = 0.5,  # Original uses 0.5 or F1-optimized
            optimize_threshold_on_val: bool = True,  # Set True to replicate "Validation-F1" approach
            **kwargs: Any,
    ):
        super().__init__(**kwargs)

        self.embedding_model_id = embedding_model
        self.requested_device = device
        self.num_heads = num_heads
        self.dropout = dropout
        self.learning_rate = lr
        self.weight_decay = weight_decay
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.inference_batch_size = inference_batch_size
        self.negative_ratio = neg_ratio
        self.top_k_candidates = top_k_candidates
        self.output_dir = output_dir
        self.seed = seed
        self.cache_embeddings = cache_embeddings
        self.use_lr_scheduler = use_lr_scheduler
        self.warmup_epochs = warmup_epochs
        self.gradient_clip = gradient_clip
        self.use_amp = use_amp and torch.cuda.is_available()
        self.hard_negative_ratio = hard_negative_ratio
        self.patience = patience
        self.validation_split = validation_split
        self.normalize_embeddings = normalize_embeddings
        self.prediction_threshold = prediction_threshold
        self.optimize_threshold_on_val = optimize_threshold_on_val

        if torch.cuda.is_available() or self.requested_device == "cpu":
            self.device = torch.device(self.requested_device)
        else:
            self.device = torch.device("cpu")

        self.embedder: Optional[SentenceTransformer] = None
        self.cross_attn_head: Optional[CrossAttentionHead] = None
        self.embedding_dim: Optional[int] = None
        self.term_to_vector: Dict[str, torch.Tensor] = {}
        self.scaler: Optional[GradScaler] = GradScaler() if self.use_amp else None
        self.best_threshold: float = self.prediction_threshold

        os.makedirs(self.output_dir, exist_ok=True)
        random.seed(self.seed)
        torch.manual_seed(self.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.seed)

    def load(self, **kwargs: Any):
        """Load the sentence embedding model and initialize the cross-attention head."""
        model_id = kwargs.get("embedding_model", self.embedding_model_id)
        self.embedder = SentenceTransformer(model_id, trust_remote_code=True, device=str(self.device))

        probe_embedding = self.embedder.encode(["_dim_probe_"],
                                               convert_to_tensor=True,
                                               normalize_embeddings=False)
        self.embedding_dim = int(probe_embedding.shape[-1])

        self.cross_attn_head = CrossAttentionHead(
            hidden_size=self.embedding_dim,
            num_heads=self.num_heads,
            dropout=self.dropout
        ).to(self.device)

    def save_model(self, path: str) -> None:
        """Save the trained cross-attention head."""
        if self.cross_attn_head is None:
            raise RuntimeError("No model to save")

        checkpoint = {
            'model_state_dict': self.cross_attn_head.state_dict(),
            'embedding_dim': self.embedding_dim,
            'num_heads': self.num_heads,
            'dropout': self.dropout,
            'embedding_model_id': self.embedding_model_id,
            'best_threshold': self.best_threshold,
        }

        torch.save(checkpoint, path)
        print(f"Model saved to {path}")

    def load_model(self, path: str) -> None:
        """Load a trained cross-attention head."""
        checkpoint = torch.load(path, map_location=self.device)

        self.embedding_dim = checkpoint['embedding_dim']
        self.num_heads = checkpoint['num_heads']
        self.dropout = checkpoint.get('dropout', 0.1)
        self.embedding_model_id = checkpoint.get('embedding_model_id', self.embedding_model_id)
        self.best_threshold = checkpoint.get('best_threshold', 0.5)

        # Load embedder if not already loaded
        if self.embedder is None:
            self.embedder = SentenceTransformer(
                self.embedding_model_id,
                trust_remote_code=True,
                device=str(self.device)
            )

        self.cross_attn_head = CrossAttentionHead(
            hidden_size=self.embedding_dim,
            num_heads=self.num_heads,
            dropout=self.dropout
        ).to(self.device)

        self.cross_attn_head.load_state_dict(checkpoint['model_state_dict'])
        print(f"Model loaded from {path} (threshold: {self.best_threshold:.3f})")

    def save_config(self, path: str) -> None:
        """Save hyperparameters to JSON."""
        config = {
            'embedding_model': self.embedding_model_id,
            'num_heads': self.num_heads,
            'dropout': self.dropout,
            'lr': self.learning_rate,
            'weight_decay': self.weight_decay,
            'num_epochs': self.num_epochs,
            'batch_size': self.batch_size,
            'inference_batch_size': self.inference_batch_size,
            'negative_ratio': self.negative_ratio,
            'top_k_candidates': self.top_k_candidates,
            'use_lr_scheduler': self.use_lr_scheduler,
            'warmup_epochs': self.warmup_epochs,
            'gradient_clip': self.gradient_clip,
            'use_amp': self.use_amp,
            'hard_negative_ratio': self.hard_negative_ratio,
            'patience': self.patience,
            'validation_split': self.validation_split,
            'normalize_embeddings': self.normalize_embeddings,
            'prediction_threshold': self.prediction_threshold,
            'optimize_threshold_on_val': self.optimize_threshold_on_val,
            'best_threshold': self.best_threshold,
            'seed': self.seed,
        }

        with open(path, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"Configuration saved to {path}")

    @classmethod
    def from_config(cls, config_path: str, **override_kwargs):
        """Load from configuration file."""
        with open(config_path, 'r') as f:
            config = json.load(f)

        config.update(override_kwargs)
        return cls(**config)

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        Train or infer taxonomy edges.

        Original behavior: Scores ALL possible pairs and applies threshold.
        Optional optimization: Can pre-filter to top-k candidates if top_k_candidates is set.
        """
        if self.embedder is None or self.cross_attn_head is None:
            self.load()

        if not test:
            # Training mode
            positive_pairs, unique_terms = self._extract_parent_child_pairs_and_terms(data, test=test)
            self._ensure_term_embeddings(unique_terms)
            negative_pairs = self._sample_negative_pairs(positive_pairs,
                                                         unique_terms,
                                                         ratio=self.negative_ratio,
                                                         seed=self.seed)
            self._train_cross_attn_head(positive_pairs, negative_pairs)

            # Save model and config after training
            model_path = os.path.join(self.output_dir, "best_model.pt")
            config_path = os.path.join(self.output_dir, "config.json")
            self.save_model(model_path)
            self.save_config(config_path)

            return None
        else:
            # Inference mode
            candidate_pairs, unique_terms = self._extract_parent_child_pairs_and_terms(data, test=test)
            self._ensure_term_embeddings(unique_terms, append_only=True)

            # Original approach: score all pairs
            if self.top_k_candidates is None:
                print(f"ORIGINAL MODE: Computing full {len(unique_terms)}x{len(unique_terms)} probability matrix...")
                probabilities = self._score_all_pairs_efficient(unique_terms)

                # Apply threshold to get predictions
                print(f"Applying threshold {self.best_threshold:.3f} to extract predictions...")
                binary_matrix = (probabilities >= self.best_threshold).cpu().numpy()

                # Find indices where prediction is 1
                child_indices, parent_indices = binary_matrix.nonzero()

                # Get corresponding probabilities
                probs = probabilities[child_indices, parent_indices].cpu().numpy()

                # Build predictions
                predictions = [
                    {
                        "parent": unique_terms[parent_idx],
                        "child": unique_terms[child_idx],
                        "score": float(prob),
                        "label": 1,
                    }
                    for child_idx, parent_idx, prob in zip(child_indices, parent_indices, probs)
                    if child_idx != parent_idx  # Exclude self-loops
                ]

                print(
                    f"Found {len(predictions)} positive predictions from {len(unique_terms) ** 2 - len(unique_terms)} possible pairs")

            else:
                # Optional optimization: pre-filter candidates
                print(f"OPTIMIZATION MODE: Filtering to top-{self.top_k_candidates} candidates per term...")
                print("WARNING: This is NOT the original Alexbek approach but an efficiency optimization.")
                candidate_pairs = self._filter_top_k_candidates(unique_terms, self.top_k_candidates)
                print(f"Reduced to {len(candidate_pairs)} candidate pairs")

                # Score filtered candidates
                print("Scoring filtered candidate pairs...")
                probabilities = self._score_specific_pairs(candidate_pairs)

                # Apply threshold
                predictions = [
                    {
                        "parent": parent,
                        "child": child,
                        "score": float(prob),
                        "label": 1,
                    }
                    for (parent, child), prob in zip(candidate_pairs, probabilities)
                    if prob >= self.best_threshold and parent != child
                ]

                print(f"Found {len(predictions)} positive predictions from {len(candidate_pairs)} candidate pairs")

            return predictions

    def _ensure_term_embeddings(self, terms: List[str], append_only: bool = False) -> None:
        """Encode terms efficiently with batching."""
        if self.embedder is None:
            raise RuntimeError("Call load() before building term embeddings")

        terms_to_encode = ([t for t in terms if t not in self.term_to_vector] if append_only else terms)
        if not terms_to_encode:
            return

        # Batch encode terms with normalization
        embeddings = self.embedder.encode(
            terms_to_encode,
            convert_to_tensor=True,
            normalize_embeddings=self.normalize_embeddings,
            batch_size=self.inference_batch_size,
            show_progress_bar=True,
        )

        for term, embedding in zip(terms_to_encode, embeddings):
            self.term_to_vector[term] = embedding.to(self.device)

    def _score_specific_pairs(self, pairs: List[Tuple[str, str]]) -> List[float]:
        """
        Score only specific (parent, child) pairs efficiently in batches.

        Args:
            pairs: List of (parent, child) tuples to score

        Returns:
            List of probability scores corresponding to input pairs
        """
        if self.cross_attn_head is None:
            raise RuntimeError("Head not initialized. Call load().")

        self.cross_attn_head.eval()
        scores: List[float] = []

        with torch.no_grad():
            for start in tqdm(range(0, len(pairs), self.inference_batch_size), desc="Scoring pairs"):
                chunk = pairs[start: start + self.inference_batch_size]
                child_tensor, parent_tensor = self._pairs_as_tensors(chunk)
                prob = self.cross_attn_head(child_tensor, parent_tensor)
                scores.extend(prob.detach().cpu().tolist())

        return scores

    def _score_all_pairs_efficient(self, terms: List[str]) -> torch.Tensor:
        """
        Efficiently score all pairs using matrix operations (ORIGINAL ALEXBEK APPROACH).

        Returns:
            scores: (n_terms, n_terms) matrix where scores[i,j] = P(terms[j] is parent of terms[i])
        """
        if self.cross_attn_head is None:
            raise RuntimeError("Head not initialized. Call load().")

        self.cross_attn_head.eval()
        n_terms = len(terms)

        # Stack all embeddings
        all_embeddings = torch.stack([self.term_to_vector[t] for t in terms], dim=0)

        # Compute scores in chunks to manage memory
        scores_matrix = torch.zeros((n_terms, n_terms), device=self.device)

        with torch.no_grad():
            chunk_size = self.inference_batch_size

            progress_bar = tqdm(
                range(0, n_terms, chunk_size),
                desc="Scoring all pairs",
                total=(n_terms + chunk_size - 1) // chunk_size
            )

            for i in progress_bar:
                end_i = min(i + chunk_size, n_terms)
                child_chunk = all_embeddings[i:end_i]

                # Score against all parents at once
                child_broadcast = child_chunk.unsqueeze(0)
                parent_broadcast = all_embeddings.unsqueeze(0)

                chunk_scores = self.cross_attn_head(child_broadcast, parent_broadcast)
                scores_matrix[i:end_i, :] = chunk_scores

                progress_bar.set_postfix({
                    'completed': f'{end_i}/{n_terms}',
                    'pairs_scored': f'{end_i * n_terms:,}'
                })

        return scores_matrix

    def _pairs_as_tensors(self, pairs: List[Tuple[str, str]]) -> Tuple[torch.Tensor, torch.Tensor]:
        """Convert string pairs into aligned embedding tensors."""
        child_tensor = torch.stack([self.term_to_vector[child] for (_, child) in pairs], dim=0)
        parent_tensor = torch.stack([self.term_to_vector[parent] for (parent, _) in pairs], dim=0)
        return child_tensor, parent_tensor

    def _optimize_threshold_on_validation(self, val_pairs: List[Tuple[int, Tuple[str, str]]]) -> float:
        """
        Find optimal threshold that maximizes F1 on validation set.
        This replicates the "Validation-F1" approach from the paper.
        """
        if not val_pairs:
            return self.prediction_threshold

        print("Optimizing prediction threshold on validation set...")
        self.cross_attn_head.eval()

        # Get validation labels and scores
        val_labels = []
        val_scores = []

        with torch.no_grad():
            for label, (parent, child) in val_pairs:
                val_labels.append(label)
                child_tensor = self.term_to_vector[child].unsqueeze(0)
                parent_tensor = self.term_to_vector[parent].unsqueeze(0)
                score = self.cross_attn_head(child_tensor, parent_tensor).item()
                val_scores.append(score)

        val_labels = torch.tensor(val_labels)
        val_scores = torch.tensor(val_scores)

        # Try different thresholds
        best_f1 = 0.0
        best_threshold = 0.5

        for threshold in torch.linspace(0.1, 0.9, 50):
            preds = (val_scores >= threshold).long()

            tp = ((preds == 1) & (val_labels == 1)).sum().item()
            fp = ((preds == 1) & (val_labels == 0)).sum().item()
            fn = ((preds == 0) & (val_labels == 1)).sum().item()

            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

            if f1 > best_f1:
                best_f1 = f1
                best_threshold = threshold.item()

        print(f"Optimal threshold: {best_threshold:.3f} (F1: {best_f1:.4f})")
        return best_threshold

    def _train_cross_attn_head(self,
                               positive_pairs: List[Tuple[str, str]],
                               negative_pairs: List[Tuple[str, str]]) -> None:
        """Train the cross-attention head with BCE loss, validation, and early stopping."""
        if self.cross_attn_head is None:
            raise RuntimeError("Head not initialized. Call load().")

        self.cross_attn_head.train()
        optimizer = torch.optim.AdamW(
            self.cross_attn_head.parameters(),
            lr=self.learning_rate,
            weight_decay=self.weight_decay,
        )

        # Prepare labeled pairs and split into train/val
        labeled_pairs: List[Tuple[int, Tuple[str, str]]] = [(1, pc) for pc in positive_pairs] + \
                                                           [(0, nc) for nc in negative_pairs]
        random.shuffle(labeled_pairs)

        split_idx = int((1 - self.validation_split) * len(labeled_pairs))
        train_pairs = labeled_pairs[:split_idx]
        val_pairs = labeled_pairs[split_idx:]

        print(f"Training samples: {len(train_pairs)}, Validation samples: {len(val_pairs)}")

        # Setup learning rate scheduler
        scheduler = None
        if self.use_lr_scheduler:
            total_steps = (len(train_pairs) // self.batch_size + 1) * self.num_epochs
            warmup_steps = (len(train_pairs) // self.batch_size + 1) * self.warmup_epochs

            def lr_lambda(step):
                if step < warmup_steps:
                    return (step + 1) / (warmup_steps + 1)
                else:
                    progress = (step - warmup_steps) / (total_steps - warmup_steps)
                    return max(0.1, 0.5 * (1 + math.cos(math.pi * progress)))

            scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=lr_lambda)

        def iterate_minibatches(items: List[Tuple[int, Tuple[str, str]]], batch_size: int):
            for start in range(0, len(items), batch_size):
                yield items[start: start + batch_size]

        # Training loop with early stopping
        best_val_loss = float('inf')
        best_model_state = None
        patience_counter = 0
        metrics_history = []
        global_step = 0

        for epoch in tqdm(range(self.num_epochs), desc="Training"):
            # Training phase
            self.cross_attn_head.train()
            epoch_loss_sum = 0.0

            for minibatch in iterate_minibatches(train_pairs, self.batch_size):
                labels = torch.tensor([y for y, _ in minibatch], dtype=torch.float32, device=self.device)
                string_pairs = [pc for _, pc in minibatch]
                child_tensor, parent_tensor = self._pairs_as_tensors(string_pairs)

                optimizer.zero_grad()

                # Mixed precision training
                if self.use_amp:
                    probs = self.cross_attn_head(child_tensor, parent_tensor)
                    loss = F.binary_cross_entropy(probs, labels)

                    self.scaler.scale(loss).backward()

                    if self.gradient_clip > 0:
                        self.scaler.unscale_(optimizer)
                        torch.nn.utils.clip_grad_norm_(
                            self.cross_attn_head.parameters(),
                            self.gradient_clip
                        )

                    self.scaler.step(optimizer)
                    self.scaler.update()
                else:
                    probs = self.cross_attn_head(child_tensor, parent_tensor)
                    loss = F.binary_cross_entropy(probs, labels)

                    loss.backward()

                    if self.gradient_clip > 0:
                        torch.nn.utils.clip_grad_norm_(
                            self.cross_attn_head.parameters(),
                            self.gradient_clip
                        )

                    optimizer.step()

                if scheduler is not None:
                    scheduler.step()
                    global_step += 1

                epoch_loss_sum += float(loss.item()) * len(minibatch)

            avg_train_loss = epoch_loss_sum / len(train_pairs)

            # Validation phase
            self.cross_attn_head.eval()
            val_loss_sum = 0.0

            with torch.no_grad():
                for minibatch in iterate_minibatches(val_pairs, self.batch_size):
                    labels = torch.tensor([y for y, _ in minibatch], dtype=torch.float32, device=self.device)
                    string_pairs = [pc for _, pc in minibatch]
                    child_tensor, parent_tensor = self._pairs_as_tensors(string_pairs)

                    probs = self.cross_attn_head(child_tensor, parent_tensor)
                    loss = F.binary_cross_entropy(probs, labels)
                    val_loss_sum += float(loss.item()) * len(minibatch)

            avg_val_loss = val_loss_sum / len(val_pairs)

            # Track metrics
            current_lr = optimizer.param_groups[0]['lr']
            metrics = {
                'epoch': epoch + 1,
                'train_loss': avg_train_loss,
                'val_loss': avg_val_loss,
                'learning_rate': current_lr,
                'timestamp': datetime.now().isoformat()
            }
            metrics_history.append(metrics)

            # Save best model
            if avg_val_loss < best_val_loss:
                best_val_loss = avg_val_loss
                best_model_state = self.cross_attn_head.state_dict()
                patience_counter = 0
                print(f"Epoch {epoch + 1}/{self.num_epochs} | "
                      f"Train Loss: {avg_train_loss:.4f} | "
                      f"Val Loss: {avg_val_loss:.4f} ⭐ (Best) | "
                      f"LR: {current_lr:.6f}")
            else:
                patience_counter += 1
                print(f"Epoch {epoch + 1}/{self.num_epochs} | "
                      f"Train Loss: {avg_train_loss:.4f} | "
                      f"Val Loss: {avg_val_loss:.4f} | "
                      f"LR: {current_lr:.6f} | "
                      f"Patience: {patience_counter}/{self.patience}")

            # Early stopping
            if patience_counter >= self.patience:
                print(f"Early stopping triggered at epoch {epoch + 1}")
                break

        # Restore best model
        if best_model_state is not None:
            self.cross_attn_head.load_state_dict(best_model_state)
            print(f"Restored best model with validation loss: {best_val_loss:.4f}")

        # Optimize threshold on validation set if requested
        if self.optimize_threshold_on_val and val_pairs:
            self.best_threshold = self._optimize_threshold_on_validation(val_pairs)
        else:
            self.best_threshold = self.prediction_threshold

        # Save training metrics
        metrics_path = os.path.join(self.output_dir, 'training_metrics.json')
        with open(metrics_path, 'w') as f:
            json.dump(metrics_history, f, indent=2)

    def _filter_top_k_candidates(self, terms: List[str], top_k: int) -> List[Tuple[str, str]]:
        """
        OPTIONAL OPTIMIZATION (NOT in original Alexbek paper):
        Filter candidate pairs to only include top-k most similar terms based on cosine similarity.
        Memory-efficient chunked implementation.

        Args:
            terms: List of unique terms
            top_k: Number of most similar candidates to keep per term

        Returns:
            List of (parent, child) candidate pairs
        """
        n_terms = len(terms)

        # Stack all embeddings and normalize for cosine similarity
        all_embeddings = torch.stack([self.term_to_vector[t] for t in terms], dim=0)
        normalized_embeddings = F.normalize(all_embeddings, p=2, dim=1)

        candidate_pairs = []

        # Process in chunks to avoid OOM for large taxonomies
        chunk_size = min(1000, n_terms)

        print("Finding top-k similar terms for each term...")
        for child_start in tqdm(range(0, n_terms, chunk_size), desc="Filtering candidates"):
            child_end = min(child_start + chunk_size, n_terms)
            child_chunk = normalized_embeddings[child_start:child_end]

            # Compute similarities for this chunk
            similarities = torch.mm(child_chunk, normalized_embeddings.t())

            # Get top-k+1 for each child in chunk (to exclude self if needed)
            top_k_values, top_k_indices = torch.topk(similarities, min(top_k + 1, n_terms), dim=1)

            # Add pairs (excluding self-loops)
            for local_idx, child_idx in enumerate(range(child_start, child_end)):
                for parent_idx in top_k_indices[local_idx].cpu().tolist():
                    if parent_idx != child_idx:
                        candidate_pairs.append((terms[parent_idx], terms[child_idx]))

        return candidate_pairs

    def _extract_parent_child_pairs_and_terms(self, data: Any, test: bool) -> Tuple[List[Tuple[str, str]], List[str]]:
        """Extract (parent, child) edges and unique terms from ontology data."""
        parent_child_pairs: List[Tuple[str, str]] = []
        unique_terms = set()

        for edge in getattr(data, "type_taxonomies").taxonomies:
            parent, child = str(edge.parent), str(edge.child)
            if not test:
                parent_child_pairs.append((parent, child))
            unique_terms.add(parent)
            unique_terms.add(child)

        if test:
            # In test mode, return empty pairs - will score all pairs in _taxonomy_discovery
            pass

        return parent_child_pairs, sorted(unique_terms)

    def _sample_negative_pairs(
            self,
            positive_pairs: List[Tuple[str, str]],
            terms: List[str],
            ratio: float = 1.0,
            seed: int = 42,
    ) -> List[Tuple[str, str]]:
        """
        Sample negative pairs.

        Original approach: All random negatives (hard_negative_ratio=0.0)
        Optional: Mix of hard negatives and random negatives (hard_negative_ratio>0.0)
        """
        random.seed(seed)
        term_list = list(terms)
        positive_set = set(positive_pairs)

        target_count = int(len(positive_pairs) * ratio)
        hard_count = int(target_count * self.hard_negative_ratio) if self.hard_negative_ratio > 0 else 0
        random_count = target_count - hard_count

        negatives = []

        # Hard negatives: pairs with high embedding similarity but not in taxonomy
        if hard_count > 0:
            print(f"Sampling {hard_count} hard negatives based on embedding similarity...")
            all_embeddings = torch.stack([self.term_to_vector[t] for t in term_list])
            normalized_embeddings = F.normalize(all_embeddings, p=2, dim=1)
            similarity_matrix = torch.mm(normalized_embeddings, normalized_embeddings.t())

            # For each term, get candidates sorted by similarity
            for i in range(len(term_list)):
                if len(negatives) >= hard_count:
                    break

                similarities = similarity_matrix[i]
                sorted_indices = torch.argsort(similarities, descending=True)

                for j in sorted_indices:
                    j_idx = j.item()
                    if i == j_idx:
                        continue
                    candidate = (term_list[j_idx], term_list[i])
                    if candidate not in positive_set and candidate not in negatives:
                        negatives.append(candidate)
                        if len(negatives) >= hard_count:
                            break
        # Random negatives (ORIGINAL ALEXBEK APPROACH)
        if random_count > 0:
            print(f"Sampling {random_count} random negatives...")
            max_attempts = random_count * 10
            attempts = 0

            while len(negatives) < target_count and attempts < max_attempts:
                parent = random.choice(term_list)
                child = random.choice(term_list)
                attempts += 1

                if parent == child:
                    continue
                candidate = (parent, child)
                if candidate not in positive_set and candidate not in negatives:
                    negatives.append(candidate)
        if hard_count > 0:
            print(f"Sampled {len(negatives)} negative pairs ({hard_count} hard, {len(negatives) - hard_count} random)")
        else:
            print(f"Sampled {len(negatives)} random negative pairs (original approach)")
        return negatives
