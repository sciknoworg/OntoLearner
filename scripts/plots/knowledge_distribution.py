import matplotlib.pyplot as plt
import numpy as np
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_knowledge_component_distribution(df=None, output_dir=None, top_n=15, show=False):
    """
    Create a grouped bar chart showing the distribution of classes, properties, and individuals.
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Create the plot
    df_sorted = df.sort_values('num_classes', ascending=False)
    top_n = min(top_n, len(df_sorted))  # Show top N or all if fewer

    # Create the grouped bar chart
    x = np.arange(top_n)

    fig, ax = plt.subplots(figsize=(16, 10))

    ax.set_xlabel('Ontology', fontsize=14)
    ax.set_ylabel('Count', fontsize=14)
    ax.set_title(f'Knowledge Component Distribution (Top {top_n} Ontologies)', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(df_sorted['Ontology ID'].head(top_n), rotation=45, ha='right')
    ax.legend()

    plt.tight_layout()

    # Save the plot
    output_path = output_dir / "knowledge_component_distribution.png"
    plt.savefig(output_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()

    print(f"Created visualization: Knowledge component distribution ({output_path})")
    return output_path

if __name__ == "__main__":
    plot_knowledge_component_distribution(show=True)
