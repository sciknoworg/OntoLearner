import numpy as np
from typing import List, Dict, Any


def aggregate_metrics(results: List[Dict[str, Any]], task: str) -> Dict[str, float]:
    """
    Aggregate metrics across multiple examples
    """
    metrics = {}

    if not results:
        return metrics

    if task == "term-typing":
        metrics['avg_precision_score'] = np.mean([r['precision_score'] for r in results])
        metrics['avg_recall_score'] = np.mean([r['recall_score'] for r in results])
        metrics['avg_f1_score'] = np.mean([r['f1_score'] for r in results])
        metrics['avg_exact_match'] = np.mean([r['exact_match'] for r in results])

    elif task == "taxonomy-discovery":
        metrics['avg_accuracy'] = np.mean([r['accuracy'] for r in results])
        metrics['avg_f1_score'] = np.mean([r['f1_score'] for r in results])

    elif task == "non-taxonomy-discovery":
        metrics['avg_exact_match'] = np.mean([r['exact_match'] for r in results])
        metrics['avg_similarity'] = np.mean([r['similarity_score'] for r in results])

    metrics['num_samples'] = len(results)

    return metrics
