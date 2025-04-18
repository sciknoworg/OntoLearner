from pydantic import BaseModel, Field
from typing import Dict


class TopologyMetrics(BaseModel):
    """Metrics describing the structural properties of the ontology graph"""
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
    """Metrics for evaluating the quality and characteristics of generated datasets"""
    num_term_types: int = Field(..., description="Number of term-type pairs in the dataset", ge=0)
    num_taxonomic_relations: int = Field(..., description="Number of taxonomic relations", ge=0)
    num_non_taxonomic_relations: int = Field(..., description="Number of non-taxonomic relations", ge=0)
    avg_terms: float = Field(..., description="Average number of terms per type", ge=0.0)


class OntologyMetrics(BaseModel):
    """Complete metrics collection for an ontology"""
    name: str = Field(..., description="Name of the ontology")
    topology: TopologyMetrics = Field(..., description="Structural topology metrics")
    dataset: DatasetMetrics = Field(..., description="Dataset metrics")


class BenchmarkMetrics(BaseModel):
    """Aggregate metrics across multiple ontologies"""
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
