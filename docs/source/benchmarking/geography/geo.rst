Geographical Entities Ontology (GEO)
========================================================================================================================

Overview
--------
Geographical Entities Ontology (GEO) is an inventory of geopolitical entities (such as sovereign states
and their administrative subdivisions) as well as various geographical regions (including but not limited
to the specific ones over which the governments have jurisdiction)

:Domain: Geography
:Category: Geographic Knowledge
:Current Version: None
:Last Updated: 2019-02-17
:Creator: William R Hogan
:License: Creative Commons 4.0
:Format: OWL
:Download: `Geographical Entities Ontology (GEO) Homepage <http://purl.obolibrary.org/obo/geo.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 108572
    - **Total Edges**: 246406
    - **Root Nodes**: 298
    - **Leaf Nodes**: 54170

Knowledge coverage
------------------
    - Classes: 397
    - Individuals: 46948
    - Properties: 75

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 1.91
    - **Depth Variance**: 3.77

Breadth metrics
------------------
    - **Maximum Breadth**: 356
    - **Minimum Breadth**: 2
    - **Average Breadth**: 95.79
    - **Breadth Variance**: 17126.60

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 46949
    - **Taxonomic Relations**: 664
    - **Non-taxonomic Relations**: 19
    - **Average Terms per Type**: 1805.73

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import GEO

    # Initialize and load ontology
    ontology = GEO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
