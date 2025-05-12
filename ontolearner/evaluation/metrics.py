from pathlib import Path

import numpy as np
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def calculate_term_typing_metrics(predicted: List[str], ground_truth: List[str]) -> Dict[str, float]:
    """
    Calculate metrics for term typing task
    """
    predicted_set = set(predicted)
    ground_truth_set = set(ground_truth)

    # Precision: What fraction of predicted types are correct
    precision = len(predicted_set.intersection(ground_truth_set)) / len(predicted_set) if predicted_set else 0

    # Recall: What fraction of actual types are predicted
    recall = len(predicted_set.intersection(ground_truth_set)) / len(ground_truth_set) if ground_truth_set else 0

    # F1 score: Harmonic mean of precision and recall
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    # Exact match: True if predicted and ground truth sets are exactly the same
    exact_match = 1.0 if predicted_set == ground_truth_set else 0.0

    return {
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'exact_match': exact_match
    }


def calculate_taxonomy_metrics(predicted: bool, ground_truth: bool) -> Dict[str, float]:
    """
    Calculate metrics for taxonomy relation prediction
    """
    # For taxonomy, it's a binary classification task
    accuracy = 1.0 if predicted == ground_truth else 0.0

    # True positive, false positive, etc.
    tp = 1.0 if predicted and ground_truth else 0.0
    fp = 1.0 if predicted and not ground_truth else 0.0
    fn = 1.0 if not predicted and ground_truth else 0.0

    # Calculate precision and recall for F1
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return {
        'accuracy': accuracy,
        'f1': f1
    }


def calculate_non_taxonomy_metrics(predicted: str, ground_truth: str) -> Dict[str, float]:
    """
    Calculate metrics for non-taxonomy relation prediction
    """
    # Exact match between relation types
    exact_match = 1.0 if predicted.lower() == ground_truth.lower() else 0.0

    # String similarity (optional if you want to give partial credit)
    from difflib import SequenceMatcher
    similarity = SequenceMatcher(None, predicted.lower(), ground_truth.lower()).ratio()

    return {
        'exact_match': exact_match,
        'similarity_score': similarity
    }


def aggregate_metrics(results: List[Dict[str, Any]], task: str) -> Dict[str, float]:
    """
    Aggregate metrics across multiple examples
    """
    metrics = {}

    if not results:
        return metrics

    if task == "term-typing":
        metrics['avg_precision'] = np.mean([r['precision'] for r in results])
        metrics['avg_recall'] = np.mean([r['recall'] for r in results])
        metrics['avg_f1'] = np.mean([r['f1'] for r in results])
        metrics['avg_exact_match'] = np.mean([r['exact_match'] for r in results])

    elif task == "taxonomy-discovery":
        metrics['avg_accuracy'] = np.mean([r['accuracy'] for r in results])
        metrics['avg_f1'] = np.mean([r['f1'] for r in results])

    elif task == "non-taxonomy-discovery":
        metrics['avg_exact_match'] = np.mean([r['exact_match'] for r in results])
        metrics['avg_similarity'] = np.mean([r['similarity_score'] for r in results])

    metrics['num_samples'] = len(results)

    return metrics


def plot_model_comparison(summary_df, path: Path):
    """Plot comparison of model performance"""
    plt.figure(figsize=(10, max(6, len(summary_df) * 0.8)))

    # Create a more readable format for model names
    summary_df['Model'] = summary_df.apply(
        lambda x: f"{x['LLM Model'].split('/')[-1]} + {x['Retriever Model'].split('/')[-1]}",
        axis=1
    )

    # Sort by F1 score
    plot_df = summary_df.sort_values('F1 Score')

    # Plot horizontal bars
    sns.barplot(x='F1 Score', y='Model', data=plot_df, color='blue', label='F1 Score')
    plt.title('Model Performance (F1 Score)')
    plt.xlabel('Score')
    plt.tight_layout()
    plt.savefig(path / "model_f1_comparison.png")

    # Create separate plots for precision and recall
    plt.figure(figsize=(10, max(6, len(summary_df) * 0.8)))
    plot_df_melted = pd.melt(
        plot_df,
        id_vars=['Model'],
        value_vars=['Precision', 'Recall', 'F1 Score'],
        var_name='Metric', value_name='Score'
    )
    sns.barplot(x='Score', y='Model', hue='Metric', data=plot_df_melted)
    plt.title('Model Performance Metrics')
    plt.tight_layout()
    plt.savefig(path / "model_metrics_comparison.png")


def plot_type_analysis(results, path):
    """Plot analysis of performance by type"""
    path.mkdir(exist_ok=True, parents=True)

    type_metrics = {}

    # Collect performance metrics per type
    for result in results:
        for entry in result['detailed_results']:
            for type_name in entry['ground_truth']:
                if type_name not in type_metrics:
                    type_metrics[type_name] = {'correct': 0, 'total': 0}

                type_metrics[type_name]['total'] += 1
                if type_name in entry['predicted']:
                    type_metrics[type_name]['correct'] += 1

    # Calculate accuracy per type
    type_accuracy = {
        t: metrics['correct'] / metrics['total']
        for t, metrics in type_metrics.items()
        if metrics['total'] > 0
    }

    # Plot type accuracy
    plt.figure(figsize=(12, max(6, len(type_accuracy) * 0.3)))
    types_df = pd.DataFrame({
        'Type': list(type_accuracy.keys()),
        'Accuracy': list(type_accuracy.values()),
        'Count': [type_metrics[t]['total'] for t in type_accuracy.keys()]
    }).sort_values('Accuracy')

    # Color bars by frequency
    colors = plt.cm.viridis(types_df['Count'] / types_df['Count'].max())

    plt.barh(types_df['Type'], types_df['Accuracy'], color=colors)
    plt.xlabel('Accuracy')
    plt.ylabel('Type')
    plt.title('Prediction Accuracy by Type')
    plt.xlim(0, 1)
    plt.tight_layout()
    plt.savefig(path / "type_accuracy.png")

    # Add a color bar to show frequency
    plt.figure(figsize=(12, max(6, len(type_accuracy) * 0.3)))
    scatter = plt.scatter(
        types_df['Accuracy'],
        range(len(types_df)),
        c=types_df['Count'],
        cmap='viridis',
        s=100
    )
    plt.colorbar(scatter, label='# Occurrences')
    plt.yticks(range(len(types_df)), types_df['Type'])
    plt.xlabel('Accuracy')
    plt.title('Type Accuracy with Frequency')
    plt.xlim(0, 1)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(path / "type_accuracy_with_freq.png")


def plot_precision_recall_distribution(results, path):
    """Plot distribution of precision and recall scores"""
    path.mkdir(exist_ok=True, parents=True)

    all_entries = []
    for result in results:
        model_name = f"{result['llm'].split('/')[-1]} + {result['retriever'].split('/')[-1]}"
        for entry in result['detailed_results']:
            entry['model'] = model_name
            all_entries.append(entry)

    entries_df = pd.DataFrame(all_entries)

    # Precision-Recall scatter plot
    plt.figure(figsize=(10, 8))
    sns.scatterplot(
        data=entries_df,
        x='precision',
        y='recall',
        hue='model',
        size='f1',
        sizes=(20, 200),
        alpha=0.7
    )
    plt.title('Precision vs Recall for Each Example')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlabel('Precision')
    plt.ylabel('Recall')
    plt.tight_layout()
    plt.savefig(path / "precision_recall_scatter.png")

    # F1 score distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(entries_df, x='f1', hue='model', multiple='dodge', bins=10)
    plt.title('Distribution of F1 Scores')
    plt.xlabel('F1 Score')
    plt.ylabel('Count')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(path / "f1_distribution.png")
