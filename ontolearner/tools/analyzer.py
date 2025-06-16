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

import logging
import time
from abc import ABC
from rdflib import RDF, RDFS, OWL
from collections import defaultdict

from ..base import BaseOntology
from ..data_structure import OntologyData, TopologyMetrics, DatasetMetrics, OntologyMetrics

logger = logging.getLogger(__name__)


class Analyzer(ABC):
    """
    Base class for comprehensive ontology analysis and metrics computation.

    This class provides a unified interface for analyzing ontologies and computing
    both structural topology metrics and dataset quality metrics. It serves as
    the foundation for ontology benchmarking, quality assessment, and comparative
    analysis across different domains and ontology types.

    The analyzer computes two main categories of metrics:
    1. **Topology Metrics**: Structural properties of the ontology graph including
       depth, breadth, connectivity, and knowledge coverage statistics.
    2. **Dataset Metrics**: Quality and characteristics of extracted learning
       datasets for the three fundamental ontology learning tasks.

    Used by the Processor class to generate comprehensive metrics for ontology
    repositories and benchmark studies.
    """

    def __init__(self) -> None:
        """
        Initialize the analyzer.

        The analyzer is stateless and can be reused across multiple ontologies.
        """
        pass

    def __call__(self, ontology: BaseOntology) -> OntologyMetrics:
        """
        Perform complete analysis of an ontology and return comprehensive metrics.

        This method orchestrates the full analysis workflow, computing both
        topology and dataset metrics for the given ontology. It provides a
        convenient callable interface for the analyzer.

        Args:
            ontology: Loaded ontology instance to analyze. Must have both
                     RDF graph and NetworkX graph representations available.

        Returns:
            Complete metrics object containing topology and dataset metrics.
        """
        return OntologyMetrics(
            name=ontology.__class__.__name__,
            topology=self.compute_topology_metrics(ontology),
            dataset=self.compute_dataset_metrics(ontology)
        )

    @staticmethod
    def compute_topology_metrics(ontology: BaseOntology) -> TopologyMetrics:
        """
        Compute comprehensive structural topology metrics for an ontology.

        This method analyzes the NetworkX graph representation of an ontology
        to extract detailed structural characteristics including graph connectivity,
        hierarchical organization, and knowledge coverage. The metrics provide
        insights into ontology complexity, quality, and design patterns.

        The computation includes:
        - Basic graph structure (nodes, edges, roots, leaves)
        - Hierarchical depth analysis with multi-root support
        - Breadth distribution across hierarchy levels
        - Knowledge coverage (classes, properties, individuals)

        Args:
            ontology: Loaded ontology with NetworkX graph representation.
                     Must have both rdf_graph and nx_graph attributes populated.

        Returns:
            Comprehensive topology metrics including all structural measures.
            Returns zero-valued metrics for empty ontologies.
        """
        logger.info("Starting topology metrics computation")
        start_time = time.time()
        graph = ontology.nx_graph

        if graph.number_of_nodes() == 0:
            return TopologyMetrics(
                total_nodes=0, total_edges=0,
                num_classes=0, num_properties=0, num_individuals=0,
                max_depth=0, min_depth=0, avg_depth=0, depth_variance=0,
                max_breadth=0, min_breadth=0, avg_breadth=0, breadth_variance=0,
                num_root_nodes=0, num_leaf_nodes=0
            )

        # Depth calculation with multiple root support
        root_nodes = [node for node in graph.nodes() if graph.in_degree(node) == 0]
        leaf_nodes = [node for node in graph.nodes() if graph.out_degree(node) == 0]
        depths = {}
        for root in root_nodes:
            current_visited = {root: 0}
            queue = [root]
            while queue:
                node = queue.pop(0)
                current_depth = current_visited[node]
                if node not in depths or current_depth < depths[node]:
                    depths[node] = current_depth
                for child in graph.successors(node):
                    child_depth = current_depth + 1
                    if child not in current_visited or child_depth < current_visited.get(child, float('inf')):
                        current_visited[child] = child_depth
                        queue.append(child)
            for node, depth in current_visited.items():
                if node not in depths or depth < depths[node]:
                    depths[node] = depth

        # Depth metrics
        depth_values = list(depths.values()) if depths else []
        max_depth = max(depth_values) if depth_values else 0
        min_depth = min(depth_values) if depth_values else 0
        avg_depth = sum(depth_values)/len(depth_values) if depth_values else 0.0
        depth_variance = sum((x - avg_depth)**2 for x in depth_values)/len(depth_values) if depth_values else 0.0

        # Breadth metrics
        depth_groups = defaultdict(list)
        for node, depth in depths.items():
            depth_groups[depth].append(node)
        breadth_values = [len(nodes) for nodes in depth_groups.values()]
        max_breadth = max(breadth_values) if breadth_values else 0
        min_breadth = min(breadth_values) if breadth_values else 0
        avg_breadth = sum(breadth_values)/len(breadth_values) if breadth_values else 0.0
        breadth_variance = sum((x - avg_breadth)**2 for x in breadth_values)/len(breadth_values) if breadth_values else 0.0

        # Knowledge coverage metrics
        classes = set(ontology.rdf_graph.subjects(RDF.type, RDFS.Class)) | \
                  set(ontology.rdf_graph.subjects(RDF.type, OWL.Class))
        num_classes = len(classes)

        properties = set(ontology.rdf_graph.subjects(RDF.type, OWL.ObjectProperty)) | \
                     set(ontology.rdf_graph.subjects(RDF.type, OWL.DatatypeProperty))
        num_properties = len(properties)

        individuals = set()
        for s in ontology.rdf_graph.subjects(RDF.type, None):
            for o in ontology.rdf_graph.objects(s, RDF.type):
                if o in classes:
                    individuals.add(s)
                    break
        num_individuals = len(individuals)

        metrics = TopologyMetrics(
            total_nodes=graph.number_of_nodes(),
            total_edges=graph.number_of_edges(),
            num_classes=num_classes,
            num_properties=num_properties,
            num_individuals=num_individuals,
            max_depth=max_depth,
            min_depth=min_depth,
            avg_depth=avg_depth,
            depth_variance=depth_variance,
            max_breadth=max_breadth,
            min_breadth=min_breadth,
            avg_breadth=avg_breadth,
            breadth_variance=breadth_variance,
            num_root_nodes=len(root_nodes),
            num_leaf_nodes=len(leaf_nodes)
        )

        logger.info(f"Completed topology metrics computation in {time.time() - start_time:.2f} seconds")

        return metrics

    @staticmethod
    def compute_dataset_metrics(ontology: BaseOntology) -> DatasetMetrics:
        """
        Compute quality and characteristics metrics for extracted learning datasets.

        This method analyzes the machine learning datasets extracted from an ontology
        to assess their quality, balance, and suitability for the three fundamental
        ontology learning tasks. The metrics help evaluate dataset richness and
        identify potential issues like class imbalance or sparse relationships.

        The computation analyzes:
        - Term typing dataset: Number and distribution of term-type mappings
        - Taxonomic relations: Count of hierarchical relationships
        - Non-taxonomic relations: Count of semantic associations
        - Class balance: Average terms per type for distribution analysis

        Args:
            ontology: Loaded ontology instance. The extract() method will be
                     called to obtain the learning datasets for analysis.

        Returns:
            Dataset metrics including counts and distribution measures for
            all three ontology learning tasks.
        """
        data: OntologyData = ontology.extract()

        term_typings = data.term_typings
        taxonomies = data.type_taxonomies.taxonomies
        non_taxonomic = data.type_non_taxonomic_relations.non_taxonomies

        class_counts = {}
        for term_type in term_typings:
            for type_name in term_type.types:
                class_counts[type_name] = class_counts.get(type_name, 0) + 1

        avg_terms_per_type = len(term_typings) / len(class_counts) if class_counts else 0

        dataset_metrics = DatasetMetrics(
            num_term_types=len(term_typings),
            num_taxonomic_relations=len(taxonomies),
            num_non_taxonomic_relations=len(non_taxonomic),
            avg_terms=avg_terms_per_type
        )
        return dataset_metrics
