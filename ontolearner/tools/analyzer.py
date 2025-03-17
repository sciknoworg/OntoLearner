import time
import networkx as nx
from abc import ABC

from .. import logger
from ..base import BaseOntology
from ..data_structure import OntologyData, TopologyMetrics, DatasetMetrics, OntologyMetrics


class Analyzer(ABC):
    """
    Base class for ontology analysis
    """
    def __init__(self):
        pass

    def __call__(self, ontology: BaseOntology) -> OntologyMetrics:
        """
        Perform complete analysis of ontology
        """
        return OntologyMetrics(
            name=ontology.__class__.__name__,
            topology=self.compute_topology_metrics(ontology),
            dataset=self.compute_dataset_metrics(ontology)
        )

    @staticmethod
    def compute_topology_metrics(ontology: BaseOntology) -> TopologyMetrics:
        """
        Compute comprehensive topology metrics for the ontology.

        :return: TopologyMetrics object with all computed metrics
        """
        logger.info("Starting topology metrics computation")

        # Time the computation
        start_time = time.time()
        graph = ontology.nx_graph

        # Early checks
        if graph.number_of_nodes() == 0:
            return TopologyMetrics(
                total_nodes=0, total_edges=0, density=0,
                avg_degree=0, max_in_degree=0, max_out_degree=0,
                max_depth=0, avg_depth=0, num_root_nodes=0,
                num_leaf_nodes=0, avg_path_length=0, diameter=0
            )

        # Basic node metrics
        root_nodes = [node for node in graph.nodes() if graph.in_degree(node) == 0]
        leaf_nodes = [node for node in graph.nodes() if graph.out_degree(node) == 0]

        # Calculate depths
        depths = []
        for node in graph.nodes():
            for root in root_nodes:
                try:
                    depth = nx.shortest_path_length(graph, root, node)
                    depths.append(depth)
                except nx.NetworkXNoPath:
                    continue

        # Calculate degree-related metrics
        in_degrees = [graph.in_degree(n) for n in graph.nodes()]
        out_degrees = [graph.out_degree(n) for n in graph.nodes()]

        # # Calculate path-related metrics
        # path_lengths = []
        # diameter = 0
        # for source in graph.nodes():
        #     for target in graph.nodes():
        #         if source != target:
        #             try:
        #                 path_length = nx.shortest_path_length(graph, source, target)
        #                 path_lengths.append(path_length)
        #                 diameter = max(diameter, path_length)
        #             except nx.NetworkXNoPath:
        #                 continue

        logger.info(f"Completed topology metrics computation in {time.time() - start_time:.2f} seconds")

        avg_degree = sum(dict(graph.degree()).values()) / graph.number_of_nodes() if graph.number_of_nodes() > 0 else 0

        # avg_path_length = sum(path_lengths) / len(path_lengths) if path_lengths else 0

        topology_metrics = TopologyMetrics(
            total_nodes=graph.number_of_nodes(),
            total_edges=graph.number_of_edges(),
            density=nx.density(graph),
            avg_degree=avg_degree,
            max_in_degree=max(in_degrees) if in_degrees else 0,
            max_out_degree=max(out_degrees) if out_degrees else 0,
            max_depth=max(depths) if depths else 0,
            avg_depth=sum(depths) / len(depths) if depths else 0,
            num_root_nodes=len(root_nodes),
            num_leaf_nodes=len(leaf_nodes),
            # avg_path_length=avg_path_length,
            # diameter=diameter
        )
        return topology_metrics


    @staticmethod
    def compute_dataset_metrics(ontology: BaseOntology) -> DatasetMetrics:
        """
        Compute metrics for generated datasets
        """
        data: OntologyData = ontology.extract()

        term_typings = data.term_typings
        taxonomies = data.type_taxonomies.taxonomies
        non_taxonomic = data.type_non_taxonomic_relations.non_taxonomies

        # Count instances per class
        class_counts = {}
        for term_type in term_typings:
            for type_name in term_type.types:
                class_counts[type_name] = class_counts.get(type_name, 0) + 1

        avg_terms_per_type = len(term_typings) / len(class_counts) if class_counts else 0

        dataset_metrics = DatasetMetrics(
            num_term_types=len(term_typings),
            num_taxonomic_relations=len(taxonomies),
            num_non_taxonomic_relations=len(non_taxonomic),
            class_distribution=class_counts,
            avg_terms=avg_terms_per_type
        )
        return dataset_metrics
