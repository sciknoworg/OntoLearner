import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_scatter_relationships(df=None, output_dir=None, min_size=20, max_size=1500, show=False):
    """
    Create an enhanced scatter plot showing the distribution of taxonomic vs non-taxonomic
    relations in ontologies, with node count represented by marker size.
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Create a new figure with a specific size and higher DPI for better resolution
    plt.figure(figsize=(14, 10), dpi=120)

    # Filter out the largest three ontologies for a more balanced visualization
    df_filtered = df.copy()

    # Sort by total nodes to identify the largest ontologies
    largest_ontologies = df.nlargest(3, 'total_nodes')['Ontology ID'].tolist()

    # Print the names of the largest ontologies for transparency
    print(f"Excluding largest ontologies for better visualization: {', '.join(largest_ontologies)}")

    # Filter the dataframe
    df_filtered = df_filtered[~df_filtered['Ontology ID'].isin(largest_ontologies)]

    # No need to add epsilon for linear scale
    tax_relations = df_filtered['num_taxonomic_relations']
    nontax_relations = df_filtered['num_non_taxonomic_relations']

    # Create a ratio metric to identify interesting outliers
    # Add a small constant to avoid division by zero
    df_filtered['relation_ratio'] = tax_relations / (nontax_relations + 0.1)

    # Calculate sizes with better scaling - using square root scaling for more perceptual accuracy
    # and clamping to avoid extremely small or large points
    sizes = np.sqrt(df_filtered['total_nodes'])
    sizes = sizes / sizes.max() * max_size
    sizes = sizes.clip(min_size, max_size)

    # Create the scatter plot
    plt.scatter(
        tax_relations,
        nontax_relations,
        s=sizes,
        alpha=0.7,       # Add some transparency
        edgecolors='white',  # Add white edge for better visibility
        linewidths=0.5
    )

    # Add a legend for the reference lines
    plt.legend(loc='upper left', frameon=True, fontsize=10)

    # Annotate notable ontologies (using filtered dataframe)
    # 1. Ontologies with the highest total nodes in the filtered set
    top_by_size = df_filtered.nlargest(5, 'total_nodes')

    # 2. Ontologies with extreme ratios of taxonomic:non-taxonomic
    top_tax_ratio = df_filtered.nlargest(2, 'relation_ratio')
    top_nontax_ratio = df_filtered.nsmallest(2, 'relation_ratio')

    # Combine and remove duplicates
    to_annotate = pd.concat([top_by_size, top_tax_ratio, top_nontax_ratio]).drop_duplicates()

    for _, row in to_annotate.iterrows():
        plt.annotate(
            row['Ontology ID'],  # Text label
            (row['num_taxonomic_relations'], row['num_non_taxonomic_relations']),
            xytext=(5, 5),  # Small offset for text
            textcoords='offset points',
            fontsize=9,
            fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
        )

    # Customize grid
    plt.grid(True, linestyle='--', alpha=0.6)

    # Add labels with more context and information
    plt.xlabel('Taxonomic Relations', fontsize=12)
    plt.ylabel('Non-taxonomic Relations', fontsize=12)
    # Title is commented out to allow for use with external captions
    # plt.title('Ontology Relationship Type Distribution (Excluding 3 Largest Ontologies)', fontsize=16, fontweight='bold')

    # Improve tick label readability
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()

    output_path = output_dir / "scatter_relationships.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')

    if show:
        plt.show()
    else:
        plt.close()

    print(f"Created visualization: Enhanced relationship scatter plot ({output_path})")
    return output_path

if __name__ == "__main__":
    plot_scatter_relationships(show=True)
