import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_size_vs_processing_time(df=None, output_dir=None, show=False):
    """
    Create a scatter plot showing the relationship between total ontology size and processing time.
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Create the plot
    plt.figure(figsize=(12, 8))

    # Create scatter plot with total nodes on x-axis
    scatter = plt.scatter(df['total_nodes'], df['Processing Time (s)'],
                          s=80,  # Fixed size for better visibility
                          alpha=0.7,
                          c=df['max_depth'],  # Color by max depth
                          cmap='plasma')

    # Add logarithmic trend line
    if (df['total_nodes'] > 0).all() and (df['Processing Time (s)'] > 0).all():
        x_log = np.log(df['total_nodes'])
        y_log = np.log(df['Processing Time (s)'])
        mask = ~np.isnan(x_log) & ~np.isnan(y_log)
        z = np.polyfit(x_log[mask], y_log[mask], 1)
        p = np.poly1d(z)

        # Generate points for plotting the curve
        x_range = np.linspace(df['total_nodes'].min(), df['total_nodes'].max(), 100)
        y_range = np.exp(p(np.log(x_range)))
        plt.plot(x_range, y_range, "r--", alpha=0.8)

        # Add power law equation to plot
        plt.annotate(f"Power Law: Time ∝ Nodes^{z[0]:.2f}",
                     xy=(0.05, 0.95),
                     xycoords='axes fraction',
                     fontsize=12,
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

    # Annotate notable points
    top_by_nodes = df.nlargest(3, 'total_nodes')
    top_by_time = df.nlargest(3, 'Processing Time (s)')
    low_time_big_ont = df.sort_values('Processing Time (s)').head(5).sort_values('total_nodes', ascending=False).head(2)

    # Combine and remove duplicates
    to_annotate = pd.concat([top_by_nodes, top_by_time, low_time_big_ont]).drop_duplicates()

    for i, row in to_annotate.iterrows():
        plt.annotate(row['Ontology ID'],
                     (row['total_nodes'], row['Processing Time (s)']),
                     xytext=(5, 5), textcoords='offset points',
                     fontsize=9, fontweight='bold',
                     bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", alpha=0.7))

    plt.title('Ontology Size vs. Processing Time', fontsize=16)
    plt.xlabel('Total Nodes', fontsize=14)
    plt.ylabel('Processing Time (seconds)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.colorbar(scatter, label='Max Depth')

    # Use log scale if data range is large
    if df['total_nodes'].max() / df['total_nodes'].min() > 100:
        plt.xscale('log')
    if df['Processing Time (s)'].max() / df['Processing Time (s)'].min() > 100:
        plt.yscale('log')

    plt.tight_layout()

    # Save the plot
    output_path = output_dir / "size_vs_processing_time.png"
    plt.savefig(output_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()

    print(f"Created visualization: Relationship between Total Ontology Size and Processing Time ({output_path})")
    return output_path

if __name__ == "__main__":
    plot_size_vs_processing_time(show=True)
