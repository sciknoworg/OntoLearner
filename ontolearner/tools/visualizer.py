# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

from typing import Dict

from ..base import BaseOntology


class Visualizer:
    """
    Class for visualizing ontology structure and metrics.
    """

    def __init__(self, style_config: Dict = None):
        """
        Initialize visualizer with optional style configuration.
        """
        self.style_config = style_config or {
            'figsize': (15, 10),
            'node_color': 'lightblue',
            'edge_color': 'gray',
            'node_size': 1000,
            'font_size': 8,
            'alpha': 0.7
        }
        # Set the style for all plots
        sns.set_theme(style="whitegrid")
        plt.rcParams['figure.figsize'] = self.style_config['figsize']


    def visualize_metrics(self, ontology: BaseOntology, save_path: str = None) -> None:
        """
        Create a comprehensive visualization of ontology metrics.

        Args:
            ontology: The ontology to visualize
            save_path: Optional path to save the visualization
        """
        graph = ontology.nx_graph
        fig = plt.figure(figsize=(20, 15))

        # 1. Topic Hierarchy Distribution
        depths = self._calculate_depths(graph)
        ax1 = plt.subplot(2, 2, 1)
        sns.histplot(depths, ax=ax1)
        ax1.set_title('Topic Hierarchy Distribution')
        ax1.set_xlabel('Depth Level')
        ax1.set_ylabel('Number of Topics')

        # 2. Node Degree Distribution
        ax2 = plt.subplot(2, 2, 2)
        degrees = [d for _, d in graph.degree()]
        sns.histplot(degrees, ax=ax2)
        ax2.set_title('Node Degree Distribution')
        ax2.set_xlabel('Degree')
        ax2.set_ylabel('Count')

        # 3. Relationship Types
        ax3 = plt.subplot(2, 2, 3)
        self._plot_relationship_types(graph, ax3)

        # 4. Network Sample
        ax4 = plt.subplot(2, 2, 4)
        self._plot_network_sample(graph, ax4)

        plt.tight_layout()

        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
        fig.show()


    @staticmethod
    def visualize_class_distribution(ontology: BaseOntology, save_path: str = None) -> None:
        """
        Visualize the distribution of classes in the ontology.

        Args:
            ontology: The ontology to visualize
            save_path: Optional path to save the visualization
        """
        data = ontology.extract()
        class_counts = {}

        # Count instances per class
        for term_type in data.term_typings:
            for type_name in term_type.types:
                class_counts[type_name] = class_counts.get(type_name, 0) + 1

        # Sort by count
        sorted_classes = dict(sorted(class_counts.items(), key=lambda x: x[1], reverse=True))

        plt.figure(figsize=(15, 8))
        sns.barplot(x=list(sorted_classes.values()), y=list(sorted_classes.keys()))
        plt.title('Class Distribution in Ontology')
        plt.xlabel('Number of Instances')
        plt.ylabel('Class')

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()


    @staticmethod
    def _calculate_depths(graph: nx.DiGraph) -> list:
        """Calculate depths for all nodes in the graph."""
        depths = []
        root_nodes = [n for n in graph.nodes() if graph.in_degree(n) == 0]

        for node in graph.nodes():
            node_depths = []
            for root in root_nodes:
                try:
                    depth = nx.shortest_path_length(graph, root, node)
                    node_depths.append(depth)
                except nx.NetworkXNoPath:
                    continue
            if node_depths:
                depths.append(max(node_depths))

        return depths


    @staticmethod
    def _plot_relationship_types(graph: nx.DiGraph, ax: plt.Axes) -> None:
        """Plot distribution of relationship types."""
        relationship_types = {}
        for _, _, data in graph.edges(data=True):
            rel_type = data.get('relation_type', 'undefined')
            relationship_types[rel_type] = relationship_types.get(rel_type, 0) + 1

        rel_types = list(relationship_types.keys())
        rel_counts = list(relationship_types.values())

        ax.barh(range(len(rel_types)), rel_counts)
        ax.set_yticks(range(len(rel_types)))
        ax.set_yticklabels(rel_types)
        ax.set_title('Relationship Types Distribution')


    def _plot_network_sample(self, graph: nx.DiGraph, ax: plt.Axes, max_nodes: int = 50) -> None:
        """Plot a sample of the network."""
        # Select a connected subset of nodes
        root_nodes = [n for n in graph.nodes() if graph.in_degree(n) == 0]
        if not root_nodes:
            return

        root = root_nodes[0]
        nodes = list(nx.bfs_tree(graph, root, depth_limit=3))[:max_nodes]
        subgraph = graph.subgraph(nodes)

        pos = nx.spring_layout(subgraph, k=2)
        nx.draw_networkx_nodes(subgraph, pos,
                               node_size=self.style_config['node_size'],
                               node_color=self.style_config['node_color'],
                               alpha=self.style_config['alpha'],
                               ax=ax)
        nx.draw_networkx_edges(subgraph, pos,
                               edge_color=self.style_config['edge_color'],
                               arrows=True,
                               ax=ax)
        nx.draw_networkx_labels(subgraph, pos,
                                font_size=self.style_config['font_size'],
                                ax=ax)

        ax.set_title(f"Network Sample (showing {len(nodes)} nodes)")
        ax.axis('off')
