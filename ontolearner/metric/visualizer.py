
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_topic_distribution(self):
    """
    Visualize topic distribution across different levels.
    """
    plt.figure(figsize=(15, 10))

    # Plot 1: Topic hierarchy levels
    depths = []
    for node in self.graph.nodes():
        in_paths = list(nx.shortest_path_length(self.graph, target=node).values())
        if in_paths:
            depths.append(max(in_paths))

    plt.subplot(2, 2, 1)
    sns.histplot(depths)
    plt.title('Topic Hierarchy Distribution')
    plt.xlabel('Depth Level')
    plt.ylabel('Number of Topics')

    # Plot 2: Relationship types distribution
    plt.subplot(2, 2, 2)
    rel_types = list(self.relationships.keys())
    rel_counts = list(self.relationships.values())
    plt.barh(range(len(rel_types)), rel_counts)
    plt.yticks(range(len(rel_types)), rel_types)
    plt.title('Relationship Types Distribution')

    plt.tight_layout()
    plt.show()


def visualize_graph_sample(self, max_nodes=50):
    """
    Visualize a sample of the topic hierarchy.
    """
    # Select a connected subset of nodes
    root = next(n for n in self.graph.nodes() if self.graph.in_degree(n) == 0)
    nodes = list(nx.bfs_tree(self.graph, root, depth_limit=3))[:max_nodes]
    subgraph = self.graph.subgraph(nodes)

    plt.figure(figsize=(15, 15))
    pos = nx.spring_layout(subgraph, k=2)

    # Draw nodes
    nx.draw_networkx_nodes(subgraph, pos, node_size=1000,
                               node_color='lightblue', alpha=0.7)
    nx.draw_networkx_edges(subgraph, pos, edge_color='gray', arrows=True)
    nx.draw_networkx_labels(subgraph, pos, font_size=8)

    plt.title(f"CSO Topic Hierarchy Sample (showing {len(nodes)} topics)")
    plt.axis('off')
    plt.show()
