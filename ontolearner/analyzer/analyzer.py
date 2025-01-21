import time

import networkx as nx
from abc import ABC
from typing import Dict
import logging

from ..base.ontology import BaseOntology
from ..base.data_model import OntologyData
from ..base.metric_model import TopologyMetrics, DatasetMetrics, OntologyMetrics


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class BaseOntologyAnalyzer(ABC):
    """
    Base class for ontology analysis
    """
    def __init__(self, ontology: BaseOntology):
        """
        Initialize the analyzer with the ontology
        :param ontology:
        """
        self.ontology = ontology

    def compute_topology_metrics(self) -> TopologyMetrics:
        """
        Compute comprehensive topology metrics for the ontology.

        :return: TopologyMetrics object with all computed metrics
        """
        logger.info("Starting topology metrics computation")

        # Time the computation
        start_time = time.time()

        G = self.ontology.nx_graph

        # Early checks
        if G.number_of_nodes() == 0:
            return TopologyMetrics(
                total_nodes=0, total_edges=0, density=0,
                avg_degree=0, max_in_degree=0, max_out_degree=0,
                max_depth=0, avg_depth=0, num_root_nodes=0,
                num_leaf_nodes=0, avg_path_length=0, diameter=0
            )

        # Basic node metrics
        root_nodes = [n for n in G.nodes() if G.in_degree(n) == 0]
        leaf_nodes = [n for n in G.nodes() if G.out_degree(n) == 0]

        # Calculate depths
        depths = []
        for node in G.nodes():
            for root in root_nodes:
                try:
                    depth = nx.shortest_path_length(G, root, node)
                    depths.append(depth)
                except nx.NetworkXNoPath:
                    continue

        # Calculate degree-related metrics
        in_degrees = [G.in_degree(n) for n in G.nodes()]
        out_degrees = [G.out_degree(n) for n in G.nodes()]

        # Calculate path-related metrics
        path_lengths = []
        diameter = 0
        for source in G.nodes():
            for target in G.nodes():
                if source != target:
                    try:
                        path_length = nx.shortest_path_length(G, source, target)
                        path_lengths.append(path_length)
                        diameter = max(diameter, path_length)
                    except nx.NetworkXNoPath:
                        continue

        logger.info(f"Completed topology metrics computation in {time.time() - start_time:.2f} seconds")

        # Create TopologyMetrics with all required fields
        return TopologyMetrics(
            # Basic graph metrics
            total_nodes=G.number_of_nodes(),
            total_edges=G.number_of_edges(),
            density=nx.density(G),

            # Degree-related metrics
            avg_degree=sum(dict(G.degree()).values()) / G.number_of_nodes() if G.number_of_nodes() > 0 else 0,
            max_in_degree=max(in_degrees) if in_degrees else 0,
            max_out_degree=max(out_degrees) if out_degrees else 0,

            # Hierarchical metrics
            max_depth=max(depths) if depths else 0,
            avg_depth=sum(depths) / len(depths) if depths else 0,
            num_root_nodes=len(root_nodes),
            num_leaf_nodes=len(leaf_nodes),

            # Path-related metrics
            avg_path_length=sum(path_lengths) / len(path_lengths) if path_lengths else 0,
            diameter=diameter
        )


    @staticmethod
    def compute_dataset_metrics(data: Dict) -> DatasetMetrics:
        """
        Compute metrics for generated datasets
        """
        term_typings = data['term_typings']
        taxonomies = data['type_taxonomies']['taxonomies']
        non_taxonomic = data['type_non_taxonomic_relations']['grand_truths']

        # Count instances per class
        class_counts = {}
        for term_type in term_typings:
            for type_name in term_type['types']:
                class_counts[type_name] = class_counts.get(type_name, 0) + 1

        return DatasetMetrics(
            num_term_types=len(term_typings),
            num_taxonomic_relations=len(taxonomies),
            num_non_taxonomic_relations=len(non_taxonomic),
            class_distribution=class_counts,
            avg_terms_per_type=len(term_typings) / len(class_counts) if class_counts else 0
        )


    def analyze(self) -> OntologyMetrics:
        """
        Perform complete analysis of ontology
        """
        # Extract data
        data: OntologyData = self.ontology.extract()

        return OntologyMetrics(
            name=self.ontology.__class__.__name__,
            topology=self.compute_topology_metrics(),
            dataset=self.compute_dataset_metrics(data)
        )
