import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_classes_vs_processing_time(df=None, output_dir=None, min_size=20, max_size=1000, show=False):
    """
    Create an enhanced scatter plot showing the relationship between number of classes
    and processing time, with node count represented by marker size.
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Create a new figure with a specific size and higher DPI for better resolution
    plt.figure(figsize=(14, 10), dpi=120)

    # Filter out the largest two ontologies for a more balanced visualization
    df_filtered = df.copy()

    # Sort by total nodes to identify the largest ontologies
    largest_ontologies = df.nlargest(3, 'total_nodes')['Ontology ID'].tolist()

    # Print the names of the largest ontologies for transparency
    print(f"Excluding largest ontologies for better visualization: {', '.join(largest_ontologies)}")

    # Filter the dataframe to exclude the largest ontologies
    df_filtered = df_filtered[~df_filtered['Ontology ID'].isin(largest_ontologies)]

    # No need to add epsilon for linear scale
    classes = df_filtered['num_classes']
    proc_time = df_filtered['Processing Time (s)']

    # Calculate sizes with better scaling - using square root scaling for more perceptual accuracy
    # and clamping to avoid extremely small or large points
    sizes = np.sqrt(df_filtered['total_nodes'])
    sizes = sizes / sizes.max() * max_size
    sizes = sizes.clip(min_size, max_size)

    # Create the scatter plot
    plt.scatter(
        classes,
        proc_time,
        s=sizes,
        alpha=0.7,       # Add some transparency
        edgecolors='white',  # Add white edge for better visibility
        linewidths=0.5
    )

    ## --- Annotate notable points (using filtered dataframe)
    ## 1. Ontologies with high class count
    top_by_classes = df_filtered.nlargest(4, 'num_classes')
    ## 2. Ontologies with high processing time
    top_by_time = df_filtered.nlargest(3, 'Processing Time (s)')
    ## 3. Ontologies with unusually efficient processing (low time for high class count)
    # Add a small constant to avoid division by zero
    df_filtered['efficiency'] = df_filtered['num_classes'] / (df_filtered['Processing Time (s)'] + 0.1)
    # efficient = df_filtered.nlargest(3, 'efficiency')

    # Combine and remove duplicates
    to_annotate = pd.concat([top_by_classes, top_by_time]).drop_duplicates()

    for i, row in to_annotate.iterrows():
        plt.annotate(
            row['Ontology ID'],  # Text label
            (row['num_classes'], row['Processing Time (s)']),
            xytext=(5, 5),  # Small offset for text
            textcoords='offset points',
            fontsize=9,
            fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
        )

    # Customize grid
    plt.grid(True, linestyle='--', alpha=0.6)

    # Add labels with more context and information
    plt.xlabel('Number of Classes', fontsize=12)
    plt.ylabel('Processing Time (seconds)', fontsize=12)
    # Title is commented out to allow for use with external captions
    # plt.title('Relationship Between Number of Classes and Processing Time (Excluding Largest Ontologies)', fontsize=16, fontweight='bold')

    # Improve tick label readability
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()

    output_path = output_dir / "scatter_classes_vs_processing_time.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')

    if show:
        plt.show()
    else:
        plt.close()

    print(f"Created visualization: Classes vs Processing Time ({output_path})")
    return output_path

if __name__ == "__main__":
    plot_classes_vs_processing_time(show=True)
