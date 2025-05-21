import matplotlib.pyplot as plt
import seaborn as sns
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_ontologies_by_domain(df=None, output_dir=None, show=False):
    """Create a bar chart showing the distribution of ontologies by domain."""
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    plt.figure(figsize=(12, 8))
    domain_counts = df['Domain'].value_counts()

    ax = sns.barplot(x=domain_counts.index, y=domain_counts.values)

    for i, count in enumerate(domain_counts.values):
        ax.text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')

    plt.ylim(0, max(domain_counts.values) * 1.1)

    # plt.title('Number of Ontologies by Domain', fontsize=16)
    # plt.xlabel('Domain', fontsize=14)
    # plt.ylabel('Count', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    output_path = output_dir / "ontologies_by_domain.png"
    plt.savefig(output_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()

    return output_path


def plot_processing_time_by_ontology(df=None, output_dir=None, show=False):
    """Create a bar chart showing the processing time for each ontology."""
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    plt.figure(figsize=(14, 8))
    df_sorted = df.sort_values('Processing Time (s)', ascending=False)
    top_n = min(20, len(df_sorted))  # Show top 20 or all if fewer

    ax = sns.barplot(x=df_sorted['Ontology ID'].head(top_n), y=df_sorted['Processing Time (s)'].head(top_n))

    for i, time in enumerate(df_sorted['Processing Time (s)'].head(top_n)):
        ax.text(i, time + 0.1, f"{time:.2f}s", ha='center', va='bottom', fontsize=9, rotation=45)

    # plt.title('Top Ontologies by Processing Time', fontsize=16)
    # plt.xlabel('Ontology ID', fontsize=14)
    # plt.ylabel('Processing Time (seconds)', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_dir / "processing_time_by_ontology.png", dpi=300)

    if show:
        plt.show()
    else:
        plt.close()


def plot_processing_time_by_domain(df=None, output_dir=None, show=False):
    """
    Create a box plot showing the processing time distribution by domain.
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Create the plot
    plt.figure(figsize=(14, 8))

    # Create box plots for processing time metrics grouped by domain
    top_domains = df['Domain'].value_counts().index.tolist()
    df_filtered = df[df['Domain'].isin(top_domains)]

    sns.boxplot(x='Domain', y='Processing Time (s)', data=df_filtered)
    # plt.title('Processing Time Distribution by Domain', fontsize=16)
    plt.xlabel('Domain', fontsize=14)
    plt.ylabel('Processing Time (seconds)', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the plot
    output_path = output_dir / "processing_time_by_domain.png"
    plt.savefig(output_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()

    print(f"Created visualization: Processing Time Distribution by Domain ({output_path})")
    return output_path


if __name__ == "__main__":
    plot_ontologies_by_domain(show=True)
    plot_processing_time_by_ontology(show=True)
    # plot_processing_time_by_domain(show=True)
