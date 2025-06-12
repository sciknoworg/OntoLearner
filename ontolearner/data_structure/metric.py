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

from pydantic import BaseModel, Field
from typing import Dict


class TopologyMetrics(BaseModel):
    """
    Comprehensive metrics describing the structural properties of an ontology graph.

    This class captures quantitative measures of an ontology's topological structure,
    including graph connectivity, hierarchical organization, and knowledge coverage.
    These metrics are essential for understanding ontology complexity, quality, and
    suitability for different learning tasks.

    The metrics are organized into four categories:
    1. Basic graph structure (nodes, edges, roots, leaves)
    2. Knowledge coverage (classes, properties, individuals)
    3. Hierarchical depth characteristics
    4. Hierarchical breadth characteristics
    """
    # Basic graph metrics
    total_nodes: int = Field(..., description="Total number of nodes (concepts) in the ontology", ge=0)
    total_edges: int = Field(..., description="Total number of edges (relationships) between nodes", ge=0)
    num_root_nodes: int = Field(..., description="Number of root concepts", ge=0)
    num_leaf_nodes: int = Field(..., description="Number of leaf concepts", ge=0)

    # Knowledge coverage
    num_classes: int = Field(..., description="Number of classes in the ontology", ge=0)
    num_properties: int = Field(..., description="Number of properties (object/data) in the ontology", ge=0)
    num_individuals: int = Field(..., description="Number of individuals in the ontology", ge=0)

    # Hierarchical metrics
    max_depth: int = Field(..., description="Maximum depth of the concept hierarchy", ge=0)
    min_depth: int = Field(..., description="Minimum depth of the concept hierarchy", ge=0)
    avg_depth: float = Field(..., description="Average depth of nodes", ge=0.0)
    depth_variance: float = Field(..., description="Variance of node depths", ge=0.0)

    # Breadth metrics
    max_breadth: int = Field(..., description="Largest number of nodes at a level", ge=0)
    min_breadth: int = Field(..., description="Smallest number of nodes at a level", ge=0)
    avg_breadth: float = Field(..., description="Average nodes per level", ge=0.0)
    breadth_variance: float = Field(..., description="Variance of nodes per level", ge=0.0)


class DatasetMetrics(BaseModel):
    """
    Metrics for evaluating the quality and characteristics of extracted learning datasets.

    This class captures quantitative measures of the machine learning datasets
    extracted from ontologies, focusing on the three fundamental ontology learning
    tasks. These metrics help assess dataset quality, balance, and suitability
    for training and evaluation.

    Attributes:
        num_term_types: Number of term-to-type mappings extracted for Task 1.
                       Higher values indicate richer type assignment data.
        num_taxonomic_relations: Number of hierarchical "is-a" relationships
                               extracted for Task 2. Indicates taxonomy richness.
        num_non_taxonomic_relations: Number of semantic associations extracted
                                   for Task 3. Shows relationship diversity.
        avg_terms: Average number of terms assigned to each type, indicating
                  the distribution balance of the term typing dataset.
    """
    num_term_types: int = Field(..., description="Number of term-type pairs in the dataset", ge=0)
    num_taxonomic_relations: int = Field(..., description="Number of taxonomic relations", ge=0)
    num_non_taxonomic_relations: int = Field(..., description="Number of non-taxonomic relations", ge=0)
    avg_terms: float = Field(..., description="Average number of terms per type", ge=0.0)


class OntologyMetrics(BaseModel):
    """
    Complete metrics collection for a single ontology.

    This class aggregates all quantitative measures for an ontology, combining
    structural topology metrics with dataset extraction metrics. It provides
    a comprehensive view of an ontology's characteristics for analysis,
    comparison, and quality assessment.

    Used by the Processor class to collect and export metrics to Excel files
    for benchmarking and analysis across multiple ontologies.

    Attributes:
        name: Human-readable name of the ontology for identification.
        topology: Structural metrics describing the ontology's graph properties.
        dataset: Dataset metrics describing the extracted learning data quality.
    """
    name: str = Field(..., description="Name of the ontology")
    topology: TopologyMetrics = Field(..., description="Structural topology metrics")
    dataset: DatasetMetrics = Field(..., description="Dataset metrics")


class BenchmarkMetrics(BaseModel):
    """
    Aggregate metrics across multiple ontologies for benchmarking and analysis.

    This class provides comprehensive statistical analysis across a collection
    of ontologies, enabling comparative studies, quality assessment, and
    benchmarking of ontology learning approaches. It aggregates individual
    ontology metrics and computes statistical summaries.

    Used for generating benchmark reports, identifying outliers, and understanding
    the distribution of characteristics across ontology collections. Essential
    for research comparing ontology learning methods across diverse domains.

    Attributes:
        total_ontologies: Total number of ontologies included in the benchmark.
        ontology_metrics: Dictionary mapping ontology IDs to their individual
                         metrics, preserving detailed information for each.
        avg_topology: Average topology metrics computed across all ontologies,
                     showing typical structural characteristics.
        avg_dataset: Average dataset metrics across all ontologies, indicating
                    typical learning data characteristics.
        topology_std: Standard deviations of topology metrics, showing structural
                     variability across the ontology collection.
        relationship_std: Standard deviations of relationship metrics, indicating
                         diversity in relationship patterns.
        dataset_std: Standard deviations of dataset metrics, showing variability
                    in learning data quality and quantity.
    """
    # Overview
    total_ontologies: int = Field(..., description="Number of ontologies analyzed")
    ontology_metrics: Dict[str, OntologyMetrics] = Field(..., description="Individual metrics for each ontology")
    # Averages
    avg_topology: TopologyMetrics = Field(..., description="Average topology metrics across ontologies")
    avg_dataset: DatasetMetrics = Field(..., description="Average dataset metrics")
    # Variation
    topology_std: Dict[str, float] = Field(..., description="Standard deviation of topology metrics")
    relationship_std: Dict[str, float] = Field(..., description="Standard deviation of relationship metrics")
    dataset_std: Dict[str, float] = Field(..., description="Standard deviation of dataset metrics")
