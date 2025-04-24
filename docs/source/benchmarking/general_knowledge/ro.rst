Relation Ontology (RO)
========================================================================================================================

Overview
--------
The Relations Ontology (RO) is a collection of OWL relations (ObjectProperties) intended for use
across a wide variety of biological ontologies.

:Domain: General Knowledge
:Category: Relations
:Current Version: 2024-04-24
:Last Updated: 2024-04-24
:Creator: None
:License: CC0
:Format: OWL
:Download: `Relation Ontology (RO) Homepage <http://purl.obolibrary.org/obo/ro.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 4635
    - **Total Edges**: 10477
    - **Root Nodes**: 381
    - **Leaf Nodes**: 2650

Knowledge coverage
------------------
    - Classes: 88
    - Individuals: 2
    - Properties: 673

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 1.90
    - **Depth Variance**: 2.53

Breadth metrics
------------------
    - **Maximum Breadth**: 870
    - **Minimum Breadth**: 1
    - **Average Breadth**: 181.93
    - **Breadth Variance**: 70257.92

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 2
    - **Taxonomic Relations**: 98
    - **Non-taxonomic Relations**: 10
    - **Average Terms per Type**: 2.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import RO

    # Initialize and load ontology
    ontology = RO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
