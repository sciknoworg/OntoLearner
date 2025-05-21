import matplotlib.pyplot as plt
import seaborn as sns
from plot_utils import setup_plotting, load_data, ensure_output_dir


def plot_combined_domain_analysis(df=None, output_dir=None, show=False, top_n=15):
    """
    Create a combined plot with two subplots:
        1. Distribution of ontologies by domain
        2. Top ontologies by processing time
    """
    setup_plotting()

    if df is None:
        df = load_data()

    output_dir = ensure_output_dir(output_dir)

    # Create a figure with two subplots side by side
    # Increased figure width and height to accommodate long domain names
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 10), dpi=120)

    # Subplot 1: Ontologies by Domain
    domain_counts = df['Domain'].value_counts()

    # Function to abbreviate extremely long domain names
    def abbreviate_long_domains(domains, max_length=25):
        abbreviated = []
        for domain in domains:
            if len(domain) > max_length:
                # For extremely long names like 'Materials Science and Engineering'
                # Abbreviate to 'Materials Sci. & Eng.'
                words = domain.split(' ')
                if len(words) > 3:
                    # Keep first word, abbreviate middle words, keep last word
                    result = words[0]
                    for word in words[1:-1]:
                        if len(word) > 3:
                            result += ' ' + word[:3] + '.'
                        else:
                            result += ' ' + word
                    result += ' ' + words[-1]
                    abbreviated.append(result)
                else:
                    abbreviated.append(domain)
            else:
                abbreviated.append(domain)
        return abbreviated

    # Abbreviate extremely long domain names
    domain_labels = abbreviate_long_domains(domain_counts.index)

    # Create the bar plot on the first axis
    sns.barplot(x=domain_counts.index, y=domain_counts.values, ax=ax1)

    # Add count labels on top of each bar
    for i, count in enumerate(domain_counts.values):
        ax1.text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')

    # Adjust y-axis limit to make room for the labels
    ax1.set_ylim(0, max(domain_counts.values) * 1.1)

    ax1.set_xlabel('Domain', fontsize=14)
    ax1.set_ylabel('Count', fontsize=14)
    ax1.set_xticklabels(domain_labels, rotation=45, ha='right')
    # ax1.set_title('Number of Ontologies by Domain', fontsize=16)

    # Subplot 2: Processing Time by Ontology
    df_sorted = df.sort_values('Processing Time (s)', ascending=False)
    top_n = min(top_n, len(df_sorted))  # Show top N or all if fewer

    # Create the bar plot on the second axis
    sns.barplot(
        x=df_sorted['Ontology ID'].head(top_n),
        y=df_sorted['Processing Time (s)'].head(top_n),
        ax=ax2
    )

    # Add time labels on top of each bar with rounded integers
    for i, time in enumerate(df_sorted['Processing Time (s)'].head(top_n)):
        # Round to integer and display
        rounded_time = int(round(time))
        ax2.text(i, time + 0.1, f"{rounded_time}s", ha='center', va='bottom', fontsize=9, rotation=45)

    ax2.set_xlabel('Ontology ID', fontsize=14)
    ax2.set_ylabel('Processing Time (seconds)', fontsize=14)
    # Keep ontology IDs as they are (typically short)
    ax2.set_xticklabels(df_sorted['Ontology ID'].head(top_n), rotation=45, ha='right')
    # ax2.set_title(f'Top {top_n} Ontologies by Processing Time', fontsize=16)

    # Adjust layout with extra padding for long labels
    plt.tight_layout(pad=2.0, w_pad=4.0, h_pad=2.0)

    # Save the plot
    output_path = output_dir / "combined_domain_analysis.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')

    if show:
        plt.show()
    else:
        plt.close()

    return output_path


if __name__ == "__main__":
    plot_combined_domain_analysis(show=True)
