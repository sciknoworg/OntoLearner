import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns
import numpy as np
from pathlib import Path


# Set the style
plt.style.use('fivethirtyeight')
sns.set_palette("viridis")

# Read the Excel file
file_path = Path("../data/metrics/metrics copy.xlsx")
df = pd.read_excel(file_path)

# Display basic information about the dataset
print(f"Dataset shape: {df.shape}")
print("\nColumn names:")
for col in df.columns:
    print(f"- {col}")

print("\nFirst few rows:")
print(df.head())

# Create a directory for saving plots
output_dir = Path("ontology_plots")
output_dir.mkdir(exist_ok=True)


# Plot 1: Distribution of ontologies by domain
plt.figure(figsize=(12, 8))
domain_counts = df['Domain'].value_counts()
sns.barplot(x=domain_counts.index, y=domain_counts.values)
plt.title('Number of Ontologies by Domain', fontsize=16)
plt.xlabel('Domain', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(output_dir / "ontologies_by_domain.png", dpi=300)
plt.close()

print("Created visualization: Distribution of ontologies by domain")

# Plot 3: Size comparison of ontologies (by total nodes and edges)
plt.figure(figsize=(16, 10))
df_sorted = df.sort_values('total_nodes', ascending=False)
top_n = min(20, len(df_sorted))  # Show top 20 or all if fewer

x = np.arange(top_n)
width = 0.4

ax = plt.subplot(111)
bar1 = ax.bar(x - width/2, df_sorted['total_nodes'].head(top_n), width, label='Total Nodes')
bar2 = ax.bar(x + width/2, df_sorted['total_edges'].head(top_n), width, label='Total Edges')

plt.xlabel('Ontology', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.title('Ontology Size Comparison (Top 20)', fontsize=16)
plt.xticks(x, df_sorted['Ontology ID'].head(top_n), rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig(output_dir / "ontology_size_comparison.png", dpi=300)
plt.close()

print("Created visualization: Size comparison of ontologies")

# Plot 4: Depth vs. Breadth analysis
plt.figure(figsize=(12, 10))
scatter = plt.scatter(df['max_depth'], df['max_breadth'],
                     s=df['total_nodes']/10, # Size points by number of nodes
                     alpha=0.6,
                     c=pd.factorize(df['Domain'])[0], # Color by domain
                     cmap='viridis')

# Add ontology IDs as labels for the largest ontologies
threshold = df['total_nodes'].quantile(0.75)  # Label top 25% by size
for i, row in df[df['total_nodes'] > threshold].iterrows():
    plt.annotate(row['Ontology ID'],
                 (row['max_depth'], row['max_breadth']),
                 xytext=(5, 5), textcoords='offset points')

plt.title('Ontology Structure: Max Depth vs. Max Breadth', fontsize=16)
plt.xlabel('Maximum Depth', fontsize=14)
plt.ylabel('Maximum Breadth', fontsize=14)
plt.colorbar(scatter, label='Domain')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir / "depth_vs_breadth.png", dpi=300)
plt.close()

print("Created visualization: Depth vs. Breadth analysis")

# Plot 5: Distribution of classes, properties, and individuals
plt.figure(figsize=(16, 10))
df_sorted = df.sort_values('num_classes', ascending=False)
top_n = min(15, len(df_sorted))  # Show top 15 or all if fewer

# Create the grouped bar chart
x = np.arange(top_n)
width = 0.25

fig, ax = plt.subplots(figsize=(16, 10))
bar1 = ax.bar(x - width, df_sorted['num_classes'].head(top_n), width, label='Classes')
bar2 = ax.bar(x, df_sorted['num_properties'].head(top_n), width, label='Properties')
bar3 = ax.bar(x + width, df_sorted['num_individuals'].head(top_n), width, label='Individuals')

ax.set_xlabel('Ontology', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.set_title('Knowledge Component Distribution (Top 15 Ontologies)', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(df_sorted['Ontology ID'].head(top_n), rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.savefig(output_dir / "knowledge_component_distribution.png", dpi=300)
plt.close()

print("Created visualization: Knowledge component distribution")


# Plot 6: Hierarchical structure analysis - comparing depth metrics
plt.figure(figsize=(14, 8))

# Create box plots for depth metrics grouped by domain
top_domains = df['Domain'].value_counts().index.tolist()
df_filtered = df[df['Domain'].isin(top_domains)]

sns.boxplot(x='Domain', y='avg_depth', data=df_filtered)
plt.title('Average Depth Distribution by Domain', fontsize=16)
plt.xlabel('Domain', fontsize=14)
plt.ylabel('Average Depth', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(output_dir / "depth_by_domain.png", dpi=300)
plt.close()

print("Created visualization: Hierarchical structure analysis")


# Plot 7: Relationship analysis - taxonomic vs. non-taxonomic relations
plt.figure(figsize=(12, 8))

# Calculate the ratio of taxonomic to non-taxonomic relations
df['taxonomic_ratio'] = df['num_taxonomic_relations'] / (df['num_non_taxonomic_relations'] + 1)  # Add 1 to avoid division by zero

# Create a scatter plot
plt.scatter(df['num_taxonomic_relations'], df['num_non_taxonomic_relations'],
           s=df['total_nodes']/10, alpha=0.7,
           c=df['taxonomic_ratio'], cmap='plasma')

plt.title('Taxonomic vs. Non-Taxonomic Relations', fontsize=16)
plt.xlabel('Taxonomic Relations', fontsize=14)
plt.ylabel('Non-Taxonomic Relations', fontsize=14)
plt.xscale('log')
plt.yscale('log')
plt.colorbar(label='Taxonomic Ratio (higher = more taxonomic)')
plt.grid(True, alpha=0.3)

# Add ontology IDs as labels for interesting cases
# Label ontologies with high counts in either dimension
threshold_tax = df['num_taxonomic_relations'].quantile(0.9)
threshold_nontax = df['num_non_taxonomic_relations'].quantile(0.9)
for i, row in df[(df['num_taxonomic_relations'] > threshold_tax) |
                (df['num_non_taxonomic_relations'] > threshold_nontax)].iterrows():
    plt.annotate(row['Ontology ID'],
                 (row['num_taxonomic_relations'], row['num_non_taxonomic_relations']),
                 xytext=(5, 5), textcoords='offset points')

plt.tight_layout()
plt.savefig(output_dir / "relation_type_analysis.png", dpi=300)
plt.close()

print("Created visualization: Relationship type analysis")


plt.figure(figsize=(10, 6))
plt.scatter(df['num_taxonomic_relations'], df['num_non_taxonomic_relations'],
            s=df['total_nodes']/1000, c=df['avg_depth'], cmap='coolwarm')
plt.colorbar(label='Average Depth')
plt.xlabel('Taxonomic Relations')
plt.ylabel('Non-taxonomic Relations')
plt.title('Relationship Type Distribution\n(Size = Total Nodes/1000, Color = Avg Depth)')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()


def improved_relationship_scatter(df, min_size=20, max_size=1500, save_path=None):
    """
    Create an enhanced scatter plot showing the distribution of taxonomic vs non-taxonomic
    relations in ontologies, with node count represented by marker size and depth by color.
    """
    # Create a new figure with a specific size and higher DPI for better resolution
    plt.figure(figsize=(14, 10), dpi=120)

    # Add a small constant to avoid log(0) issues
    epsilon = 0.1
    tax_relations = df['num_taxonomic_relations'] + epsilon
    nontax_relations = df['num_non_taxonomic_relations'] + epsilon

    # Create a ratio metric to identify interesting outliers
    df['relation_ratio'] = tax_relations / nontax_relations

    # Calculate sizes with better scaling - using square root scaling for more perceptual accuracy
    # and clamping to avoid extremely small or large points
    sizes = np.sqrt(df['total_nodes'])
    sizes = sizes / sizes.max() * max_size
    sizes = sizes.clip(min_size, max_size)

    # Create the scatter plot
    scatter = plt.scatter(
        tax_relations,
        nontax_relations,
        s=sizes,
        c=df['avg_depth'],
        cmap='viridis',  # Changed to viridis which is better for continuous data
        alpha=0.7,       # Add some transparency
        edgecolors='white',  # Add white edge for better visibility
        linewidths=0.5
    )

    # Add a colorbar with a more descriptive label and better formatting
    cbar = plt.colorbar(scatter)
    cbar.set_label('Average Hierarchical Depth', fontsize=12)
    cbar.ax.tick_params(labelsize=10)

    # Add diagonal reference lines
    # max_val = max(tax_relations.max(), nontax_relations.max())

    # Diagonal line where taxonomic = non-taxonomic
    # plt.plot([epsilon, max_val], [epsilon, max_val], 'k--', alpha=0.3, label='Equal Relations')
    # plt.plot([epsilon, max_val], [epsilon*10, max_val*10], 'r--', alpha=0.3, label='10x Non-taxonomic')
    # plt.plot([epsilon*10, max_val*10], [epsilon, max_val], 'g--', alpha=0.3, label='10x Taxonomic')

    # Add a legend for the reference lines
    plt.legend(loc='upper left', frameon=True, fontsize=10)

    # Annotate notable ontologies
    # 1. Ontologies with the highest total nodes
    top_by_size = df.nlargest(3, 'total_nodes')

    # 2. Ontologies with extreme ratios of taxonomic:non-taxonomic
    top_tax_ratio = df.nlargest(2, 'relation_ratio')
    top_nontax_ratio = df.nsmallest(2, 'relation_ratio')

    # Combine and remove duplicates
    to_annotate = pd.concat([top_by_size, top_tax_ratio, top_nontax_ratio]).drop_duplicates()

    for _, row in to_annotate.iterrows():
        plt.annotate(
            row['Ontology ID'],  # Text label (assumes you have an ontology_id column)
            (row['num_taxonomic_relations'] + epsilon, row['num_non_taxonomic_relations'] + epsilon),
            xytext=(5, 5),  # Small offset for text
            textcoords='offset points',
            fontsize=9,
            fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
        )

    # Set axis scales to logarithmic, but with better formatting
    plt.xscale('log')
    plt.yscale('log')

    # Use ScalarFormatter to display actual values rather than powers of 10
    for axis in [plt.gca().xaxis, plt.gca().yaxis]:
        axis.set_major_formatter(ScalarFormatter())

    # Customize grid
    plt.grid(True, linestyle='--', alpha=0.6)

    # Add labels and title with more context and information
    plt.xlabel('Taxonomic Relations (log scale)', fontsize=12)
    plt.ylabel('Non-taxonomic Relations (log scale)', fontsize=12)
    plt.title('Ontology Relationship Type Distribution', fontsize=16, fontweight='bold')

    # Improve tick label readability
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Adjust layout to make room for the title and subtitle
    plt.tight_layout(rect=[0, 0, 1, 0.9])

    # Save the figure if a path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    return plt.gcf()  # Return the figure object

# Example usage:
fig = improved_relationship_scatter(df, save_path="ontology_relationships.png")
plt.show()
