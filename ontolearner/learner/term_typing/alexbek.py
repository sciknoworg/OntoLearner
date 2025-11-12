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

"""Learners for supervised and retrieval-augmented *term typing*.

This module implements two learners:

- **AlexbekRFLearner** (retriever/classifier):
  Encodes terms with a Hugging Face encoder, optionally augments with simple
  graph features, and trains a One-vs-Rest RandomForest for multi-label typing.

- **AlexbekRAGLearner** (retrieval-augmented generation):
  Builds an in-memory example index with sentence embeddings, retrieves
  nearest examples for each query term, then prompts an instruction-tuned
  causal LLM to produce types, parsing the JSON response.

Both learners conform to the `AutoLearner` / `AutoRetriever` APIs used in
the outer pipeline.
"""

import gc
import json
import re
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.nn.functional as F
import networkx as nx
from tqdm import tqdm
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier

from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer

from ...base import AutoLearner, AutoRetriever


class AlexbekRFLearner(AutoRetriever):
    """
    Embedding-based multi-label classifier for *term typing*.

    Pipeline
    1) Load a Hugging Face encoder (tokenizer + model).
    2) Encode input terms into sentence embeddings.
    3) Optionally augment with simple graph (co-occurrence) features.
    4) Train a One-vs-Rest RandomForest on the concatenated features.
    5) Predict multi-label types with a probability threshold (fallback to top-1).

    Implements the `AutoRetriever` interface used by the outer pipeline.
    """

    def __init__(
        self,
        device: str = "cpu",
        batch_size: int = 16,
        max_length: int = 256,
        threshold: float = 0.30,
        use_graph_features: bool = True,
        rf_kwargs: Optional[Dict[str, Any]] = None,
    ):
        """Configure the RF-based multi-label learner.

        Parameters
        device:
            Torch device spec ('cpu' or 'cuda').
        batch_size:
            Encoding mini-batch size for the transformer.
        max_length:
            Maximum input token length for the encoder tokenizer.
        threshold:
            Per-label probability threshold at prediction time.
        use_graph_features:
            If True, add simple graph features to embeddings.
        rf_kwargs:
            Optional RandomForest hyperparameters dictionary.

        """
        # Runtime / inference settings
        self.device = torch.device(device)
        self.batch_size = batch_size
        self.max_length = max_length
        self.threshold = threshold  # probability cutoff for selecting labels
        self.use_graph_features = use_graph_features

        # RandomForest hyperparameters (with sensible defaults)
        self.rf_kwargs = rf_kwargs or dict(
            n_estimators=200, max_depth=20, class_weight="balanced", random_state=42
        )

        # Filled during load/fit
        self.model_name: Optional[str] = None
        self.tokenizer: Optional[AutoTokenizer] = None
        self.embedding_model: Optional[AutoModel] = None

        # Label processing / classifier / optional graph
        self.label_binarizer = MultiLabelBinarizer()
        self.ovr_random_forest: Optional[OneVsRestClassifier] = None
        self.term_graph: Optional[nx.Graph] = None

    def load(self, model_id: str, **_: Any) -> None:
        """Load a Hugging Face encoder by model id (tokenizer + base model).

        Parameters
        model_id:
            HF model identifier or local path for an encoder backbone.

        Side Effects
        - Sets `self.model_name`, `self.tokenizer`, `self.embedding_model`.
        - Puts the model in eval mode and moves it to `self.device`.
        """
        self.model_name = model_id
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.embedding_model = AutoModel.from_pretrained(model_id)
        self.embedding_model.eval().to(self.device)

    def fit(self, data: Any, task: str, ontologizer: bool = True, **_: Any) -> None:
        """Train the One-vs-Rest RandomForest on term embeddings (+ optional graph features).

        Parameters
        data:
            Training payload; supported formats are routed via `_as_term_types_dicts`.
            Each example must contain at least `{"term": str, "types": List[str]}`.
        task:
            Must be `'term-typing'`.
        ontologizer:
            Unused here; accepted for API compatibility.
        **_:
            Ignored extra arguments.

        Raises
        ValueError
            If `task` is not `'term-typing'` or if no valid examples are found.
        """
        if task != "term-typing":
            raise ValueError(
                "OntologyTypeRFClassifier supports only task='term-typing'."
            )

        # Normalize incoming training data into a list of dicts: {term, types, RAG}
        training_rows = self._as_term_types_dicts(data)
        if not training_rows:
            raise ValueError(
                "No valid training examples found (need 'term' and 'types')."
            )

        # Split out terms and raw labels
        training_terms: List[str] = [row["term"] for row in training_rows]
        raw_label_lists: List[List[str]] = [row["types"] for row in training_rows]

        # Fit label binarizer to learn label space/order
        self.label_binarizer.fit(raw_label_lists)

        # Encode terms to sentence embeddings
        term_embeddings_train = self._encode(training_terms)

        # Optionally build a light-weight co-occurrence graph and extract features
        if self.use_graph_features:
            self.term_graph = self._create_term_graph(training_rows)
            graph_features_train = self._extract_graph_features(
                self.term_graph, training_terms
            )
            X_train = np.hstack([term_embeddings_train, graph_features_train])
        else:
            self.term_graph = None
            X_train = term_embeddings_train

        # Multi-label targets (multi-hot)
        Y_train = self.label_binarizer.transform(raw_label_lists)

        # One-vs-Rest RandomForest (one binary RF per label)
        self.ovr_random_forest = OneVsRestClassifier(
            RandomForestClassifier(**self.rf_kwargs)
        )
        self.ovr_random_forest.fit(X_train, Y_train)

    def predict(
        self, data: Any, task: str, ontologizer: bool = True, **_: Any
    ) -> List[Dict[str, Any]]:
        """Predict multi-label types for input terms.

        Parameters
        data:
            Evaluation payload; formats normalized by `_as_predict_terms_ids`.
        task:
            Must be `'term-typing'`.
        ontologizer:
            Unused here; accepted for API compatibility.
        **_:
            Ignored extra arguments.

        Returns
        List[Dict[str, Any]]
            A list of dictionaries with keys:
            - `id`: Original example id (if provided).
            - `term`: Input term string.
            - `types`: List of predicted label strings (selected by threshold or top-1).

        Raises
        ValueError
            If `task` is not `'term-typing'`.
        RuntimeError
            If `load()` and `fit()` have not been called.
        """
        if task != "term-typing":
            raise ValueError(
                "OntologyTypeRFClassifier supports only task='term-typing'."
            )
        if (
            self.ovr_random_forest is None
            or self.tokenizer is None
            or self.embedding_model is None
        ):
            raise RuntimeError("Call load() and fit() before predict().")

        # Normalize prediction input into parallel lists of terms and example ids
        test_terms, example_ids = self._as_predict_terms_ids(data)

        # Encode terms
        term_embeddings_test = self._encode(test_terms)

        # Match feature layout used during training
        if self.use_graph_features and self.term_graph is not None:
            graph_features_test = self._extract_graph_features(
                self.term_graph, test_terms
            )
            X_test = np.hstack([term_embeddings_test, graph_features_test])
        else:
            X_test = term_embeddings_test

        # Probabilities per label (shape: [n_samples, n_labels])
        probability_matrix = self.ovr_random_forest.predict_proba(X_test)

        predictions: List[Dict[str, Any]] = []
        label_names = self.label_binarizer.classes_
        threshold = float(self.threshold)

        # Select labels above threshold; fallback to argmax if none exceed it
        for row_index, label_probabilities in enumerate(probability_matrix):
            selected_label_indices = np.where(label_probabilities > threshold)[0]
            if len(selected_label_indices) == 0:
                selected_label_indices = [int(np.argmax(label_probabilities))]

            predicted_types = [
                label_names[label_idx] for label_idx in selected_label_indices
            ]

            predictions.append(
                {
                    "id": example_ids[row_index],
                    "term": test_terms[row_index],
                    "types": predicted_types,
                }
            )
        return predictions

    def tasks_ground_truth_former(self, data: Any, task: str) -> List[Dict[str, Any]]:
        """Normalize ground-truth into a list of {id, term, types} dicts for evaluation.

        Parameters
        data:
            Ground-truth payload; supported formats include objects exposing
            `.term_typings`, a list of dicts, or a list of tuples/lists.
        task:
            Must be `'term-typing'`.

        Returns
        List[Dict[str, Any]]
            A list of dictionaries with keys `id`, `term`, `types` (list of str).

        Raises
        ValueError
            If `task` is not `'term-typing'`.
        """
        if task != "term-typing":
            raise ValueError(
                "OntologyTypeRFClassifier supports only task='term-typing'."
            )
        return self._as_gold_id_term_types(data)

    def _encode(self, texts: List[str]) -> np.ndarray:
        """Encode a list of strings into L2-normalized sentence embeddings.

        Parameters
        texts:
            List of input texts/terms.

        Returns
        np.ndarray
            Array of shape `(len(texts), hidden_size)` with L2-normalized
            embeddings. If `texts` is empty, returns a `(0, hidden_size)` array.
        """
        assert self.tokenizer is not None and self.embedding_model is not None, (
            "Call load(model_id) first."
        )

        if not texts:
            hidden_size = getattr(
                getattr(self.embedding_model, "config", None), "hidden_size", 768
            )
            return np.zeros((0, hidden_size), dtype=np.float32)

        batch_embeddings: List[torch.Tensor] = []

        for start_idx in tqdm(range(0, len(texts), self.batch_size), desc="Embedding"):
            end_idx = start_idx + self.batch_size
            batch_texts = texts[start_idx:end_idx]

            # Tokenize and move to device
            tokenized_batch = self.tokenizer(
                batch_texts,
                padding=True,
                truncation=True,
                max_length=self.max_length,
                return_tensors="pt",
            ).to(self.device)

            # Forward pass without gradients
            with torch.no_grad():
                model_output = self.embedding_model(**tokenized_batch)

                # Prefer dedicated pooler if provided; otherwise pool by last valid token
                if (
                    hasattr(model_output, "pooler_output")
                    and model_output.pooler_output is not None
                ):
                    sentence_embeddings = model_output.pooler_output
                else:
                    sentence_embeddings = self._last_token_pool(
                        model_output.last_hidden_state,
                        tokenized_batch["attention_mask"],
                    )

                # L2-normalize embeddings for stability
                sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

            # Detach, move to CPU, collect
            batch_embeddings.append(sentence_embeddings.detach().cpu())

            # Best-effort memory cleanup (especially useful on CUDA)
            del tokenized_batch, model_output, sentence_embeddings
            if self.device.type == "cuda":
                torch.cuda.empty_cache()
            gc.collect()

        # Concatenate all batches and convert to NumPy
        return torch.cat(batch_embeddings, dim=0).numpy()

    def _last_token_pool(
        self, last_hidden_states: torch.Tensor, attention_mask: torch.Tensor
    ) -> torch.Tensor:
        """Select the last *non-padding* token embedding for each sequence.

        Parameters
        last_hidden_states:
            Tensor of shape `(batch, seq_len, hidden)`.
        attention_mask:
            Tensor of shape `(batch, seq_len)` with 1 for real tokens.

        Returns
        torch.Tensor
            Tensor of shape `(batch, hidden)` with per-sequence pooled embeddings.
        """
        last_valid_token_idx = attention_mask.sum(dim=1) - 1  # (batch,)
        batch_row_idx = torch.arange(
            last_hidden_states.size(0), device=last_hidden_states.device
        )
        return last_hidden_states[batch_row_idx, last_valid_token_idx]

    def _create_term_graph(self, training_rows: List[Dict[str, Any]]) -> nx.Graph:
        """Create a simple undirected co-occurrence graph from training rows.

        Graph Structure
        Nodes
            Terms (node attribute `'types'` is stored per term).
        Edges
            Between a term and each neighbor from its optional RAG list.
            Edge weight = number of shared types (or 0.1 if none shared).

        Parameters
        training_rows:
            Normalized rows with keys: `'term'`, `'types'`, optional `'RAG'`.

        Returns
        networkx.Graph
            The constructed undirected graph.
        """
        graph = nx.Graph()

        for row in training_rows:
            term = row["term"]
            term_types = row.get("types", [])
            graph.add_node(term, types=term_types)

            # RAG may be a list of neighbor dicts like {"term": ..., "types": [...]}
            for neighbor in row.get("RAG", []) or []:
                neighbor_term = neighbor.get("term")
                neighbor_types = neighbor.get("types", [])

                # Shared-type-based edge weight (weak edge if no overlap)
                shared_types = set(term_types).intersection(set(neighbor_types))
                edge_weight = float(len(shared_types)) if shared_types else 0.1

                graph.add_edge(term, neighbor_term, weight=edge_weight)

        return graph

    def _extract_graph_features(
        self, term_graph: nx.Graph, terms: List[str]
    ) -> np.ndarray:
        """Compute simple per-term graph features.

        Feature Vector
        For each term we compute a 4-dim vector:
        `[degree, clustering_coefficient, degree_centrality, pagerank_score]`

        Parameters
        term_graph:
            Graph built over training terms.
        terms:
            List of term strings to extract features for.

        Returns
        np.ndarray
            Array of shape `(len(terms), 4)` (dtype float32).
        """
        if len(term_graph):
            degree_centrality = nx.degree_centrality(term_graph)
            pagerank_scores = nx.pagerank(term_graph)
        else:
            degree_centrality, pagerank_scores = {}, {}

        feature_rows: List[List[float]] = []
        for term in terms:
            if term in term_graph:
                feature_rows.append(
                    [
                        float(term_graph.degree(term)),
                        float(nx.clustering(term_graph, term)),
                        float(degree_centrality.get(term, 0.0)),
                        float(pagerank_scores.get(term, 0.0)),
                    ]
                )
            else:
                feature_rows.append([0.0, 0.0, 0.0, 0.0])

        return np.asarray(feature_rows, dtype=np.float32)

    def _as_term_types_dicts(self, data: Any) -> List[Dict[str, Any]]:
        """Normalize diverse training data formats to a list of dicts: {term, types, RAG}.

        Supported Inputs
        - Object with attribute `.term_typings` (iterable of items exposing
          `.term`, `.types`, optional `.RAG`).
        - List of dicts with keys `term`, `types`, optional `RAG`.
        - List/tuple of `(term, types[, RAG])`.

        Parameters
        data:
            Training payload.

        Returns
        List[Dict[str, Any]]
            Normalized dictionaries ready for training.

        Raises
        ValueError
            If `data` is neither a list/tuple nor exposes `.term_typings`.
        """
        normalized_rows: List[Dict[str, Any]] = []

        # Case 1: object with attribute `.term_typings`
        term_typings_attr = getattr(data, "term_typings", None)
        if term_typings_attr is not None:
            for item in term_typings_attr:
                term_text = getattr(item, "term", None)
                type_list = getattr(item, "types", None)
                rag_neighbors = getattr(item, "RAG", None)
                if term_text is None or type_list is None:
                    continue
                if not isinstance(type_list, list):
                    type_list = [type_list]
                normalized_rows.append(
                    {
                        "term": str(term_text),
                        "types": [str(x) for x in type_list],
                        "RAG": rag_neighbors,
                    }
                )
            return normalized_rows

        # Otherwise: must be a list/tuple-like container
        if not isinstance(data, (list, tuple)):
            raise ValueError(
                "Training data must be a list/tuple or expose .term_typings"
            )

        if not data:
            return normalized_rows

        # Case 2: list of dicts
        if isinstance(data[0], dict):
            for row in data:
                term_text = row.get("term")
                type_list = row.get("types")
                rag_neighbors = row.get("RAG")
                if term_text is None or type_list is None:
                    continue
                if not isinstance(type_list, list):
                    type_list = [type_list]
                normalized_rows.append(
                    {
                        "term": str(term_text),
                        "types": [str(x) for x in type_list],
                        "RAG": rag_neighbors,
                    }
                )
            return normalized_rows

        # Case 3: list of tuples/lists: (term, types[, RAG])
        for item in data:
            if not isinstance(item, (list, tuple)) or len(item) < 2:
                continue
            term_text, type_list = item[0], item[1]
            rag_neighbors = item[2] if len(item) > 2 else None
            if term_text is None or type_list is None:
                continue
            if not isinstance(type_list, list):
                type_list = [type_list]
            normalized_rows.append(
                {
                    "term": str(term_text),
                    "types": [str(x) for x in type_list],
                    "RAG": rag_neighbors,
                }
            )

        return normalized_rows

    def _as_predict_terms_ids(self, data: Any) -> Tuple[List[str], List[Any]]:
        """Normalize prediction input into parallel lists: (terms, ids).

        Supported Inputs
        - Object with `.term_typings`.
        - List of dicts with `term` and optional `id`.
        - List of tuples/lists `(term, id[, ...])`.
        - List of plain term strings.

        Parameters
        data:
            Evaluation payload.

        Returns
        Tuple[List[str], List[Any]]
            `(terms, example_ids)` lists aligned by index.

        Raises
        ValueError
            If the input format is unsupported.
        """
        terms: List[str] = []
        example_ids: List[Any] = []

        # Case 1: object with attribute `.term_typings`
        term_typings_attr = getattr(data, "term_typings", None)
        if term_typings_attr is not None:
            for idx, item in enumerate(term_typings_attr):
                terms.append(str(getattr(item, "term", "")))
                example_ids.append(getattr(item, "id", getattr(item, "ID", idx)))
            return terms, example_ids

        # Case 2: list/tuple container
        if isinstance(data, (list, tuple)) and data:
            first_element = data[0]

            # 2a) list of dicts
            if isinstance(first_element, dict):
                for i, row in enumerate(data):
                    terms.append(str(row.get("term", "")))
                    example_ids.append(row.get("id", row.get("ID", i)))
                return terms, example_ids

            # 2b) list of tuples/lists: (term, id[, ...])
            if isinstance(first_element, (list, tuple)):
                for i, tuple_row in enumerate(data):
                    if not tuple_row:
                        continue
                    terms.append(str(tuple_row[0]))
                    example_ids.append(tuple_row[1] if len(tuple_row) > 1 else i)
                return terms, example_ids

            # 2c) list of strings (terms only)
            if isinstance(first_element, str):
                terms = [str(x) for x in data]  # type: ignore[arg-type]
                example_ids = list(range(len(terms)))
                return terms, example_ids

        raise ValueError("Unsupported predict() input format.")

    def _as_gold_id_term_types(self, data: Any) -> List[Dict[str, Any]]:
        """Normalize gold labels into a list of dicts: {id, term, types}.

        Supported Inputs
        Mirrors `_as_term_types_dicts`, but ensures an `id` is set.

        Parameters
        data:
            Ground-truth payload.

        Returns
        List[Dict[str, Any]]
            `{'id': Any, 'term': str, 'types': List[str]}` entries.

        """
        gold_rows: List[Dict[str, Any]] = []

        # Case 1: object with attribute `.term_typings`
        term_typings_attr = getattr(data, "term_typings", None)
        if term_typings_attr is not None:
            for idx, item in enumerate(term_typings_attr):
                gold_id = getattr(item, "id", getattr(item, "ID", idx))
                term_text = str(getattr(item, "term", ""))
                type_list = getattr(item, "types", [])
                if not isinstance(type_list, list):
                    type_list = [type_list]
                gold_rows.append(
                    {
                        "id": gold_id,
                        "term": term_text,
                        "types": [str(t) for t in type_list],
                    }
                )
            return gold_rows

        # Case 2: list/tuple container
        if isinstance(data, (list, tuple)) and data:
            first_element = data[0]

            # 2a) list of dicts
            if isinstance(first_element, dict):
                for i, row in enumerate(data):
                    gold_id = row.get("id", row.get("ID", i))
                    term_text = str(row.get("term", ""))
                    type_list = row.get("types", [])
                    if not isinstance(type_list, list):
                        type_list = [type_list]
                    gold_rows.append(
                        {
                            "id": gold_id,
                            "term": term_text,
                            "types": [str(t) for t in type_list],
                        }
                    )
                return gold_rows

            # 2b) list of tuples/lists: (term, types[, id])
            if isinstance(first_element, (list, tuple)):
                for i, tuple_row in enumerate(data):
                    if not tuple_row or len(tuple_row) < 2:
                        continue
                    term_text = str(tuple_row[0])
                    type_list = tuple_row[1]
                    gold_id = tuple_row[2] if len(tuple_row) > 2 else i
                    if not isinstance(type_list, list):
                        type_list = [type_list]
                    gold_rows.append(
                        {
                            "id": gold_id,
                            "term": term_text,
                            "types": [str(t) for t in type_list],
                        }
                    )
                return gold_rows

        raise ValueError(
            "Unsupported ground-truth input format for tasks_ground_truth_former()."
        )


class AlexbekRAGLearner(AutoLearner):
    """Retrieval-Augmented Term Typing learner (single task: term-typing).

    Flow
    1) `fit`: collect (term -> [types]) examples, build an in-memory index
       using a sentence-embedding model.
    2) `predict`: for each new term, retrieve top-k similar examples, compose a
       structured prompt, query an instruction-tuned causal LLM, and parse types.

    Returns
    List[Dict[str, Any]]
        `{"term": str, "types": List[str], "id": Optional[str]}` rows.
    """

    def __init__(
        self,
        llm_model_id: str = "Qwen/Qwen2.5-0.5B-Instruct",
        retriever_model_id: str = "sentence-transformers/all-MiniLM-L6-v2",
        device: str = "auto",  # "auto" | "cuda" | "cpu"
        token: str = "",  # HF token if needed
        top_k: int = 3,
        max_new_tokens: int = 256,
        gen_batch_size: int = 4,  # generation batch size
        enc_batch_size: int = 64,  # embedding batch size
        **kwargs: Any,  # absorb extra pipeline-style args
    ) -> None:
        """Configure the RAG learner.

        Parameters
        llm_model_id:
            HF model id/path for the instruction-tuned causal LLM.
        retriever_model_id:
            Sentence-embedding model id for retrieval.
        device:
            Device policy ('auto'|'cuda'|'cpu') for the LLM.
        token:
            Optional HF token for gated models.
        top_k:
            Number of nearest examples to retrieve per query term.
        max_new_tokens:
            Decoding budget for the LLM.
        gen_batch_size:
            Number of prompts per generation batch.
        enc_batch_size:
            Number of texts per embedding batch.
        **kwargs:
            Extra configuration captured for downstream use.
        """
        super().__init__()

        # Consolidated configuration for simple serialization
        self.cfg: Dict[str, Any] = {
            "llm_model_id": llm_model_id,
            "retriever_model_id": retriever_model_id,
            "device": device,
            "token": token,
            "top_k": int(top_k),
            "max_new_tokens": int(max_new_tokens),
            "gen_batch_size": int(gen_batch_size),
            "enc_batch_size": int(enc_batch_size),
        }
        self.extra_cfg: Dict[str, Any] = dict(kwargs)

        # LLM components
        self.tokenizer: Optional[AutoTokenizer] = None
        self.generation_model: Optional[AutoModelForCausalLM] = None

        # Retriever components
        self.embedder: Optional[SentenceTransformer] = None
        self.indexed_corpus: List[str] = []  # items: "<term> || [<types>...]"
        self.corpus_embeddings: Optional[torch.Tensor] = None

        # Training cache of (term, [types]) tuples
        self.train_term_types: List[Tuple[str, List[str]]] = []

        # Prompt templates
        self._system_prompt: str = (
            "You are an expert in ontologies and semantic term classification.\n"
            "Task: determine semantic types for the TERM using the EXAMPLES provided.\n"
            "Rules:\n"
            "1) Types must be generalizing categories from the domain ontology.\n"
            "2) Be concise. Respond ONLY in JSON using double quotes.\n"
            'Format: {"term":"...", "reasoning":"<<=100 words>>", "types":["...", "..."]}\n'
        )
        self._user_prompt_template: str = """{examples}

            TERM: {term}

            TASK: Determine semantic types for the given term based on the domain ontology.
            Remember: types are generalizing categories, not the term itself. Respond in JSON.
            """

    def load(
        self,
        model_id: Optional[str] = None,
        retriever_id: Optional[str] = None,
        device: Optional[str] = None,
        token: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Load the LLM and the embedding retriever. Overrides constructor values if provided.

        Parameters
        model_id:
            Optional override for the LLM model id.
        retriever_id:
            Optional override for the embedding model id.
        device:
            Optional override for device selection policy.
        token:
            Optional override for HF token.
        **kwargs:
            Extra values to store in `extra_cfg`.

        """
        if model_id is not None:
            self.cfg["llm_model_id"] = model_id
        if retriever_id is not None:
            self.cfg["retriever_model_id"] = retriever_id
        if device is not None:
            self.cfg["device"] = device
        if token is not None:
            self.cfg["token"] = token
        self.extra_cfg.update(kwargs)

        # Choose device & dtype for the LLM
        cuda_available: bool = torch.cuda.is_available()
        use_cuda: bool = cuda_available and (self.cfg["device"] != "cpu")
        device_map: str = "auto" if use_cuda else "cpu"
        torch_dtype = torch.bfloat16 if use_cuda else torch.float32

        # Tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.cfg["llm_model_id"], padding_side="left", token=self.cfg["token"]
        )
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        # LLM
        self.generation_model = AutoModelForCausalLM.from_pretrained(
            self.cfg["llm_model_id"],
            device_map=device_map,
            torch_dtype=torch_dtype,
            token=self.cfg["token"],
        )

        # Deterministic decoding defaults
        generation_cfg = self.generation_model.generation_config
        generation_cfg.do_sample = False
        generation_cfg.temperature = None
        generation_cfg.top_p = None
        generation_cfg.top_k = None
        generation_cfg.num_beams = 1

        # Retriever
        self.embedder = SentenceTransformer(
            self.cfg["retriever_model_id"], trust_remote_code=True
        )

    def fit(self, train_data: Any, task: str, ontologizer: bool = True) -> None:
        """Prepare the retrieval index from training examples.

        Parameters
        train_data:
            Training payload containing terms and their types.
        task:
            Must be `'term-typing'`; other tasks are forwarded to base.
        ontologizer:
            Unused flag for API compatibility.

        Side Effects
        - Normalizes to a list of `(term, [types])`.
        - Builds an indexable text corpus and (if embedder is loaded)
          computes embeddings for retrieval.
        """
        if task != "term-typing":
            return super().fit(train_data, task, ontologizer)

        # Normalize incoming training data -> list[(term, [types])]
        self.train_term_types = self._unpack_train(train_data)

        # Build the textual corpus to index
        self.indexed_corpus = [
            f"{term} || {json.dumps(types, ensure_ascii=False)}"
            for term, types in self.train_term_types
        ]

        # Embed the corpus if available; else fall back to zero-shot prompting
        if self.indexed_corpus and self.embedder is not None:
            self.corpus_embeddings = self._encode_texts(self.indexed_corpus)
        else:
            self.corpus_embeddings = None

    def predict(self, eval_data: Any, task: str, ontologizer: bool = True) -> Any:
        """Predict types for evaluation items; returns a list of {term, types, id?}.

        Parameters
        eval_data:
            Evaluation payload to type (terms + optional ids).
        task:
            Must be `'term-typing'`; other tasks are forwarded to base.
        ontologizer:
            Unused flag for API compatibility.

        Returns
        List[Dict[str, Any]]
            For each input term, a dictionary with keys:
            - `term`: The input term.
            - `types`: A (unique, sorted) list of predicted types.
            - `id`: Optional example id (if provided in input).
        """
        if task != "term-typing":
            return super().predict(eval_data, task, ontologizer)

        eval_terms, eval_ids = self._unpack_eval(eval_data)
        if not eval_terms:
            return []

        # Use RAG if we have an indexed corpus & embeddings; otherwise zero-shot
        rag_available = (
            self.corpus_embeddings is not None
            and self.embedder is not None
            and len(self.indexed_corpus) > 0
        )

        if rag_available:
            neighbor_docs_per_query = self._retrieve_batch(
                eval_terms, top_k=int(self.cfg["top_k"])
            )
        else:
            neighbor_docs_per_query = [[] for _ in eval_terms]

        # Compose prompts
        prompts: List[str] = []
        for term, neighbor_docs in zip(eval_terms, neighbor_docs_per_query):
            example_pairs = self._decode_examples(neighbor_docs)
            examples_block = self._format_examples(example_pairs)
            prompt_text = self._compose_prompt(examples_block, term)
            prompts.append(prompt_text)

        predicted_types_lists = self._generate_and_parse(prompts)

        # Build standardized results
        results: List[Dict[str, Any]] = []
        for term, example_id, predicted_types in zip(
            eval_terms, eval_ids, predicted_types_lists
        ):
            result_row: Dict[str, Any] = {
                "term": term,
                "types": sorted({t for t in predicted_types}),  # unique + sorted
            }
            if example_id is not None:
                result_row["id"] = example_id
            results.append(result_row)

        assert all(("term" in row and "types" in row) for row in results), (
            "predict() must return term + types"
        )
        return results

    def _unpack_train(self, data: Any) -> List[Tuple[str, List[str]]]:
        """Extract `(term, [types])` tuples from supported training payloads.

        Supported Inputs
        - `data.term_typings` (objects exposing `.term` & `.types`)
        - `list[dict]` with keys `'term'` and `'types'`
        - `list[str]` → returns empty (nothing to index)
        - other formats → empty

        Parameters
        data:
            Training payload.

        Returns
        List[Tuple[str, List[str]]]
            (term, types) tuples (types kept as strings).
        """
        term_typings = getattr(data, "term_typings", None)
        if term_typings is not None:
            parsed_pairs: List[Tuple[str, List[str]]] = []
            for item in term_typings:
                term = getattr(item, "term", None)
                types = list(getattr(item, "types", []) or [])
                if term and types:
                    parsed_pairs.append(
                        (term, [t for t in types if isinstance(t, str)])
                    )
            return parsed_pairs

        if isinstance(data, list) and data and isinstance(data[0], dict):
            parsed_pairs = []
            for row in data:
                term = row.get("term")
                types = row.get("types") or []
                if term and isinstance(types, list) and types:
                    parsed_pairs.append(
                        (term, [t for t in types if isinstance(t, str)])
                    )
            return parsed_pairs

        # If only a list of strings is provided, there's nothing to index for RAG
        if isinstance(data, (list, set, tuple)) and all(
            isinstance(x, str) for x in data
        ):
            return []

        return []

    def _unpack_eval(self, data: Any) -> Tuple[List[str], List[Optional[str]]]:
        """Extract `(terms, ids)` from supported evaluation payloads.

        Supported Inputs
        - `data.term_typings` (objects exposing `.term` & optional `.id`)
        - `list[str]`
        - `list[dict]` with `term` and optional `id`

        Parameters
        data:
            Evaluation payload.

        Returns
        Tuple[List[str], List[Optional[str]]]
            Two lists aligned by index: terms and ids (ids may contain `None`).
        """
        term_typings = getattr(data, "term_typings", None)
        if term_typings is not None:
            terms: List[str] = []
            ids: List[Optional[str]] = []
            for item in term_typings:
                terms.append(getattr(item, "term", ""))
                ids.append(getattr(item, "id", None))
            return terms, ids

        if isinstance(data, list) and data and isinstance(data[0], str):
            return list(data), [None] * len(data)

        if isinstance(data, list) and data and isinstance(data[0], dict):
            terms: List[str] = []
            ids: List[Optional[str]] = []
            for row in data:
                terms.append(row.get("term", ""))
                ids.append(row.get("id"))
            return terms, ids

        return [], []

    def _encode_texts(self, texts: List[str]) -> torch.Tensor:
        """Encode a batch of texts with the sentence-embedding model.

        Parameters
        texts:
            List of strings to embed.

        Returns
        torch.Tensor
            Tensor of shape `(len(texts), hidden_dim)`. If `texts` is empty,
            returns an empty tensor with 0 rows.
        """
        batch_size = int(self.cfg["enc_batch_size"])
        batch_embeddings: List[torch.Tensor] = []

        for batch_start in range(0, len(texts), batch_size):
            batch_texts = texts[batch_start : batch_start + batch_size]
            embeddings = self.embedder.encode(
                batch_texts, convert_to_tensor=True, show_progress_bar=False
            )
            batch_embeddings.append(embeddings)

        return (
            torch.cat(batch_embeddings, dim=0) if batch_embeddings else torch.empty(0)
        )

    def _retrieve_batch(self, queries: List[str], top_k: int) -> List[List[str]]:
        """Return for each query the top-k most similar corpus entries.

        Parameters
        queries:
            List of query terms.
        top_k:
            Number of neighbors to retrieve for each query.

        Returns
        List[List[str]]
            For each query, a list of raw corpus strings formatted as
            `"<term> || [\\"type1\\", ...]"`.
        """
        if self.corpus_embeddings is None or not self.indexed_corpus:
            return [[] for _ in queries]

        query_embeddings = self._encode_texts(queries)  # [Q, D]
        doc_embeddings = self.corpus_embeddings  # [N, D]
        if query_embeddings.shape[-1] != doc_embeddings.shape[-1]:
            raise ValueError(
                f"Embedding dim mismatch: {query_embeddings.shape[-1]} vs {doc_embeddings.shape[-1]}"
            )

        # Cosine similarity via L2-normalized dot product
        q_norm = F.normalize(query_embeddings, p=2, dim=1)
        d_norm = F.normalize(doc_embeddings, p=2, dim=1)
        cos_sim = torch.matmul(q_norm, d_norm.T)  # [Q, N]

        k = min(max(1, top_k), len(self.indexed_corpus))
        _, top_indices = torch.topk(cos_sim, k=k, dim=1)
        return [[self.indexed_corpus[j] for j in row.tolist()] for row in top_indices]

    def _decode_examples(self, docs: List[str]) -> List[Tuple[str, List[str]]]:
        """Parse raw corpus rows ('term || [types]') into `(term, [types])` pairs.

        Parameters
        docs:
            Raw strings from the index/corpus.

        Returns
        List[Tuple[str, List[str]]]
            Parsed (term, types) pairs; malformed rows are skipped.
        """
        example_pairs: List[Tuple[str, List[str]]] = []
        for raw_row in docs:
            try:
                term_raw, types_json = raw_row.split("||", 1)
                term = term_raw.strip()
                types_list = json.loads(types_json.strip())
                if isinstance(types_list, list):
                    example_pairs.append(
                        (term, [t for t in types_list if isinstance(t, str)])
                    )
            except Exception:
                continue
        return example_pairs

    def _format_examples(self, pairs: List[Tuple[str, List[str]]]) -> str:
        """Format retrieved example pairs into a compact block for the prompt.

        Parameters
        pairs:
            Retrieved `(term, [types])` examples.

        Returns
        str
            Human-readable lines to provide *light* guidance to the LLM.
        """
        if not pairs:
            return "EXAMPLES: (none provided)"
        lines: List[str] = ["CLASSIFICATION EXAMPLES:"]
        for idx, (term, types) in enumerate(pairs, 1):
            preview_types = types[:3]  # keep context small
            lines.append(f"{idx}. Term: '{term}' → Types: {list(preview_types)}")
        lines.append("END OF EXAMPLES.")
        return "\n".join(lines)

    def _compose_prompt(self, examples_block: str, term: str) -> str:
        """Compose the final prompt from system + user blocks.

        Parameters
        examples_block:
            Text block with retrieved examples.
        term:
            The query term to classify.

        Returns
        str
            Full prompt string passed to the LLM.
        """
        user_block = self._user_prompt_template.format(
            examples=examples_block, term=term
        )
        return f"{self._system_prompt}\n\n{user_block}\n"

    def _generate_and_parse(self, prompts: List[str]) -> List[List[str]]:
        """Run generation for a batch of prompts and parse the JSON `'types'` from outputs.

        Parameters
        prompts:
            Finalized prompts for the LLM.

        Returns
        List[List[str]]
            For each prompt, a list of predicted type strings.
        """
        batch_size = int(self.cfg["gen_batch_size"])
        all_predicted_types: List[List[str]] = []

        for batch_start in range(0, len(prompts), batch_size):
            prompt_batch = prompts[batch_start : batch_start + batch_size]

            # Tokenize and move to the LLM's device
            model_device = getattr(self.generation_model, "device", None)
            encodings = self.tokenizer(
                prompt_batch, return_tensors="pt", padding=True
            ).to(model_device)
            input_token_length = encodings["input_ids"].shape[1]

            # Deterministic decoding (greedy)
            with torch.no_grad():
                generated_tokens = self.generation_model.generate(
                    **encodings,
                    do_sample=False,
                    num_beams=1,
                    temperature=None,
                    top_p=None,
                    top_k=None,
                    max_new_tokens=int(self.cfg["max_new_tokens"]),
                    pad_token_id=self.tokenizer.eos_token_id,
                )

            # Slice off the prompt tokens and decode only newly generated tokens
            new_token_span = generated_tokens[:, input_token_length:]
            decoded_texts = [
                self.tokenizer.decode(seq, skip_special_tokens=True)
                for seq in new_token_span
            ]

            parsed_types_per_prompt = [
                self._parse_types(text) for text in decoded_texts
            ]
            all_predicted_types.extend(parsed_types_per_prompt)

        return all_predicted_types

    def _parse_types(self, text: str) -> List[str]:
        """Extract a list of type strings from LLM output.

        Parsing Strategy (in order)
        1) Strict JSON object with `"types"`.
        2) Regex-extract JSON object containing `"types"`.
        3) Regex-extract first bracketed list.
        4) Comma-split fallback.

        Parameters
        text:
            Raw LLM output to parse.

        Returns
        List[str]
            Parsed list of type strings (possibly empty if parsing fails).
        """
        try:
            obj = json.loads(text)
            if isinstance(obj, dict) and isinstance(obj.get("types"), list):
                return [t for t in obj["types"] if isinstance(t, str)]
        except Exception:
            pass

        try:
            obj_match = re.search(
                r'\{[^{}]*"types"\s*:\s*\[[^\]]*\][^{}]*\}', text, re.S
            )
            if obj_match:
                obj = json.loads(obj_match.group(0))
                types = obj.get("types", [])
                return [t for t in types if isinstance(t, str)]
        except Exception:
            pass

        try:
            list_match = re.search(r"\[([^\]]+)\]", text)
            if list_match:
                items = [
                    x.strip().strip('"').strip("'")
                    for x in list_match.group(1).split(",")
                ]
                return [t for t in items if t]
        except Exception:
            pass

        if "," in text:
            items = [x.strip().strip('"').strip("'") for x in text.split(",")]
            return [t for t in items if t]

        return []
