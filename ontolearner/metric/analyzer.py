
import rdflib
from rdflib import Graph, Namespace
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns


class OntologyAnalyzer:
    def __init__(self, rdf_file):
        print(f"Loading CSO ontology from {rdf_file}...")
        self.g     = Graph()
        self.CSO   = Namespace("http://cso.kmi.open.ac.uk/schema/cso#")
        self.RDFS  = Namespace("http://www.w3.org/2000/01/rdf-schema#")
        self.graph = nx.DiGraph()

        self.g.parse(rdf_file, format="xml")

        self.build_graph()


    def build_graph(self):
        """
        Build and analyze the ontology graph structure.
        """
        print("\nAnalyzing CSO structure...")

        # Extract topics
        self.topics = list(self.g.subjects(predicate=rdflib.RDF.type, object=self.CSO.Topic))

        # Analyze relationship types
        self.relationships = self.analyze_relationship_types()

        print("\nBasic Statistics:")
        print(f"- Total Topics: {len(self.topics):,}")
        print(f"- Total Relationships: {sum(self.relationships.values()):,}")

        # Build graph from superTopicOf relationships
        print("\nBuilding topic hierarchy...")
        for s, p, o in self.g.triples((None, self.CSO.superTopicOf, None)):
            s_label = self.get_topic_label(s)
            o_label = self.get_topic_label(o)

            self.graph.add_edge(s_label, o_label)

        print(f"Graph contains {self.graph.number_of_nodes():,} nodes and {self.graph.number_of_edges():,} edges")


    def analyze_relationship_types(self):
        """
        Analyze and categorize relationship types.
        """
        relationships = defaultdict(int)

        for _, p, _ in self.g:
            rel_type = str(p).split('#')[-1]
            relationships[rel_type] += 1

        return dict(relationships)


    def get_topic_label(self, topic_uri):
        """Get human-readable label for a topic."""
        labels = list(self.g.objects(subject=topic_uri, predicate=self.RDFS.label))
        return str(labels[0]) if labels else str(topic_uri).split('/')[-1].replace('_', ' ')


    def analyze_structure(self):
        """Comprehensive structural analysis."""
        # Topic analysis
        root_topics = [n for n in self.graph.nodes() if self.graph.in_degree(n) == 0]
        leaf_topics = [n for n in self.graph.nodes() if self.graph.out_degree(n) == 0]

        # Calculate depths
        depths = []
        for node in self.graph.nodes():
            for root in root_topics:
                try:
                    path = nx.shortest_path_length(self.graph, root, node)
                    depths.append(path)
                except nx.NetworkXNoPath:
                    continue

        metrics = {
            'Topics': {
                'Total Topics': len(self.topics),
                'Root Topics': len(root_topics),
                'Leaf Topics': len(leaf_topics),
                'Max Depth': max(depths) if depths else 0,
                'Avg Depth': sum(depths) / len(depths) if depths else 0
            },
            'Relationships': self.relationships,
            'Graph Metrics': {
                'Nodes': self.graph.number_of_nodes(),
                'Edges': self.graph.number_of_edges(),
                'Density': nx.density(self.graph),
                'Average Degree': sum(dict(self.graph.degree()).values()) / self.graph.number_of_nodes()
            }
        }

        return metrics


    def visualize_topic_distribution(self):
        """Visualize topic distribution across different levels."""
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
        """Visualize a sample of the topic hierarchy."""
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


    def generate_report(self):
        """Generate comprehensive analysis report."""
        metrics = self.analyze_structure()

        print("\nCSO Analysis Report")
        print("==================")

        print("\n1. Topic Statistics:")
        for k, v in metrics['Topics'].items():
            print(f"  - {k}: {v:,.2f}" if isinstance(v, float) else f"  - {k}: {v:,}")

        print("\n2. Relationship Types:")
        for k, v in metrics['Relationships'].items():
            print(f"  - {k}: {v:,}")

        print("\n3. Graph Metrics:")
        for k, v in metrics['Graph Metrics'].items():
            print(f"  - {k}: {v:,.4f}" if isinstance(v, float) else f"  - {k}: {v:,}")

        # Visualizations
        print("\nGenerating visualizations...")
        self.visualize_topic_distribution()
        self.visualize_graph_sample()


if __name__ == "__main__":
    analyzer = OntologyAnalyzer("../../data/ontologies/CSO.3.4.owl")
    analyzer.generate_report()
