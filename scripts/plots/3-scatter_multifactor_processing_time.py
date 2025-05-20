import matplotlib.pyplot as plt
import pandas as pd
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_multifactor_processing_time(df=None, output_dir=None, show=False):
    """
    Create a bubble chart showing multiple factors vs processing time.
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Create the plot
    plt.figure(figsize=(14, 10))

    # Calculate taxonomic ratio
    df['taxonomic_ratio'] = df['num_taxonomic_relations'] / (df['num_non_taxonomic_relations'] + 1)

    scatter = plt.scatter(df['num_classes'],
                          df['Processing Time (s)'],
                          s=df['total_edges']/10,  # Size based on total edges
                          c=df['taxonomic_ratio'],  # Color based on taxonomic ratio
                          alpha=0.7,
                          cmap='coolwarm')

    plt.title('Multi-factor Analysis: Classes, Edges and Relation Types vs. Processing Time', fontsize=16)
    plt.xlabel('Number of Classes', fontsize=14)
    plt.ylabel('Processing Time (seconds)', fontsize=14)
    plt.colorbar(scatter, label='Taxonomic Ratio (higher = more taxonomic)')

    # Add annotations for interesting cases
    # Ontologies with high class count but low processing time
    efficient = df.sort_values('num_classes', ascending=False).head(15).sort_values('Processing Time (s)').head(3)
    # Ontologies with low class count but high processing time
    inefficient = df.sort_values('num_classes').head(15).sort_values('Processing Time (s)', ascending=False).head(3)

    for i, row in pd.concat([efficient, inefficient]).iterrows():
        plt.annotate(row['Ontology ID'],
                     (row['num_classes'], row['Processing Time (s)']),
                     xytext=(5, 5), textcoords='offset points',
                     fontsize=9, fontweight='bold',
                     bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", alpha=0.7))

    # Add a legend to explain bubble size
    sizes = [min(df['total_edges']/10), df['total_edges'].quantile(0.5)/10, max(df['total_edges']/10)]
    labels = [f"{int(size*10)} edges" for size in sizes]
    for i, size in enumerate(sizes):
        plt.scatter([], [], s=size, c='gray', alpha=0.7, label=labels[i])
    plt.legend(title="Bubble Size Legend:", loc="upper right")

    plt.tight_layout()

    # Save the plot
    output_path = output_dir / "multifactor_processing_time.png"
    plt.savefig(output_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()

    print(f"Created visualization: Multi-factor Analysis of Processing Time ({output_path})")
    return output_path

if __name__ == "__main__":
    plot_multifactor_processing_time(show=True)
