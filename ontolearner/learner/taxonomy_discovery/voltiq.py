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

from __future__ import annotations

import json
import math
import os
import re
import urllib.request
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import networkx as nx

from ...base import AutoLearner


class VoltIQTaxonomyLearner(AutoLearner):
    """
    This implementation integrates the original Volt-IQ submission to the
    LLMs4OL 2026 competition into the OntoLearner framework. The original
    substring induction, lexical subsumption, rewrite cascade, source-domain
    priors, and OBO/OWL parent recovery methods are preserved.
    """

    TAXONOMY_DISCOVERY_BENCHMARK_METHODS = (
        "lexical_subsumption",
        "parent_prior",
        "tfidf_pair_linear",
        "hybrid_cascade",
        "rewrite_cascade",
    )
    TAXONOMY_DISCOVERY_TEST_METHODS = TAXONOMY_DISCOVERY_BENCHMARK_METHODS + (
        "go_rewrite_hybrid",
        "go_rewrite_strict",
        "obo_rewrite_hybrid",
        "obo_rewrite_strict",
        "obo_owl_rewrite_hybrid",
        "obo_owl_rewrite_strict",
        "domain_calibrated_primary",
        "domain_calibrated_backup",
        "domain_calibrated_conservative",
        "substring_heuristic",
    )
    GO_BASIC_OBO_URL = "http://current.geneontology.org/ontology/go-basic.obo"
    OBO_SOURCE_URLS = {
        "go": GO_BASIC_OBO_URL,
        "cl": "http://purl.obolibrary.org/obo/cl.obo",
        "envo": "http://purl.obolibrary.org/obo/envo.obo",
        "pato": "http://purl.obolibrary.org/obo/pato.obo",
        "uo": "http://purl.obolibrary.org/obo/uo.obo",
        "bfo": "http://purl.obolibrary.org/obo/bfo.obo",
        "obi": "http://purl.obolibrary.org/obo/obi.obo",
        "ro": "http://purl.obolibrary.org/obo/ro.obo",
        "po": "http://purl.obolibrary.org/obo/po.obo",
        "uberon": "http://purl.obolibrary.org/obo/uberon.obo",
        "chebi": "http://purl.obolibrary.org/obo/chebi.obo",
        "mondo": "http://purl.obolibrary.org/obo/mondo.obo",
        "hp": "http://purl.obolibrary.org/obo/hp.obo",
        "doid": "http://purl.obolibrary.org/obo/doid.obo",
        "ncit": "http://purl.obolibrary.org/obo/ncit.obo",
    }
    TAXONOMY_DISCOVERY_OBO_SOURCE_KEYS = tuple(OBO_SOURCE_URLS)
    TAXONOMY_DISCOVERY_OWL_SOURCE_URLS = {
        "iao": "https://raw.githubusercontent.com/information-artifact-ontology/IAO/master/iao.owl",
        "edam": "https://edamontology.org/EDAM.owl",
        "swo": "http://purl.obolibrary.org/obo/swo.owl",
    }
    TAXONOMY_DISCOVERY_OWL_SOURCE_KEYS = tuple(TAXONOMY_DISCOVERY_OWL_SOURCE_URLS)
    OBO_IN_OWL_PREFIX = "http://www.geneontology.org/formats/oboInOwl#"
    REWRITE_SUFFIX_RULES = (
        (" model prediction", " model", 2.8),
        (" modeling assumption", " model", 2.8),
        (" characteristic", "", 2.4),
        (" initial condition", "", 2.2),
        (" boundary condition", "", 2.2),
        (" parameter", "", 2.0),
        (" property", "", 2.0),
    )

### Initialize Parameters ####################################################

    def __init__(
        self,
        method: str = "hybrid_cascade",
        target_domain: Optional[str] = None,
        cache_dir: Optional[str | Path] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the Volt-IQ taxonomy learner and resource paths.

        Args:
            method: Taxonomy induction method to use. Domain-calibrated methods
                require one of the named LLMs4OL 2026 Taxonomy discovery target domains.
            target_domain: Target domain (Archeon, Biora, Hylex, or Phyra) for
                domain-calibrated prediction. Optional for other methods.
            cache_dir: Directory for locally cached OBO and OWL resources.
            **kwargs: Additional arguments passed to AutoLearner.

        Raises:
            ValueError: If the method is unknown or its target domain is missing.
        """
        super().__init__(**kwargs)
        if method not in self.TAXONOMY_DISCOVERY_TEST_METHODS:
            raise ValueError(f"Unknown taxonomy method: {method}")
        if method.startswith("domain_calibrated_") and target_domain not in {
            "Archeon", "Biora", "Hylex", "Phyra"
        }:
            raise ValueError("A named Taxonomy discovery target_domain is required for domain calibration.")

        self.method = method
        self.target_domain = target_domain
        self.train_edges: List[Tuple[str, str]] = []
        self.train_types: List[str] = []
        self.is_fitted = False

        # OBO/OWL resources are used only by ontology-backed prediction methods.
        cache_root = cache_dir or os.environ.get(
            "LLMS4OL_CACHE_DIR", Path.home() / ".cache" / "ontolearner"
        )
        self.TAXONOMY_DISCOVERY_CACHE_DIR = Path(cache_root) / "taxonomy_discovery"
        self.GO_BASIC_OBO_PATH = self.TAXONOMY_DISCOVERY_CACHE_DIR / "go-basic.obo"
        self.GO_BASIC_INDEX_PATH = self.TAXONOMY_DISCOVERY_CACHE_DIR / "go_basic_index.json"
        self.OBO_PROBE_CACHE_DIR = self.TAXONOMY_DISCOVERY_CACHE_DIR / "obo_probe"
        self.OWL_PROBE_CACHE_DIR = self.TAXONOMY_DISCOVERY_CACHE_DIR / "owl_probe"

### OntoLearner Task Interface ###############################################

    def tasks_data_former(self, data: Any, task: str, test: bool = False) -> Any:
        """
        Preserve OntoLearner's taxonomy data for training and prediction.

        The default AutoLearner formatter returns only type labels for taxonomy
        discovery. Volt-IQ also needs the source taxonomy relations during fit(),
        so the full OntologyData object is retained.

        Args:
            data: Extracted ontology data.
            task: Ontology learning task.
            test: Whether data are being formatted for inference.

        Returns:
            The original ontology data for taxonomy discovery; otherwise the
            output of AutoLearner's default formatter.
        """
        if task == "taxonomy-discovery":
            return data
        return super().tasks_data_former(data=data, task=task, test=test)

    def fit(self, train_data: Any, task: str, ontologizer: bool = True) -> None:
        """
        Fit the learner using source taxonomy relations and type labels.

        The original Taxonomy discovery methods use training edges to estimate parent priors
        and construct features during prediction. No additional model is trained
        by this method.

        Args:
            train_data: OntoLearner OntologyData or a list of such objects.
            task: Ontology learning task.
            ontologizer: Whether to apply OntoLearner data formatting.

        Raises:
            ValueError: If the task or required taxonomy data are invalid.
        """
        if task != "taxonomy-discovery":
            raise ValueError(f"{task} is not a valid task for Volt-IQ.")
        if ontologizer:
            train_data = self.tasks_data_former(data=train_data, task=task, test=False)

        # Collect source taxonomy relations in (child, parent) order.
        datasets = train_data if isinstance(train_data, (list, tuple)) else [train_data]
        train_edges = []
        train_types = []
        for data in datasets:
            taxonomies = getattr(data, "type_taxonomies", None)
            if taxonomies is None:
                raise ValueError("Expected OntoLearner data with type_taxonomies.")
            train_types.extend(taxonomies.types)
            for relation in taxonomies.taxonomies:
                if isinstance(relation.parent, str) and isinstance(relation.child, str):
                    train_edges.append((relation.child, relation.parent))

        if not train_edges:
            raise ValueError("No taxonomy relations found in training data.")
        # Keep the cleaned source relations for candidate scoring at inference.
        self.train_edges = self._clean_taxonomy_edges(train_edges)
        self.train_types = list(dict.fromkeys(train_types))
        self.is_fitted = True

    def predict(self, eval_data: Any, task: str, ontologizer: bool = True) -> List[Dict[str, str]]:
        """
        Predict taxonomy relations using the target ontology type labels.

        Only the target label inventory is used for prediction. Ground-truth
        relations from the evaluation ontology are not accessed.

        Args:
            eval_data: OntoLearner ontology data containing target labels.
            task: Ontology learning task.
            ontologizer: Whether to apply OntoLearner data formatting.

        Returns:
            List[Dict[str, str]]: Predicted relations with parent and child keys.
        """
        if task != "taxonomy-discovery":
            raise ValueError(f"{task} is not a valid task for Volt-IQ.")
        if ontologizer:
            eval_data = self.tasks_data_former(data=eval_data, task=task, test=True)

        if not self.is_fitted:
            raise RuntimeError("Call fit() with OntoLearner training data first.")
        taxonomies = getattr(eval_data, "type_taxonomies", None)
        if taxonomies is None:
            raise ValueError("Expected OntoLearner data with type_taxonomies.")
        # Use only target labels; held-out taxonomy relations remain untouched.
        labels = taxonomies.types
        original_labels = self._build_original_label_map(labels)

        # Select the original method family for the named Taxonomy discovery domain.
        if self.method in {"domain_calibrated_primary", "domain_calibrated_backup", "domain_calibrated_conservative"}:
            if self.target_domain == "Biora":
                if self.method == "domain_calibrated_conservative":
                    predicted_edges = self._predict_taxonomy_discovery_edges_for_labels(
                        train_edges=self.train_edges,
                        train_types=self.train_types,
                        test_types=labels,
                        method="substring_heuristic",
                    )
                else:
                    predicted_edges = self._predict_obo_backfilled_edges(
                        train_edges=self.train_edges,
                        test_types=labels,
                        include_rewrite_fallback=self.method == "domain_calibrated_primary",
                        include_owl_sources=True,
                    )
            else:
                calibrated_method = (
                    "lexical_subsumption" if self.target_domain == "Hylex"
                    else "substring_heuristic"
                )
                predicted_edges = self._predict_taxonomy_discovery_edges_for_labels(
                    train_edges=self.train_edges,
                    train_types=self.train_types,
                    test_types=labels,
                    method=calibrated_method,
                )
        elif self.method in {
            "obo_rewrite_hybrid", "obo_rewrite_strict",
            "obo_owl_rewrite_hybrid", "obo_owl_rewrite_strict",
        }:
            predicted_edges = self._predict_obo_backfilled_edges(
                train_edges=self.train_edges,
                test_types=labels,
                include_rewrite_fallback=self.method in {
                    "obo_rewrite_hybrid", "obo_owl_rewrite_hybrid"
                },
                include_owl_sources=self.method in {
                    "obo_owl_rewrite_hybrid", "obo_owl_rewrite_strict"
                },
            )
        elif self.method in {"go_rewrite_hybrid", "go_rewrite_strict"} and self.target_domain == "Biora":
            predicted_edges = self._predict_go_backfilled_biora_edges(
                train_edges=self.train_edges,
                test_types=labels,
                include_rewrite_fallback=self.method == "go_rewrite_hybrid",
            )
        else:
            selected_method = (
                "rewrite_cascade" if self.method in {"go_rewrite_hybrid", "go_rewrite_strict"}
                else self.method
            )
            predicted_edges = self._predict_taxonomy_discovery_edges_for_labels(
                train_edges=self.train_edges,
                train_types=self.train_types,
                test_types=labels,
                method=selected_method,
            )

        return [
            {
                "parent": original_labels.get(parent, parent),
                "child": original_labels.get(child, child),
            }
            for child, parent in predicted_edges
        ]

### Taxonomy Data Normalization ##############################################

    def _normalize_label(self, label: str) -> str:
        """Normalize label text for matching and candidate generation."""
        value = label.lower().strip()
        value = re.sub(r"[_/\\-]+", " ", value)
        value = re.sub(r"[^\w\s]", " ", value)
        value = re.sub(r"\s+", " ", value)
        return value.strip()

    def _build_original_label_map(self, labels: list[str]) -> dict[str, str]:
        """Map normalized labels back to the original target label spellings."""
        original_by_normalized: dict[str, str] = {}
        for label in labels:
            if not isinstance(label, str):
                continue
            normalized = self._normalize_label(label)
            if normalized and normalized not in original_by_normalized:
                original_by_normalized[normalized] = label.strip()
        return original_by_normalized

    def _clean_taxonomy_edges(self, edges):
        """
        Normalize, deduplicate, and remove cycles from taxonomy edges.

        Args:
            edges: Iterable of (child, parent) relations.

        Returns:
            List of valid, acyclic (child, parent) relations.
        """
        graph = nx.DiGraph()
        cleaned = []
        seen = set()
        for child, parent in edges:
            child_norm = self._normalize_label(child)
            parent_norm = self._normalize_label(parent)
            if not child_norm or not parent_norm or child_norm == parent_norm:
                continue
            edge = (child_norm, parent_norm)
            if edge in seen:
                continue
            graph.add_edge(child_norm, parent_norm)
            if not nx.is_directed_acyclic_graph(graph):
                graph.remove_edge(child_norm, parent_norm)
                continue
            seen.add(edge)
            cleaned.append(edge)
        return cleaned

    def _select_predicted_edges(self, *, scored_edges, expected_edge_count, max_parents_per_child=1):
        """
        Select the highest-ranked taxonomy edges without introducing cycles.

        Args:
            scored_edges: Candidate (child, parent, score) tuples.
            expected_edge_count: Maximum number of edges to retain.
            max_parents_per_child: Upper bound on selected parents per child.

        Returns:
            List of selected (child, parent) relations.
        """
        selected = []
        parents_per_child = defaultdict(int)
        graph = nx.DiGraph()
        # Select highest-scoring candidates while respecting parent and cycle limits.
        for child, parent, score in sorted(scored_edges, key=lambda item: (-item[2], item[0], item[1])):
            if len(selected) >= expected_edge_count:
                break
            if parents_per_child[child] >= max_parents_per_child:
                continue
            graph.add_edge(child, parent)
            if not nx.is_directed_acyclic_graph(graph):
                graph.remove_edge(child, parent)
                continue
            selected.append((child, parent))
            parents_per_child[child] += 1
        return selected

    def _dedupe_taxonomy_edges(self, edges):
        """Normalize and remove duplicate or self-referential edges."""
        cleaned = []
        seen = set()
        for child, parent in edges:
            child_norm = self._normalize_label(child)
            parent_norm = self._normalize_label(parent)
            if not child_norm or not parent_norm or child_norm == parent_norm:
                continue
            edge = (child_norm, parent_norm)
            if edge in seen:
                continue
            seen.add(edge)
            cleaned.append(edge)
        return cleaned

    def _token_set(self, text: str) -> set[str]:
        """Return the set of normalized tokens in a label."""
        return {token for token in self._normalize_label(text).split() if token}

    def _char_3grams(self, text: str) -> set[str]:
        """Return character trigrams for normalized label similarity."""
        value = f" {self._normalize_label(text)} "
        if len(value) < 3:
            return {value}
        return {value[index:index + 3] for index in range(len(value) - 2)}

    def _jaccard(self, a: set[str], b: set[str]) -> float:
        """Compute Jaccard similarity between two sets."""
        if not a and not b:
            return 0.0
        union = a | b
        if not union:
            return 0.0
        return len(a & b) / len(union)

    def _suffix_match_score(self, child: str, parent: str) -> float:
        """Check whether two labels share the same final token."""
        child_tokens = self._normalize_label(child).split()
        parent_tokens = self._normalize_label(parent).split()
        if not child_tokens or not parent_tokens:
            return 0.0
        return 1.0 if child_tokens[-1] == parent_tokens[-1] else 0.0

    def _head_token_overlap_score(self, child: str, parent: str) -> float:
        """Measure the proportion of child tokens shared with a parent."""
        child_tokens = self._token_set(child)
        parent_tokens = self._token_set(parent)
        if not child_tokens:
            return 0.0
        return len(child_tokens & parent_tokens) / len(child_tokens)

    def _build_parent_prior(self, train_edges):
        """Compute parent label frequencies from source-domain taxonomy edges."""
        parent_counts = Counter(parent for _, parent in train_edges)
        total = sum(parent_counts.values()) or 1
        return {parent: count / total for parent, count in parent_counts.items()}

### Candidate Generation and Feature Extraction ##############################

    def _collect_rewrite_parent_candidates(self, label: str, label_set: set[str]) -> dict[str, float]:
        """
        Generate existing target labels that can parent a rewritten label.

        Candidates are admitted only when their normalized form occurs in the
        current target label inventory. Rewrite bonuses follow the original
        Volt-IQ suffix, phrase, and regulation rules.

        Args:
            label: Child label for which parent candidates are generated.
            label_set: Normalized labels allowed in the target taxonomy.

        Returns:
            Dictionary mapping candidate parent labels to rewrite bonuses.
        """
        label_norm = self._normalize_label(label)
        token_list = label_norm.split()
        candidates: dict[str, float] = {}

        def add(candidate: str, bonus: float) -> None:
            candidate_norm = self._normalize_label(candidate)
            if not candidate_norm or candidate_norm == label_norm or candidate_norm not in label_set:
                return
            candidates[candidate_norm] = max(candidates.get(candidate_norm, -1.0), bonus)

        if label_norm.startswith("positive regulation of "):
            remainder = label_norm[len("positive regulation of "):]
            add(f"regulation of {remainder}", 3.2)
            add(remainder, 1.0)
        if label_norm.startswith("negative regulation of "):
            remainder = label_norm[len("negative regulation of "):]
            add(f"regulation of {remainder}", 3.2)
            add(remainder, 1.0)
        if " of " in label_norm:
            add(label_norm.split(" of ")[0], 2.6)
        if " by " in label_norm:
            add(label_norm.split(" by ")[0], 2.5)
        if " involved in " in label_norm:
            add(label_norm.split(" involved in ")[0], 2.2)
        if "," in label_norm:
            add(label_norm.replace(",", ""), 1.4)

        for suffix, replacement, bonus in self.REWRITE_SUFFIX_RULES:
            if label_norm.endswith(suffix):
                add(label_norm[: -len(suffix)] + replacement, bonus)

        for cut in range(1, min(4, len(token_list))):
            add(" ".join(token_list[cut:]), 1.8 - (0.2 * cut))
            add(" ".join(token_list[:-cut]), 1.6 - (0.2 * cut))

        for width in range(len(token_list) - 1, 0, -1):
            for start in range(0, len(token_list) - width + 1):
                add(" ".join(token_list[start:start + width]), 1.0 + (width / max(1, len(token_list))))
            if candidates:
                break

        return candidates

    def _build_rewrite_candidate_pool(self, train_edges, test_types, top_k_per_child=16, target_children=None):
        """
        Build and rank candidate parent pairs for rewrite-based induction.

        The pool uses lexical rewrites, token/suffix indexes, parent priors,
        and a bounded number of candidates per child.

        Args:
            train_edges: Source-domain (child, parent) relations.
            test_types: Target-domain type labels.
            top_k_per_child: Maximum number of candidate pairs per child.
            target_children: Optional subset of labels that still need parents.

        Returns:
            Candidate (child, parent) pairs and their feature dictionaries.
        """
        parent_prior = self._build_parent_prior(train_edges)
        normalized_test = sorted({self._normalize_label(item) for item in test_types if self._normalize_label(item)})
        label_set = set(normalized_test)
        normalized_target_children = (
            sorted({self._normalize_label(item) for item in target_children if self._normalize_label(item)})
            if target_children is not None
            else normalized_test
        )
        tokens_by_label = {label: set(label.split()) for label in normalized_test}
        token_list_by_label = {label: label.split() for label in normalized_test}
        suffix_by_label = {
            label: (token_list_by_label[label][-1] if token_list_by_label[label] else "")
            for label in normalized_test
        }
        token_to_labels = defaultdict(set)
        suffix_to_labels = defaultdict(set)
        for label in normalized_test:
            for token in tokens_by_label[label]:
                token_to_labels[token].add(label)
            if suffix_by_label[label]:
                suffix_to_labels[suffix_by_label[label]].add(label)

        # Use frequent source parents only when lexical candidates are unavailable.
        fallback_parents = sorted(
            normalized_test,
            key=lambda item: (-parent_prior.get(item, 0.0), len(item.split()), item),
        )[:32]

        candidate_pairs = []
        feature_rows = {}
        for child in normalized_target_children:
            child_tokens = tokens_by_label[child]
            child_tokens_list = token_list_by_label[child]
            child_suffix = suffix_by_label[child]
            candidate_parents = self._collect_rewrite_parent_candidates(child, label_set)

            if child_suffix:
                suffix_candidates = [
                    parent
                    for parent in suffix_to_labels.get(child_suffix, set())
                    if parent != child and len(token_list_by_label[parent]) <= len(child_tokens_list)
                ]
                suffix_candidates.sort(
                    key=lambda parent: (
                        -(len(tokens_by_label[parent] & child_tokens)),
                        len(token_list_by_label[parent]),
                        -parent_prior.get(parent, 0.0),
                        parent,
                    )
                )
                for parent in suffix_candidates[: top_k_per_child * 2]:
                    candidate_parents[parent] = max(candidate_parents.get(parent, 0.0), 0.4)

            if child_tokens:
                rare_tokens = sorted(
                    child_tokens,
                    key=lambda token: (len(token_to_labels.get(token, ())), token),
                )[:2]
                for rare_token in rare_tokens:
                    token_candidates = [
                        parent
                        for parent in token_to_labels.get(rare_token, set())
                        if parent != child and len(token_list_by_label[parent]) <= len(child_tokens_list)
                    ]
                    token_candidates.sort(
                        key=lambda parent: (
                            -(len(tokens_by_label[parent] & child_tokens)),
                            len(token_list_by_label[parent]),
                            -parent_prior.get(parent, 0.0),
                            parent,
                        )
                    )
                    for parent in token_candidates[:top_k_per_child]:
                        candidate_parents[parent] = max(candidate_parents.get(parent, 0.0), 0.0)

            if not candidate_parents:
                for parent in fallback_parents:
                    if parent != child and len(parent.split()) <= len(child_tokens_list):
                        candidate_parents[parent] = 0.0

            scored_rows = []
            for parent, rewrite_bonus in candidate_parents.items():
                if parent == child:
                    continue
                parent_tokens = tokens_by_label[parent]
                token_union = child_tokens | parent_tokens
                token_intersection = child_tokens & parent_tokens
                child_len = max(1, len(child_tokens_list))
                parent_len = max(1, len(token_list_by_label[parent]))
                char_proxy = 0.0
                if parent in child or child in parent:
                    char_proxy = min(len(parent), len(child)) / max(len(parent), len(child))
                elif token_union:
                    char_proxy = len(token_intersection) / len(token_union)
                features = {
                    "head_token_overlap": len(token_intersection) / child_len,
                    "suffix_match": 1.0 if child_suffix and child_suffix == suffix_by_label[parent] else 0.0,
                    "char_jaccard": char_proxy,
                    "token_jaccard": len(token_intersection) / len(token_union) if token_union else 0.0,
                    "parent_prior": parent_prior.get(parent, 0.0),
                    "child_len": float(child_len),
                    "parent_len": float(parent_len),
                    "rewrite_bonus": rewrite_bonus,
                }
                if (
                    features["head_token_overlap"] == 0
                    and features["suffix_match"] == 0
                    and features["char_jaccard"] < 0.18
                    and rewrite_bonus <= 0.0
                ):
                    continue
                base_score = (
                    1.8 * features["head_token_overlap"]
                    + 1.3 * features["suffix_match"]
                    + 0.7 * features["char_jaccard"]
                    + 0.6 * features["token_jaccard"]
                    + 0.5 * features["parent_prior"]
                    + 0.9 * rewrite_bonus
                )
                features["_base_score"] = base_score
                feature_rows[(child, parent)] = features
                scored_rows.append((child, parent, base_score))
            scored_rows.sort(key=lambda item: (-item[2], item[1]))
            candidate_pairs.extend((child_name, parent_name) for child_name, parent_name, _ in scored_rows[:top_k_per_child])
        return candidate_pairs, feature_rows

    def _score_rewrite_edges(self, candidate_edges, feature_rows):
        """Score rewrite candidates using Volt-IQ's weighted lexical features."""
        scored = []
        for child, parent, base_score in candidate_edges:
            features = feature_rows[(child, parent)]
            score = (
                1.8 * features["head_token_overlap"]
                + 1.4 * features["suffix_match"]
                + 0.8 * features["char_jaccard"]
                + 0.8 * features["token_jaccard"]
                + 0.6 * features["parent_prior"]
                + 1.6 * features.get("rewrite_bonus", 0.0)
                - 0.05 * features["parent_len"]
                + 0.2 * base_score
            )
            scored.append((child, parent, score))
        return scored

    def _build_training_examples(self, train_edges, train_types, negative_ratio=3):
        """
        Build positive and sampled negative parent-child examples.

        The TF-IDF pair classifier uses source taxonomy edges as positive
        examples and draws other candidate parents as negatives.

        Args:
            train_edges: Source-domain (child, parent) relations.
            train_types: Source-domain type labels.
            negative_ratio: Maximum number of negatives per positive relation.

        Returns:
            Feature rows, binary labels, and paired-label training texts.
        """
        parent_prior = self._build_parent_prior(train_edges)
        positive_pairs = set(train_edges)
        all_types = sorted({self._normalize_label(item) for item in train_types if self._normalize_label(item)})
        X = []
        y = []
        pair_texts = []
        for child, parent in sorted(positive_pairs):
            X.append(self._extract_pair_features(child, parent, parent_prior))
            y.append(1)
            pair_texts.append(f"{self._normalize_label(child)} [SEP] {self._normalize_label(parent)}")
            negatives_added = 0
            for candidate_parent in all_types:
                if candidate_parent == child or (child, candidate_parent) in positive_pairs:
                    continue
                X.append(self._extract_pair_features(child, candidate_parent, parent_prior))
                y.append(0)
                pair_texts.append(f"{self._normalize_label(child)} [SEP] {self._normalize_label(candidate_parent)}")
                negatives_added += 1
                if negatives_added >= negative_ratio:
                    break
        return X, y, pair_texts

    def _extract_pair_features(self, child: str, parent: str, parent_prior: dict[str, float]):
        """Extract lexical overlap, length, and source-parent prior features."""
        return {
            "head_token_overlap": self._head_token_overlap_score(child, parent),
            "suffix_match": self._suffix_match_score(child, parent),
            "char_jaccard": self._jaccard(self._char_3grams(child), self._char_3grams(parent)),
            "token_jaccard": self._jaccard(self._token_set(child), self._token_set(parent)),
            "parent_prior": parent_prior.get(parent, 0.0),
            "child_len": math.log1p(len(self._normalize_label(child).split())),
            "parent_len": math.log1p(len(self._normalize_label(parent).split())),
        }

    def _feature_matrix(self, feature_dicts):
        """Convert feature dictionaries to a consistently ordered matrix."""
        names = sorted(feature_dicts[0]) if feature_dicts else []
        return [[row[name] for name in names] for row in feature_dicts], names

    def _build_sparse_candidate_pool(self, train_edges, train_types, test_types, top_k_per_child=12):
        """
        Build a sparse parent-child candidate pool from target labels.

        Proper subphrases, matching suffixes, and shared tokens narrow the
        candidate search before scoring. Source parent frequencies contribute
        a ranking prior.

        Args:
            train_edges: Source-domain (child, parent) relations.
            train_types: Source-domain type labels (not used by this pool).
            test_types: Target-domain type labels.
            top_k_per_child: Maximum number of candidates retained per child.

        Returns:
            Candidate (child, parent) pairs and their feature dictionaries.
        """
        del train_types
        parent_prior = self._build_parent_prior(train_edges)
        normalized_test = sorted({self._normalize_label(item) for item in test_types if self._normalize_label(item)})
        label_set = set(normalized_test)
        token_to_parents = defaultdict(set)
        suffix_to_parents = defaultdict(set)
        for parent in normalized_test:
            tokens = self._token_set(parent)
            for token in tokens:
                token_to_parents[token].add(parent)
            parent_tokens = parent.split()
            if parent_tokens:
                suffix_to_parents[parent_tokens[-1]].add(parent)

        fallback_parents = [parent for parent, _ in sorted(parent_prior.items(), key=lambda item: (-item[1], item[0]))[:32]]
        feature_rows = {}
        candidate_pairs = []
        for child in normalized_test:
            child_tokens_list = child.split()
            child_tokens = set(child_tokens_list)
            child_suffix = child_tokens_list[-1] if child_tokens_list else ""
            candidate_parents = set()

            # Prefer exact subphrases of the child label that already exist in the target label set.
            token_count = len(child_tokens_list)
            for width in range(token_count - 1, 0, -1):
                for start in range(0, token_count - width + 1):
                    phrase = " ".join(child_tokens_list[start:start + width])
                    if phrase in label_set and phrase != child:
                        candidate_parents.add(phrase)
                if len(candidate_parents) >= max(top_k_per_child * 2, 8):
                    break

            # Back off to shorter labels sharing the same suffix token.
            if child_suffix:
                suffix_candidates = [
                    parent for parent in suffix_to_parents.get(child_suffix, set())
                    if parent != child and len(parent.split()) <= len(child_tokens_list)
                ]
                suffix_candidates.sort(
                    key=lambda parent: (
                        -(len(self._token_set(parent) & child_tokens)),
                        len(child_tokens_list) - len(parent.split()),
                        -parent_prior.get(parent, 0.0),
                        parent,
                    )
                )
                candidate_parents.update(suffix_candidates[:24])

            # Use the rarest child token to avoid exploding on very common words.
            if child_tokens:
                rare_token = min(child_tokens, key=lambda token: (len(token_to_parents.get(token, ())), token))
                token_candidates = [
                    parent for parent in token_to_parents.get(rare_token, set())
                    if parent != child and len(parent.split()) <= len(child_tokens_list)
                ]
                token_candidates.sort(
                    key=lambda parent: (
                        -(len(self._token_set(parent) & child_tokens)),
                        len(child_tokens_list) - len(parent.split()),
                        -parent_prior.get(parent, 0.0),
                        parent,
                    )
                )
                candidate_parents.update(token_candidates[:24])

            if not candidate_parents:
                candidate_parents.update(parent for parent in fallback_parents if parent != child)

            scored_pairs = []
            for parent in candidate_parents:
                if child == parent:
                    continue
                features = self._extract_pair_features(child, parent, parent_prior)
                feature_rows[(child, parent)] = features
                if (
                    features["head_token_overlap"] == 0
                    and features["suffix_match"] == 0
                    and features["char_jaccard"] < 0.22
                ):
                    continue
                base_score = (
                    1.5 * features["head_token_overlap"]
                    + 1.2 * features["suffix_match"]
                    + 0.8 * features["char_jaccard"]
                    + 0.5 * features["token_jaccard"]
                    + 0.5 * features["parent_prior"]
                )
                if base_score <= 0:
                    continue
                scored_pairs.append((child, parent, base_score))
            scored_pairs.sort(key=lambda item: (-item[2], item[1]))
            for child_name, parent_name, base_score in scored_pairs[:top_k_per_child]:
                feature_rows[(child_name, parent_name)]["_base_score"] = base_score
                candidate_pairs.append((child_name, parent_name))
        return candidate_pairs, feature_rows

### Taxonomy Induction and Prediction ########################################

    def _build_substring_heuristic_taxonomy(self, test_types, train_edges):
        """
        Select the longest proper target-label subphrases as parents.

        The method uses a suffix/prefix preference and source-parent prior
        when ranking subphrases. Each parent is shorter than its child, so
        selected edges cannot form a cycle.

        Args:
            test_types: Target-domain labels.
            train_edges: Source-domain taxonomy edges.

        Returns:
            Predicted (child, parent) relations.
        """
        parent_prior = self._build_parent_prior(train_edges)
        normalized_test = sorted({self._normalize_label(item) for item in test_types if self._normalize_label(item)})
        label_set = set(normalized_test)
        chosen = []
        for child in normalized_test:
            tokens = child.split()
            if len(tokens) < 2:
                continue
            candidates = []
            for width in range(len(tokens) - 1, 0, -1):
                for start in range(0, len(tokens) - width + 1):
                    parent = " ".join(tokens[start:start + width])
                    if parent == child or parent not in label_set:
                        continue
                    overlap_ratio = width / len(tokens)
                    suffix_bonus = 1.0 if start + width == len(tokens) else 0.0
                    prefix_bonus = 0.5 if start == 0 else 0.0
                    score = 3.0 * overlap_ratio + suffix_bonus + prefix_bonus + parent_prior.get(parent, 0.0)
                    candidates.append((child, parent, score))
                if candidates:
                    break
            if not candidates:
                continue
            candidates.sort(key=lambda item: (-item[2], item[1]))
            chosen.append(candidates[0])
        # Parent is always a proper subphrase, so edges are length-decreasing and acyclic.
        return [(child, parent) for child, parent, _ in chosen]

    def _predict_taxonomy_discovery_edges_for_labels(self, *, train_edges, train_types, test_types, method="hybrid_cascade"):
        """
        Route target labels to the selected Volt-IQ taxonomy method.

        Args:
            train_edges: Source-domain taxonomy relations.
            train_types: Source-domain type labels.
            test_types: Target-domain labels.
            method: Taxonomy induction method.

        Returns:
            Predicted (child, parent) relations.
        """
        if method == "substring_heuristic":
            return self._build_substring_heuristic_taxonomy(test_types=test_types, train_edges=train_edges)
        if method == "rewrite_cascade":
            candidate_pairs, feature_rows = self._build_rewrite_candidate_pool(
                train_edges,
                test_types,
                top_k_per_child=16,
            )
            candidate_edges = [
                (child, parent, feature_rows[(child, parent)].get("_base_score", 0.0))
                for child, parent in candidate_pairs
            ]
            expected_edge_count = max(1, len({self._normalize_label(item) for item in test_types if self._normalize_label(item)}) - 1)
            return self._baseline_rewrite_cascade(candidate_edges, feature_rows, expected_edge_count)

        candidate_pairs, feature_rows = self._build_sparse_candidate_pool(
            train_edges,
            train_types,
            test_types,
            top_k_per_child=12,
        )
        candidate_edges = [
            (child, parent, feature_rows[(child, parent)].get("_base_score", 0.0))
            for child, parent in candidate_pairs
        ]
        expected_edge_count = max(1, len({self._normalize_label(item) for item in test_types if self._normalize_label(item)}) - 1)
        if method == "lexical_subsumption":
            return self._baseline_lexical_subsumption(candidate_edges, feature_rows, expected_edge_count)
        if method == "parent_prior":
            return self._baseline_parent_prior(candidate_edges, feature_rows, expected_edge_count)
        if method == "tfidf_pair_linear":
            return self._baseline_tfidf_linear(train_edges, train_types, candidate_edges, feature_rows, expected_edge_count)
        return self._baseline_hybrid_cascade(candidate_edges, feature_rows, expected_edge_count)

    def _baseline_lexical_subsumption(self, candidate_edges, feature_rows, expected_edge_count):
        """Rank taxonomy candidates using lexical subsumption features."""
        scored = []
        for child, parent, _ in candidate_edges:
            features = feature_rows[(child, parent)]
            score = (
                2.5 * features["head_token_overlap"]
                + 2.0 * features["suffix_match"]
                + 1.0 * features["token_jaccard"]
                + 0.5 * features["char_jaccard"]
            )
            scored.append((child, parent, score))
        return self._select_predicted_edges(
            scored_edges=scored,
            expected_edge_count=expected_edge_count,
            max_parents_per_child=1,
        )

    def _baseline_parent_prior(self, candidate_edges, feature_rows, expected_edge_count):
        """Rank taxonomy candidates using source-parent frequencies."""
        scored = []
        for child, parent, _ in candidate_edges:
            features = feature_rows[(child, parent)]
            score = (
                1.5 * features["parent_prior"]
                + 1.0 * features["suffix_match"]
                + 0.5 * features["head_token_overlap"]
            )
            scored.append((child, parent, score))
        return self._select_predicted_edges(
            scored_edges=scored,
            expected_edge_count=expected_edge_count,
            max_parents_per_child=1,
        )

    def _baseline_tfidf_linear(self, train_edges, train_types, candidate_edges, feature_rows, expected_edge_count):
        """
        Fit a TF-IDF pair classifier and rank target candidate edges.

        This optional method trains a logistic regression classifier on
        source-domain positive and negative parent-child pairs during inference.

        Args:
            train_edges: Source-domain taxonomy relations.
            train_types: Source-domain labels.
            candidate_edges: Candidate (child, parent, score) tuples.
            feature_rows: Precomputed candidate features.
            expected_edge_count: Maximum number of selected edges.

        Returns:
            Predicted (child, parent) relations.
        """
        from scipy import sparse
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression

        parent_prior = self._build_parent_prior(train_edges)
        feature_dicts, labels, pair_texts = self._build_training_examples(train_edges, train_types)
        dense_matrix, feature_names = self._feature_matrix(feature_dicts)
        vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), min_df=1)
        tfidf_matrix = vectorizer.fit_transform(pair_texts)
        import numpy as np

        X_dense = sparse.csr_matrix(np.asarray(dense_matrix, dtype=float))
        X = sparse.hstack([X_dense, tfidf_matrix], format="csr")
        model = LogisticRegression(max_iter=1000, random_state=42)
        model.fit(X, labels)

        scored = []
        for child, parent, base_score in candidate_edges:
            features = feature_rows[(child, parent)]
            dense_row = sparse.csr_matrix([[features[name] for name in feature_names]])
            pair_text = [f"{child} [SEP] {parent}"]
            tfidf_row = vectorizer.transform(pair_text)
            row = sparse.hstack([dense_row, tfidf_row], format="csr")
            score = float(model.predict_proba(row)[0][1]) + 0.15 * base_score
            scored.append((child, parent, score))
        return self._select_predicted_edges(
            scored_edges=scored,
            expected_edge_count=expected_edge_count,
            max_parents_per_child=1,
        )

    def _baseline_hybrid_cascade(self, candidate_edges, feature_rows, expected_edge_count):
        """Rank candidate edges using Volt-IQ's combined lexical and prior scores."""
        scored = []
        for child, parent, _ in candidate_edges:
            features = feature_rows[(child, parent)]
            score = (
                1.8 * features["head_token_overlap"]
                + 1.2 * features["suffix_match"]
                + 0.8 * features["char_jaccard"]
                + 0.6 * features["token_jaccard"]
                + 0.8 * features["parent_prior"]
            )
            scored.append((child, parent, score))
        return self._select_predicted_edges(
            scored_edges=scored,
            expected_edge_count=expected_edge_count,
            max_parents_per_child=1,
        )

    def _baseline_rewrite_cascade(self, candidate_edges, feature_rows, expected_edge_count):
        """Apply rewrite scores and select non-cyclic parent-child relations."""
        return self._select_predicted_edges(
            scored_edges=self._score_rewrite_edges(candidate_edges, feature_rows),
            expected_edge_count=expected_edge_count,
            max_parents_per_child=1,
        )

### Ontology Resource Loading ################################################

    def _ensure_go_basic_obo_cached(self, ) -> Path:
        """Download GO Basic OBO on first use and reuse its local cache."""
        self.TAXONOMY_DISCOVERY_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        if self.GO_BASIC_OBO_PATH.exists():
            return self.GO_BASIC_OBO_PATH
        request = urllib.request.Request(self.GO_BASIC_OBO_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=120) as response:
            self.GO_BASIC_OBO_PATH.write_bytes(response.read())
        return self.GO_BASIC_OBO_PATH

    def _write_go_basic_index(self, index: dict[str, dict[str, list[str]] | dict[str, str]]) -> None:
        """Write the parsed GO label and direct-parent index to cache."""
        self.TAXONOMY_DISCOVERY_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        self.GO_BASIC_INDEX_PATH.write_text(json.dumps(index, ensure_ascii=True), encoding="utf-8")

    def _build_go_basic_index_from_obo(self, obo_path: Path) -> dict[str, dict[str, list[str]] | dict[str, str]]:
        """
        Parse GO Basic labels, synonyms, and direct is-a parent links.

        Obsolete terms are excluded from the cached index.

        Args:
            obo_path: Path to the GO Basic OBO file.

        Returns:
            Lookup dictionaries for labels, synonyms, identifiers, and parents.
        """
        name_to_ids: dict[str, list[str]] = defaultdict(list)
        synonym_to_ids: dict[str, list[str]] = defaultdict(list)
        id_to_name: dict[str, str] = {}
        id_to_parents: dict[str, list[str]] = {}
        id_to_synonyms: dict[str, list[str]] = {}

        current_id = None
        current_name = None
        current_parents: list[str] = []
        current_synonyms: list[str] = []
        is_obsolete = False

        def flush_term() -> None:
            if not current_id or not current_name or is_obsolete:
                return
            normalized_name = self._normalize_label(current_name)
            id_to_name[current_id] = normalized_name
            id_to_parents[current_id] = list(current_parents)
            normalized_synonyms = [self._normalize_label(item) for item in current_synonyms if self._normalize_label(item)]
            id_to_synonyms[current_id] = normalized_synonyms
            if normalized_name:
                name_to_ids[normalized_name].append(current_id)
            for synonym in normalized_synonyms:
                synonym_to_ids[synonym].append(current_id)

        for raw_line in obo_path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw_line.strip()
            if line == "[Term]":
                flush_term()
                current_id = None
                current_name = None
                current_parents = []
                current_synonyms = []
                is_obsolete = False
                continue
            if line.startswith("["):
                flush_term()
                current_id = None
                current_name = None
                current_parents = []
                current_synonyms = []
                is_obsolete = False
                continue
            if line.startswith("id: "):
                current_id = line[4:].strip()
            elif line.startswith("name: "):
                current_name = line[6:].strip()
            elif line.startswith("is_a: "):
                current_parents.append(line.split()[1])
            elif line.startswith("synonym: "):
                match = re.match(r'synonym: "(.+?)"\s', line)
                if match:
                    current_synonyms.append(match.group(1))
            elif line == "is_obsolete: true":
                is_obsolete = True
        flush_term()

        return {
            "name_to_ids": dict(name_to_ids),
            "synonym_to_ids": dict(synonym_to_ids),
            "id_to_name": id_to_name,
            "id_to_parents": id_to_parents,
            "id_to_synonyms": id_to_synonyms,
        }

    @lru_cache(maxsize=1)
    def _load_go_basic_index(self, ) -> dict[str, dict[str, list[str]] | dict[str, str]]:
        """Load the GO index from cache, or build it from the OBO source."""
        if self.GO_BASIC_INDEX_PATH.exists():
            with self.GO_BASIC_INDEX_PATH.open("r", encoding="utf-8") as handle:
                return json.load(handle)
        obo_path = self._ensure_go_basic_obo_cached()
        index = self._build_go_basic_index_from_obo(obo_path)
        self._write_go_basic_index(index)
        return index

    def _go_parent_labels_for_id(
        self,
        go_id: str,
        *,
        label_set: set[str],
        id_to_name: dict[str, str],
        id_to_synonyms: dict[str, list[str]],
    ) -> list[str]:
        """
        Resolve GO parent labels present in the target vocabulary.

        Args:
            go_id: Parent GO identifier.
            label_set: Normalized target labels allowed in the prediction.
            id_to_name: GO identifier-to-label lookup.
            id_to_synonyms: GO identifier-to-synonym lookup.

        Returns:
            Matching target-domain labels for the parent identifier.
        """
        labels = []
        canonical_name = id_to_name.get(go_id)
        if canonical_name and canonical_name in label_set:
            labels.append(canonical_name)
        for synonym in id_to_synonyms.get(go_id, []):
            if synonym in label_set and synonym not in labels:
                labels.append(synonym)
        return labels

    def _ensure_obo_source_cached(self, source_key: str) -> Path:
        """Download an OBO ontology on first use and return its cache path."""
        if source_key == "go":
            return self._ensure_go_basic_obo_cached()
        if source_key not in self.OBO_SOURCE_URLS:
            raise ValueError(f"Unknown OBO source: {source_key}")
        self.OBO_PROBE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path = self.OBO_PROBE_CACHE_DIR / f"{source_key}.obo"
        if path.exists():
            return path
        request = urllib.request.Request(self.OBO_SOURCE_URLS[source_key], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=120) as response:
            path.write_bytes(response.read())
        return path

    @lru_cache(maxsize=None)
    def _load_obo_source_terms(self, source_key: str):
        """
        Parse OBO term identifiers, names, synonyms, and direct parents.

        Args:
            source_key: Key of a configured public OBO resource.

        Returns:
            Cached tuple of non-obsolete term records.
        """
        path = self._ensure_obo_source_cached(source_key)
        terms = []
        current_id = None
        current_name = None
        current_parents: list[str] = []
        current_synonyms: list[str] = []
        is_obsolete = False
        in_term = False

        def flush_term() -> None:
            if not current_id or not current_name or is_obsolete:
                return
            terms.append(
                {
                    "id": current_id,
                    "name": self._normalize_label(current_name),
                    "parents": list(current_parents),
                    "synonyms": [self._normalize_label(item) for item in current_synonyms if self._normalize_label(item)],
                }
            )

        for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw_line.strip()
            if line == "[Term]":
                flush_term()
                current_id = None
                current_name = None
                current_parents = []
                current_synonyms = []
                is_obsolete = False
                in_term = True
                continue
            if line.startswith("["):
                flush_term()
                current_id = None
                current_name = None
                current_parents = []
                current_synonyms = []
                is_obsolete = False
                in_term = False
                continue
            if not in_term:
                continue
            if line.startswith("id: "):
                current_id = line[4:].strip()
            elif line.startswith("name: "):
                current_name = line[6:].strip()
            elif line.startswith("is_a: "):
                current_parents.append(line.split()[1])
            elif line.startswith("synonym: "):
                match = re.match(r'synonym: "(.+?)"\s', line)
                if match:
                    current_synonyms.append(match.group(1))
            elif line == "is_obsolete: true":
                is_obsolete = True
        flush_term()
        return tuple(terms)

    def _ensure_owl_source_cached(self, source_key: str) -> Path:
        """Download an OWL ontology on first use and return its cache path."""
        if source_key not in self.TAXONOMY_DISCOVERY_OWL_SOURCE_URLS:
            raise ValueError(f"Unknown OWL source: {source_key}")
        self.OWL_PROBE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path = self.OWL_PROBE_CACHE_DIR / f"{source_key}.owl"
        if path.exists() and path.stat().st_size > 0:
            return path
        request = urllib.request.Request(self.TAXONOMY_DISCOVERY_OWL_SOURCE_URLS[source_key], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=180) as response:
            path.write_bytes(response.read())
        return path

    @lru_cache(maxsize=None)
    def _load_owl_source_terms(self, source_key: str):
        """
        Parse OWL labels, synonyms, and direct subclass links.

        Only resource-backed classes with labels are indexed. The method
        keeps identifier-based parent links for later target-label matching.

        Args:
            source_key: Key of a configured public OWL resource.

        Returns:
            Cached tuple of ontology term records.
        """
        try:
            import rdflib
            from rdflib import URIRef
        except ImportError as exc:  # pragma: no cover - dependency is provided by OntoLearner
            raise RuntimeError("rdflib is required to parse Taxonomy discovery OWL sources.") from exc

        owl_path = self._ensure_owl_source_cached(source_key)
        graph = rdflib.Graph()
        graph.parse(str(owl_path), format="xml")
        label_predicates = {
            rdflib.namespace.RDFS.label,
            URIRef(f"{self.OBO_IN_OWL_PREFIX}hasExactSynonym"),
            URIRef(f"{self.OBO_IN_OWL_PREFIX}hasRelatedSynonym"),
            URIRef(f"{self.OBO_IN_OWL_PREFIX}hasBroadSynonym"),
        }
        labels_by_uri: dict[str, list[str]] = defaultdict(list)
        parent_uris: dict[str, list[str]] = defaultdict(list)

        for subject, predicate, object_value in graph.triples((None, None, None)):
            if predicate in label_predicates and isinstance(subject, URIRef):
                label = self._normalize_label(str(object_value))
                subject_id = str(subject)
                if label and label not in labels_by_uri[subject_id]:
                    labels_by_uri[subject_id].append(label)
        for subject, object_value in graph.subject_objects(rdflib.namespace.RDFS.subClassOf):
            if isinstance(subject, URIRef) and isinstance(object_value, URIRef):
                parent_uris[str(subject)].append(str(object_value))

        return tuple(
            {
                "id": term_id,
                "labels": tuple(labels),
                "parents": tuple(parent_uris.get(term_id, [])),
            }
            for term_id, labels in labels_by_uri.items()
        )

### Ontology-Backed Taxonomy Prediction ######################################

    def _predict_obo_backfilled_edges(
        self,
        *,
        train_edges,
        test_types,
        source_keys=None,
        include_rewrite_fallback=True,
        include_owl_sources=False,
        owl_source_keys=None,
    ):
        """
        Recover direct taxonomy parents from OBO/OWL resources.

        Both child and parent must match labels in the target inventory. For
        children without an ontology-backed edge, the optional rewrite fallback
        adds at most one ranked lexical parent.

        Args:
            train_edges: Source-domain taxonomy edges used for lexical priors.
            test_types: Target-domain type labels.
            source_keys: OBO sources to check, or all configured sources.
            include_rewrite_fallback: Whether to add lexical fallback parents.
            include_owl_sources: Whether to search the configured OWL sources.
            owl_source_keys: OWL sources to check, or all configured sources.

        Returns:
            Predicted (child, parent) relations.
        """
        source_keys = self.TAXONOMY_DISCOVERY_OBO_SOURCE_KEYS if source_keys is None else source_keys
        owl_source_keys = self.TAXONOMY_DISCOVERY_OWL_SOURCE_KEYS if owl_source_keys is None else owl_source_keys
        normalized_test = sorted({self._normalize_label(item) for item in test_types if self._normalize_label(item)})
        label_set = set(normalized_test)
        source_edges = []
        matched_children = set()

        # Recover only ontology edges whose endpoints occur in target labels.
        for source_key in source_keys:
            terms = self._load_obo_source_terms(source_key)
            id_to_labels = {}
            id_to_parents = {}
            for term in terms:
                labels = []
                if term["name"] in label_set:
                    labels.append(term["name"])
                labels.extend(synonym for synonym in term["synonyms"] if synonym in label_set and synonym not in labels)
                if labels:
                    id_to_labels[term["id"]] = labels
                id_to_parents[term["id"]] = term["parents"]
            for term_id, child_labels in id_to_labels.items():
                child_edges = set()
                for parent_id in id_to_parents.get(term_id, []):
                    for parent_label in id_to_labels.get(parent_id, []):
                        for child_label in child_labels:
                            if child_label != parent_label:
                                child_edges.add((child_label, parent_label))
                if child_edges:
                    source_edges.extend(sorted(child_edges))
                    matched_children.update(child for child, _ in child_edges)

        # OWL labels and direct subclass links complement the OBO sources.
        if include_owl_sources:
            for source_key in owl_source_keys:
                terms = self._load_owl_source_terms(source_key)
                id_to_labels = {}
                id_to_parents = {}
                for term in terms:
                    labels = [label for label in term["labels"] if label in label_set]
                    if labels:
                        id_to_labels[term["id"]] = labels
                    id_to_parents[term["id"]] = term["parents"]
                for term_id, child_labels in id_to_labels.items():
                    child_edges = set()
                    for parent_id in id_to_parents.get(term_id, []):
                        for parent_label in id_to_labels.get(parent_id, []):
                            for child_label in child_labels:
                                if child_label != parent_label:
                                    child_edges.add((child_label, parent_label))
                    if child_edges:
                        source_edges.extend(sorted(child_edges))
                        matched_children.update(child for child, _ in child_edges)

        selected_edges = self._dedupe_taxonomy_edges(source_edges)
        if not include_rewrite_fallback:
            return selected_edges

        children_with_parents = {child for child, _ in selected_edges}
        # Backfill children that have no direct ontology-supported parent.
        fallback_children = set(normalized_test) - matched_children
        rewrite_candidate_pairs, rewrite_feature_rows = self._build_rewrite_candidate_pool(
            train_edges,
            normalized_test,
            top_k_per_child=16,
            target_children=fallback_children,
        )
        rewrite_candidate_edges = [
            (child, parent, rewrite_feature_rows[(child, parent)].get("_base_score", 0.0))
            for child, parent in rewrite_candidate_pairs
        ]
        rewrite_ranked_edges = sorted(
            self._score_rewrite_edges(rewrite_candidate_edges, rewrite_feature_rows),
            key=lambda item: (-item[2], item[0], item[1]),
        )
        for child, parent, _ in rewrite_ranked_edges:
            if child not in fallback_children or child in children_with_parents:
                continue
            if len(parent.split()) > len(child.split()) and parent not in child:
                continue
            selected_edges.append((child, parent))
            children_with_parents.add(child)
        return self._dedupe_taxonomy_edges(selected_edges)

    def _predict_go_backfilled_biora_edges(self, *, train_edges, test_types, include_rewrite_fallback=True):
        """
        Recover GO direct parents with an optional rewrite fallback.

        Only parent-child matches within the Biora label inventory are
        retained. Unmatched children may receive one lexical rewrite parent.

        Args:
            train_edges: Source-domain taxonomy edges.
            test_types: Target-domain type labels.
            include_rewrite_fallback: Whether to add lexical fallback parents.

        Returns:
            Predicted (child, parent) relations.
        """
        normalized_test = sorted({self._normalize_label(item) for item in test_types if self._normalize_label(item)})
        label_set = set(normalized_test)
        go_index = self._load_go_basic_index()
        name_to_ids = go_index["name_to_ids"]
        synonym_to_ids = go_index["synonym_to_ids"]
        id_to_name = go_index["id_to_name"]
        id_to_parents = go_index["id_to_parents"]
        id_to_synonyms = go_index["id_to_synonyms"]

        go_edges = []
        matched_children = set()
        for label in normalized_test:
            candidate_ids = name_to_ids.get(label, [])
            if not candidate_ids:
                candidate_ids = synonym_to_ids.get(label, [])
            child_edges = set()
            for go_id in candidate_ids:
                for parent_id in id_to_parents.get(go_id, []):
                    for parent_label in self._go_parent_labels_for_id(
                        parent_id,
                        label_set=label_set,
                        id_to_name=id_to_name,
                        id_to_synonyms=id_to_synonyms,
                    ):
                        if parent_label != label:
                            child_edges.add((label, parent_label))
            if child_edges:
                go_edges.extend(sorted(child_edges))
                matched_children.add(label)

        selected_edges = self._dedupe_taxonomy_edges(go_edges)
        if not include_rewrite_fallback:
            return selected_edges
        children_with_parents = {child for child, _ in selected_edges}
        fallback_children = set(normalized_test) - matched_children

        rewrite_candidate_pairs, rewrite_feature_rows = self._build_rewrite_candidate_pool(
            train_edges,
            normalized_test,
            top_k_per_child=16,
            target_children=fallback_children,
        )
        rewrite_candidate_edges = [
            (child, parent, rewrite_feature_rows[(child, parent)].get("_base_score", 0.0))
            for child, parent in rewrite_candidate_pairs
        ]
        rewrite_ranked_edges = sorted(
            self._score_rewrite_edges(rewrite_candidate_edges, rewrite_feature_rows),
            key=lambda item: (-item[2], item[0], item[1]),
        )

        for child, parent, _ in rewrite_ranked_edges:
            if child not in fallback_children or child in children_with_parents:
                continue
            if len(parent.split()) > len(child.split()) and parent not in child:
                continue
            selected_edges.append((child, parent))
            children_with_parents.add(child)

        return self._dedupe_taxonomy_edges(selected_edges)