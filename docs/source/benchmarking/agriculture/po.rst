Plant Ontology (PO)
========================================================================================================================

Overview
--------
The Plant Ontology (PO) is a structured vocabulary and database resource that links plant anatomy,
morphology and growth and development to plant genomics data.

:Domain: Agriculture
:Category: Plant Anatomy, Morphology, Growth and Development
:Current Version: None
:Last Updated: None
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `Plant Ontology (PO) Homepage <https://github.com/Planteome/plant-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 20790
    - **Total Edges**: 60638
    - **Root Nodes**: 5936
    - **Leaf Nodes**: 11639

Knowledge coverage
------------------
    - Classes: 1874
    - Individuals: 0
    - Properties: 13

Hierarchical metrics
--------------------
    - **Maximum Depth**: 5
    - **Minimum Depth**: 0
    - **Average Depth**: 1.07
    - **Depth Variance**: 0.72

Breadth metrics
------------------
    - **Maximum Breadth**: 8034
    - **Minimum Breadth**: 82
    - **Average Breadth**: 3462.50
    - **Breadth Variance**: 11752362.58

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2863
    - **Non-taxonomic Relations**: 36
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PO

    # Initialize and load ontology
    ontology = PO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
