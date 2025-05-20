import matplotlib.pyplot as plt
import numpy as np
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_ontology_size_comparison(df=None, output_dir=None, top_n=20, show=False):
    """
    Create a bar chart comparing the size of ontologies by total nodes and edges.
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Create the plot
    plt.figure(figsize=(16, 10))
    df_sorted = df.sort_values('total_nodes', ascending=False)
    top_n = min(top_n, len(df_sorted))  # Show top N or all if fewer

    x = np.arange(top_n)

    plt.xlabel('Ontology', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.title(f'Ontology Size Comparison (Top {top_n})', fontsize=16)
    plt.xticks(x, df_sorted['Ontology ID'].head(top_n), rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    # Save the plot
    output_path = output_dir / "ontology_size_comparison.png"
    plt.savefig(output_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()

    print(f"Created visualization: Size comparison of ontologies ({output_path})")
    return output_path

if __name__ == "__main__":
    plot_ontology_size_comparison(show=True)
