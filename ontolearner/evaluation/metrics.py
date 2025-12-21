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
from typing import List, Dict, Tuple, Set, Any, Union

SYMMETRIC_RELATIONS = {"equivalentclass", "sameas", "disjointwith"}

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
