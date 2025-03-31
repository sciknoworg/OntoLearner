from typing import List, Dict

from ontolearner.data_structure import TermTyping


class Evaluator:
    def __init__(self, ground_truth: List[Dict]):
        self.ground_truth = {item["concept"] for item in ground_truth}

    def compute_precision_at_k(self, term_typings: List[TermTyping], k: int = 10) -> float:
        """
        Calculate Precision@K for extracted terms vs. ground truth
        """
        predicted_terms = {typing.term for typing in term_typings}

        top_k_terms = list(predicted_terms)[:k]

        correct = len([term for term in top_k_terms if term in self.ground_truth])

        return correct / k
