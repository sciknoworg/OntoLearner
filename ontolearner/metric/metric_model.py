
from pydantic import BaseModel, Field
from typing import Dict


class TopologyMetrics(BaseModel):
    """
    Metrics describing the structural properties of the ontology graph
    """
    # Basic graph metrics
    total_nodes: int = Field(
        ...,
        description="Total number of nodes (concepts) in the ontology",
        ge=0
    )
    total_edges: int = Field(
        ...,
        description="Total number of edges (relationships) between nodes",
        ge=0
    )
    density: float = Field(
        ...,
        description="Ratio of actual connections to possible connections",
        ge=0.0,
        le=1.0
    )

    # Degree-related metrics
    avg_degree: float = Field(
        ...,
        description="Average number of connections per node",
        ge=0.0
    )
    max_in_degree: int = Field(
        ...,
        description="Maximum number of incoming edges to any node",
        ge=0
    )
    max_out_degree: int = Field(
        ...,
        description="Maximum number of outgoing edges from any node",
        ge=0
    )

    # Hierarchical metrics
    max_depth: int = Field(
        ...,
        description="Maximum depth of the concept hierarchy",
        ge=0
    )
    avg_depth: float = Field(
        ...,
        description="Average depth of nodes in the hierarchy",
        ge=0.0
    )
    num_root_nodes: int = Field(
        ...,
        description="Number of top-level (root) concepts",
        ge=0
    )
    num_leaf_nodes: int = Field(
        ...,
        description="Number of bottom-level (leaf) concepts",
        ge=0
    )

    # Path-related metrics
    avg_path_length: float = Field(
        ...,
        description="Average shortest path length between connected nodes",
        ge=0.0
    )
    diameter: int = Field(
        ...,
        description="Longest shortest path in the graph",
        ge=0
    )


class DatasetMetrics(BaseModel):
    """
    Metrics for evaluating the quality and characteristics of generated datasets
    """
    num_term_types: int = Field(..., description="Number of term-type pairs in the dataset", ge=0)
    num_taxonomic_relations: int = Field(..., description="Number of taxonomic relations", ge=0)
    num_non_taxonomic_relations: int = Field(..., description="Number of non-taxonomic relations", ge=0)

    class_distribution: Dict[str, int] = Field(..., description="Distribution of instances across classes")
    avg_terms_per_type: float = Field(..., description="Average number of terms per type", ge=0.0)


class OntologyMetrics(BaseModel):
    """
    Complete metrics collection for an ontology
    """
    name: str = Field(..., description="Name of the ontology")
    topology: TopologyMetrics = Field(..., description="Structural topology metrics")
    dataset: DatasetMetrics = Field(..., description="Dataset metrics")


class BenchmarkMetrics(BaseModel):
    """
    Aggregate metrics across multiple ontologies
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
