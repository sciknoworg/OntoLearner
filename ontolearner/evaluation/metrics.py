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

from typing import Dict

SYMMETRIC_RELATIONS = {"equivalentclass", "sameas", "disjointwith"}

def text2onto_metrics(y_true, y_pred, similarity_threshold: float = 0.8) -> Dict:
    def jaccard_similarity(a, b):
        set_a = set(a.lower().split())
        set_b = set(b.lower().split())
        if not set_a and not set_b:
            return 1.0
        return len(set_a & set_b) / len(set_a | set_b)

    matched_gt_indices = set()
    matched_pred_indices = set()
    for i, pred_label in enumerate(y_pred):
        for j, gt_label in enumerate(y_true):
            if j in matched_gt_indices:
                continue
            sim = jaccard_similarity(pred_label, gt_label)
            if sim >= similarity_threshold:
                matched_pred_indices.add(i)
                matched_gt_indices.add(j)
                break  # each gt matched once

    total_correct = len(matched_pred_indices)
    total_predicted = len(y_pred)
    total_ground_truth = len(y_true)

    precision = total_correct / total_predicted if total_predicted > 0 else 0
    recall = total_correct / total_ground_truth if total_ground_truth > 0 else 0
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    return {
        "f1_score": f1_score,
        "precision": precision,
        "recall": recall
    }

def term_typing_metrics(y_true, y_pred) -> Dict:
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
        "recall": recall
    }

def taxonomy_discovery_metrics(y_true, y_pred) -> Dict:
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
        "recall": recall
    }

def non_taxonomic_re_metrics(y_true, y_pred) -> Dict:
    def normalize_triple(item):
        return (
            item["head"].strip().lower(),
            item["relation"].strip().lower(),
            item["tail"].strip().lower()
        )

    def expand_symmetric(triples):
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
        "recall": recall
    }
