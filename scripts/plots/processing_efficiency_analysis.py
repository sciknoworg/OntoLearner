import matplotlib.pyplot as plt
import numpy as np
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_processing_efficiency_analysis(df=None, output_dir=None, top_n=15, show=False):
    """
    Create a combined bar chart and scatter plot showing processing efficiency analysis.
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Calculate processing efficiency (nodes processed per second)
    df['processing_efficiency'] = df['total_nodes'] / df['Processing Time (s)']

    # Sort by efficiency
    df_sorted = df.sort_values('processing_efficiency', ascending=False)
    top_n = min(top_n, len(df_sorted))  # Show top N or all if fewer

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), gridspec_kw={'height_ratios': [2, 1]})

    # Bar chart of processing efficiency
    x = np.arange(top_n)
    bars = ax1.bar(x, df_sorted['processing_efficiency'].head(top_n), width=0.7)

    # Add value labels on top of bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 5,
                 f'{height:.0f}',
                 ha='center', va='bottom', rotation=0, fontsize=9)

    ax1.set_xlabel('Ontology', fontsize=12)
    ax1.set_ylabel('Processing Efficiency\n(nodes/second)', fontsize=12)
    ax1.set_title('Ontology Processing Efficiency (Higher is Better)', fontsize=16)
    ax1.set_xticks(x)
    ax1.set_xticklabels(df_sorted['Ontology ID'].head(top_n), rotation=45, ha='right')
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    # Scatter plot showing relationship between size and efficiency
    scatter = ax2.scatter(df['total_nodes'],
                          df['processing_efficiency'],
                          s=80,
                          c=df['max_depth'],
                          cmap='viridis',
                          alpha=0.7)

    # Add annotations for the most efficient ontologies
    for i, row in df_sorted.head(5).iterrows():
        ax2.annotate(row['Ontology ID'],
                     (row['total_nodes'], row['processing_efficiency']),
                     xytext=(5, 5), textcoords='offset points',
                     fontsize=9, fontweight='bold',
                     bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", alpha=0.7))

    ax2.set_xlabel('Total Nodes', fontsize=12)
    ax2.set_ylabel('Processing Efficiency\n(nodes/second)', fontsize=12)
    ax2.set_title('Relationship Between Ontology Size and Processing Efficiency', fontsize=14)
    ax2.grid(True, linestyle='--', alpha=0.7)

    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax2)
    cbar.set_label('Max Depth')

    plt.tight_layout()

    # Save the plot
    output_path = output_dir / "processing_efficiency_analysis.png"
    plt.savefig(output_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()

    return output_path

if __name__ == "__main__":
    plot_processing_efficiency_analysis(show=True)
