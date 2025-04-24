FAIR Vocabulary (FAIR)
========================================================================================================================

Overview
--------
This is the formal vocabulary (ontology) describing the FAIR principles.

:Domain: Upper Ontology
:Category: Data, Metadata
:Current Version: None
:Last Updated: None
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `FAIR Vocabulary (FAIR) Homepage <https://terminology.tib.eu/ts/ontologies/FAIR>`_

Graph Metrics
-------------
    - **Total Nodes**: 92
    - **Total Edges**: 180
    - **Root Nodes**: 9
    - **Leaf Nodes**: 37

Knowledge coverage
------------------
    - Classes: 7
    - Individuals: 19
    - Properties: 1

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.18
    - **Depth Variance**: 0.15

Breadth metrics
------------------
    - **Maximum Breadth**: 9
    - **Minimum Breadth**: 2
    - **Average Breadth**: 5.50
    - **Breadth Variance**: 12.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 19
    - **Taxonomic Relations**: 3
    - **Non-taxonomic Relations**: 3
    - **Average Terms per Type**: 9.50

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import FAIR

    # Initialize and load ontology
    ontology = FAIR()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
