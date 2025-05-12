from typing import List, Dict
from difflib import SequenceMatcher


def calculate_term_typing_metrics(predicted: List[str], ground_truth: List[str]) -> Dict[str, float]:
    """Calculate metrics for term typing task"""
    predicted_set = set(predicted)
    ground_truth_set = set(ground_truth)

    precision_score = len(predicted_set.intersection(ground_truth_set)) / len(predicted_set) if predicted_set else 0
    recall_score = len(predicted_set.intersection(ground_truth_set)) / len(ground_truth_set) if ground_truth_set else 0
    f1_score = 2 * (precision_score * recall_score) / (precision_score + recall_score) if (precision_score + recall_score) > 0 else 0
    exact_match = 1.0 if predicted_set == ground_truth_set else 0.0

    return {
        'precision_score': precision_score,
        'recall_score': recall_score,
        'f1_score': f1_score,
        'exact_match': exact_match
    }


def calculate_taxonomy_metrics(predicted: bool, ground_truth: bool) -> Dict[str, float]:
    """Calculate metrics for taxonomy relation prediction"""
    accuracy = 1.0 if predicted == ground_truth else 0.0

    tp = 1.0 if predicted and ground_truth else 0.0
    fp = 1.0 if predicted and not ground_truth else 0.0
    fn = 1.0 if not predicted and ground_truth else 0.0

    precision_score = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall_score = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1_score = 2 * (precision_score * recall_score) / (precision_score + recall_score) \
        if (precision_score + recall_score) > 0 else 0

    return {
        'accuracy': accuracy,
        'f1_score': f1_score
    }


def calculate_non_taxonomy_metrics(predicted: str, ground_truth: str) -> Dict[str, float]:
    """Calculate metrics for non-taxonomy relation prediction"""
    exact_match = 1.0 if predicted.lower() == ground_truth.lower() else 0.0
    similarity_score = SequenceMatcher(None, predicted.lower(), ground_truth.lower()).ratio()

    return {
        'exact_match': exact_match,
        'similarity_score': similarity_score
    }
