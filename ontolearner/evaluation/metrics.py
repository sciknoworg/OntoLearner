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
from typing import List, Dict, Tuple, Set, Any, Union, Callable

import networkx as nx
import numpy as np
from collections import defaultdict
from rapidfuzz import fuzz
from scipy.optimize import linear_sum_assignment

SYMMETRIC_RELATIONS = {"equivalentclass", "sameas", "disjointwith"}

def primitive_ontology_metrics(
        y_true: List[List[str]] | List[Dict[str, Any]],
        y_pred: List[List[str]] | List[Dict[str, Any]],
        fuzzy_threshold: float = 0.90,
        semantic_threshold: float = 0.90,
        embedding_model: Any = None
) -> Dict[str, Dict[str, float]]:
    """
    Compute exact, fuzzy and semantic graph similarity metrics for primitive ontology learning.

    Supports both triple lists and record-based ontology predictions.

    Args:
        y_true: Ground-truth triples or records containing reference triples.
        y_pred: Predicted triples or records containing generated triples.
        fuzzy_threshold: Minimum fuzzy similarity for triple alignment.
        semantic_threshold: Minimum semantic similarity for triple alignment.
        embedding_model: Optional sentence embedding model.

    Returns:
        Exact, fuzzy and semantic graph similarity scores.
    """
    # Extract and evaluate ontology triples from record-based inputs.
    true_records = bool(y_true) and isinstance(y_true[0], dict)
    pred_records = bool(y_pred) and isinstance(y_pred[0], dict)

    if true_records or pred_records:
        if not true_records or not pred_records:
            raise ValueError("Ground truth and predictions must use the same format.")

        target = (
            "primitive-ontology-triples"
            if "primitive-ontology-triples" in y_true[0]
            else "extended-primitive-ontology-triples"
        )

        gold_by_id = {item["id"]: item[target] for item in y_true}
        pred_by_id = {item["id"]: item[target] for item in y_pred}

        if len(gold_by_id) != len(y_true) or len(pred_by_id) != len(y_pred):
            raise ValueError("Duplicate sample identifiers in evaluation data.")

        if gold_by_id.keys() != pred_by_id.keys():
            raise ValueError("Ground-truth and prediction identifiers do not match.")

        # Reuse the embedding model across all evaluation records.
        if embedding_model is None and any(
                gold_by_id[item_id] and pred_by_id[item_id]
                for item_id in gold_by_id
        ):
            from sentence_transformers import SentenceTransformer
            embedding_model = SentenceTransformer(
                "nomic-ai/nomic-embed-text-v1.5",
                trust_remote_code=True
            )

        record_scores = [
            primitive_ontology_metrics(
                y_true=gold_by_id[item_id],
                y_pred=pred_by_id[item_id],
                fuzzy_threshold=fuzzy_threshold,
                semantic_threshold=semantic_threshold,
                embedding_model=embedding_model,
            )
            for item_id in gold_by_id
        ]

        # Average graph scores across the evaluated records.
        return {
            match_type: {
                metric: sum(
                    scores[match_type][metric] for scores in record_scores
                ) / len(record_scores)
                for metric in record_scores[0][match_type]
            }
            for match_type in ("exact_match", "semantic_match", "fuzzy_match")
        }

    TAXONOMY_RELATIONS = {"is-a"}

    def normalize(text: str) -> str:
        return " ".join(str(text).lower().strip().split())

    def normalize_triples(triples: List[List[str]]) -> List[Tuple[str, str, str]]:
        return [tuple(normalize(x) for x in triple) for triple in triples]

    def edge_f1(gold_edges: List[Tuple[str, str, str]], pred_edges: List[Tuple[str, str, str]]) -> float:
        gold_set, pred_set = set(gold_edges), set(pred_edges)
        intersection = gold_set & pred_set
        if not gold_set and not pred_set:
            return 1.0
        if not gold_set or not pred_set:
            return 0.0
        precision = len(intersection) / len(pred_set)
        recall = len(intersection) / len(gold_set)
        return 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0

    def get_neighborhood(triples: List[Tuple[str, str, str]]) -> Dict[str, Set]:
        neighborhood = defaultdict(set)
        for subject, predicate, obj in triples:
            neighborhood[subject].add(("OUT", predicate, obj))
            neighborhood[obj].add(("IN", predicate, subject))
        return neighborhood

    def neighborhood_similarity(gold, pred) -> float:
        gold_neighborhood, pred_neighborhood = get_neighborhood(gold), get_neighborhood(pred)
        scores = []
        for node in set(gold_neighborhood.keys()) | set(pred_neighborhood.keys()):
            gold_neighbors = gold_neighborhood.get(node, set())
            pred_neighbors = pred_neighborhood.get(node, set())
            union = gold_neighbors | pred_neighbors
            if not union:
                continue
            scores.append(len(gold_neighbors & pred_neighbors) / len(union))
        return sum(scores) / len(scores) if scores else 0.0

    def build_taxonomy_graph(triples: List[Tuple[str, str, str]]) -> nx.DiGraph:
        graph = nx.DiGraph()
        for subject, predicate, obj in triples:
            if predicate in TAXONOMY_RELATIONS:
                graph.add_edge(subject, obj)
        return graph

    def taxonomy_similarity(gold, pred) -> float:
        gold_graph, pred_graph = build_taxonomy_graph(gold), build_taxonomy_graph(pred)
        scores = []
        for node in set(gold_graph.nodes()) | set(pred_graph.nodes()):
            gold_relations = (
                nx.ancestors(gold_graph, node) | nx.descendants(gold_graph, node)
            ) if node in gold_graph else set()
            pred_relations = (
                nx.ancestors(pred_graph, node) | nx.descendants(pred_graph, node)
            ) if node in pred_graph else set()
            union = gold_relations | pred_relations
            if not union:
                continue
            scores.append(len(gold_relations & pred_relations) / len(union))
        return sum(scores) / len(scores) if scores else 0.0

    def graph_scores(gold, pred) -> Dict[str, float]:
        edge_score = edge_f1(gold, pred)
        neighborhood_score = neighborhood_similarity(gold, pred)
        taxonomy_score = taxonomy_similarity(gold, pred)
        return {
            "edge_f1": edge_score,
            "neighborhood_similarity": neighborhood_score,
            "taxonomy_similarity": taxonomy_score,
            "graph_similarity": (edge_score + neighborhood_score + taxonomy_score) / 3,
        }

    def triple_similarity_fuzzy(t1, t2) -> float:
        subject_score = fuzz.ratio(t1[0], t2[0]) / 100
        predicate_score = fuzz.ratio(t1[1], t2[1]) / 100
        object_score = fuzz.ratio(t1[2], t2[2]) / 100
        return (subject_score + predicate_score + object_score) / 3

    def align_triples_fuzzy(gold, pred, threshold: float):
        if not gold or not pred:
            return pred
        cost_matrix = np.zeros((len(pred), len(gold)))
        for i, predicted_triple in enumerate(pred):
            for j, gold_triple in enumerate(gold):
                cost_matrix[i, j] = 1.0 - triple_similarity_fuzzy(predicted_triple, gold_triple)
        row_indices, col_indices = linear_sum_assignment(cost_matrix)
        aligned = list(pred)
        for row, col in zip(row_indices, col_indices):
            if 1.0 - cost_matrix[row, col] >= threshold:
                aligned[row] = gold[col]
        return aligned

    def build_embeddings(gold, pred, model) -> Dict[str, np.ndarray]:
        terms = set()
        for triple in gold + pred:
            terms.update(triple)
        terms = sorted(terms)
        if not terms:
            return {}
        vectors = model.encode(
            terms, normalize_embeddings=True, convert_to_numpy=True
        )
        return dict(zip(terms, vectors))

    def triple_similarity_semantic(t1, t2, embeddings) -> float:
        subject_score = np.dot(embeddings[t1[0]], embeddings[t2[0]])
        predicate_score = np.dot(embeddings[t1[1]], embeddings[t2[1]])
        object_score = np.dot(embeddings[t1[2]], embeddings[t2[2]])
        return float((subject_score + predicate_score + object_score) / 3)

    def align_triples_semantic(gold, pred, embeddings, threshold: float):
        if not gold or not pred:
            return pred
        cost_matrix = np.zeros((len(pred), len(gold)))
        for i, predicted_triple in enumerate(pred):
            for j, gold_triple in enumerate(gold):
                cost_matrix[i, j] = 1.0 - triple_similarity_semantic(
                    predicted_triple, gold_triple, embeddings
                )
        row_indices, col_indices = linear_sum_assignment(cost_matrix)
        aligned = list(pred)
        for row, col in zip(row_indices, col_indices):
            if 1.0 - cost_matrix[row, col] >= threshold:
                aligned[row] = gold[col]
        return aligned

    gold = normalize_triples(y_true)
    predicted = normalize_triples(y_pred)

    # Exact evaluation
    exact_scores = graph_scores(gold, predicted)

    # Fuzzy evaluation
    fuzzy_aligned = align_triples_fuzzy(gold, predicted, threshold=fuzzy_threshold)
    fuzzy_scores = graph_scores(gold, fuzzy_aligned)

    # Semantic evaluation
    if gold and predicted:
        if embedding_model is None:
            from sentence_transformers import SentenceTransformer
            embedding_model = SentenceTransformer(
                "nomic-ai/nomic-embed-text-v1.5",
                trust_remote_code=True
            )
        embeddings = build_embeddings(gold, predicted, embedding_model)
        semantic_aligned = align_triples_semantic(
            gold, predicted, embeddings, threshold=semantic_threshold
        )
    else:
        semantic_aligned = predicted

    semantic_scores = graph_scores(gold, semantic_aligned)

    return {
        "exact_match": exact_scores,
        "semantic_match": semantic_scores,
        "fuzzy_match": fuzzy_scores,
    }

def text2onto_metrics(
    y_true: Dict[str, Any],
    y_pred: Dict[str, Any],
    similarity_threshold: float = 0.8
) -> Dict[str, Any]:
    """
    Expects:
      y_true = {"terms": [{"doc_id": str, "term": str}, ...],
               "types": [{"doc_id": str, "type": str}, ...]}
      y_pred = same shape

    Returns:
      {"terms": {...}, "types": {...}}
    """

    def jaccard_similarity(text_a: str, text_b: str) -> float:
        tokens_a = set(text_a.lower().split())
        tokens_b = set(text_b.lower().split())
        if not tokens_a and not tokens_b:
            return 1.0
        return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)

    def pairs_to_strings(rows: List[Dict[str, str]], value_key: str) -> List[str]:
        paired_strings: List[str] = []
        for row in rows or []:
            doc_id = (row.get("doc_id") or "").strip()
            value = (row.get(value_key) or "").strip()
            if doc_id and value:
                # keep doc association + allow token Jaccard
                paired_strings.append(f"{doc_id} {value}")
        return paired_strings

    def score_list(ground_truth_items: List[str], predicted_items: List[str]) -> Dict[str, Union[float, int]]:
        matched_ground_truth_indices: Set[int] = set()
        matched_predicted_indices: Set[int] = set()

        for predicted_index, predicted_item in enumerate(predicted_items):
            for ground_truth_index, ground_truth_item in enumerate(ground_truth_items):
                if ground_truth_index in matched_ground_truth_indices:
                    continue

                if jaccard_similarity(predicted_item, ground_truth_item) >= similarity_threshold:
                    matched_predicted_indices.add(predicted_index)
                    matched_ground_truth_indices.add(ground_truth_index)
                    break

        total_correct = len(matched_predicted_indices)
        total_predicted = len(predicted_items)
        total_ground_truth = len(ground_truth_items)

        precision = total_correct / total_predicted if total_predicted else 0.0
        recall = total_correct / total_ground_truth if total_ground_truth else 0.0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0

        return {
            "f1_score": f1,
            "precision": precision,
            "recall": recall,
            "total_correct": total_correct,
            "total_predicted": total_predicted,
            "total_ground_truth": total_ground_truth,
        }

    ground_truth_terms = pairs_to_strings(y_true.get("terms", []), "term")
    predicted_terms = pairs_to_strings(y_pred.get("terms", []), "term")
    ground_truth_types = pairs_to_strings(y_true.get("types", []), "type")
    predicted_types = pairs_to_strings(y_pred.get("types", []), "type")

    terms_metrics = score_list(ground_truth_terms, predicted_terms)
    types_metrics = score_list(ground_truth_types, predicted_types)

    return {
        "terms": terms_metrics,
        "types": types_metrics,
    }

def term_typing_metrics(y_true: List[Dict[str, List[str]]], y_pred: List[Dict[str, List[str]]]) -> Dict[str, float | int]:
    """
    Compute precision, recall, and F1-score for term typing
    using (term, type) pair-level matching instead of ID-based lookups.

    Args:
        y_true: List of ground truth dicts, each with keys {"term": str, "types": List[str]}
        y_pred: List of predicted dicts, same format as y_true

    Returns:
        Dict: Containing precision, recall, and F1-score
    """
    # Flatten all (term, type) pairs from both y_true and y_pred
    true_pairs = set(
        (item["term"].strip().lower(), t.strip().lower())
        for item in y_true for t in item["types"]
    )
    pred_pairs = set(
        (item["term"].strip().lower(), t.strip().lower())
        for item in y_pred for t in item["types"]
    )
    correct_pairs = true_pairs.intersection(pred_pairs)
    total_correct = len(correct_pairs)
    total_predicted = len(pred_pairs)
    total_ground_truth = len(true_pairs)
    precision = total_correct / total_predicted if total_predicted > 0 else 0.0
    recall = total_correct / total_ground_truth if total_ground_truth > 0 else 0.0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "f1_score": f1_score,
        "precision": precision,
        "recall": recall,
        "total_correct": total_correct,
        "total_predicted": total_predicted,
        "total_ground_truth": total_ground_truth
    }

def taxonomy_discovery_metrics(y_true: List[Dict[str, str]], y_pred: List[Dict[str, str]]) -> Dict[str, float | int]:
    total_predicted = len(y_pred)
    total_ground_truth = len(y_true)
    # Convert ground truth and predictions to sets of tuples for easy comparison
    ground_truth_set = {(item["parent"].lower(), item["child"].lower()) for item in y_true}
    predictions_set = {(item["parent"].lower(), item["child"].lower()) for item in y_pred}
    # Calculate correctly predicted pairs (intersection of sets)
    correct_predictions = ground_truth_set.intersection(predictions_set)
    total_correct = len(correct_predictions)
    # Calculate precision, recall, and F1-score
    precision = total_correct / total_predicted if total_predicted > 0 else 0
    recall = total_correct / total_ground_truth if total_ground_truth > 0 else 0
    if precision + recall > 0:
        f1_score = 2 * (precision * recall) / (precision + recall)
    else:
        f1_score = 0
    return {
        "f1_score": f1_score,
        "precision": precision,
        "recall": recall,
        "total_correct": total_correct,
        "total_predicted": total_predicted,
        "total_ground_truth": total_ground_truth
    }


def non_taxonomic_re_metrics(y_true: List[Dict[str, str]], y_pred: List[Dict[str, str]]) -> Dict[str, float | int]:
    def normalize_triple(item: Dict[str, str]) -> Tuple[str, str, str]:
        return (
            item["head"].strip().lower(),
            item["relation"].strip().lower(),
            item["tail"].strip().lower()
        )

    def expand_symmetric(triples: Set[Tuple[str, str, str]]) -> Set[Tuple[str, str, str]]:
        expanded = set()
        for h, r, t in triples:
            expanded.add((h, r, t))
            if r in SYMMETRIC_RELATIONS:
                expanded.add((t, r, h))  # add reverse for symmetric
        return expanded

    gt_set = expand_symmetric({normalize_triple(item) for item in y_true})
    pred_set = expand_symmetric({normalize_triple(item) for item in y_pred})

    correct = gt_set & pred_set
    total_correct = len(correct)
    total_predicted = len(pred_set)
    total_ground_truth = len(gt_set)

    precision = total_correct / total_predicted if total_predicted else 0
    recall = total_correct / total_ground_truth if total_ground_truth else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0

    return {
        "f1_score": f1_score,
        "precision": precision,
        "recall": recall,
        "total_correct": total_correct,
        "total_predicted": total_predicted,
        "total_ground_truth": total_ground_truth
    }
