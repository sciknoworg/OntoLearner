import matplotlib.pyplot as plt
import seaborn as sns
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_depth_by_domain(df=None, output_dir=None, show=False):
    """
    Create a box plot showing the average depth distribution by domain.
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Create the plot
    plt.figure(figsize=(14, 8))

    # Create box plots for depth metrics grouped by domain
    top_domains = df['Domain'].value_counts().index.tolist()
    df_filtered = df[df['Domain'].isin(top_domains)]

    sns.boxplot(x='Domain', y='avg_depth', data=df_filtered)
    # plt.title('Average Depth Distribution by Domain', fontsize=16)
    # plt.xlabel('Domain', fontsize=14)
    # plt.ylabel('Average Depth', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the plot
    output_path = output_dir / "depth_by_domain.png"
    plt.savefig(output_path, dpi=300)

    if show:
        plt.show()
    else:
        plt.close()

    print(f"Created visualization: Hierarchical structure analysis ({output_path})")
    return output_path

if __name__ == "__main__":
    plot_depth_by_domain(show=True)
