from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_model_comparison(summary_df, path: Path):
    """Plot comparison of model performance"""
    plt.figure(figsize=(10, max(6, len(summary_df) * 0.8)))

    # Create a more readable format for model names
    summary_df['Model'] = summary_df.apply(
        lambda x: f"{x['LLM Model'].split('/')[-1]} + {x['Retriever Model'].split('/')[-1]}",
        axis=1
    )

    plot_df = summary_df.sort_values('F1 Score')

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
        value_vars=['Precision Score', 'Recall Score', 'F1 Score'],
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
        x='precision_score',
        y='recall_score',
        hue='model',
        size='f1_score',
        sizes=(20, 200),
        alpha=0.7
    )
    plt.title('Precision Score vs Recall Score for Each Example')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlabel('Precision Score')
    plt.ylabel('Recall Score')
    plt.tight_layout()
    plt.savefig(path / "precision_recall_scatter.png")

    # F1 score distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(entries_df, x='f1_score', hue='model', multiple='dodge', bins=10)
    plt.title('Distribution of F1 Scores')
    plt.xlabel('F1 Score')
    plt.ylabel('Count')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(path / "f1_distribution.png")
