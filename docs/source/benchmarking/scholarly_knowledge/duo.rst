Data Use Ontology (DUO)
==========================

Overview
--------
DUO is an ontology which represent data use conditions.

:Domain: Scholarly Knowledge
:Category: Scholarly Knowledge
:Current Version: 1.0
:Last Updated: 2025-02-17
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `Data Use Ontology (DUO) Homepage <https://terminology.tib.eu/ts/ontologies/DUO/>`_

Graph Metrics
-------------
    - **Total Nodes**: 476
    - **Total Edges**: 583
    - **Root Nodes**: 196
    - **Leaf Nodes**: 168

Knowledge coverage
------------------
    - Classes: 45
    - Individuals: 0
    - Properties: 1

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 0.30
    - **Depth Variance**: 0.32

Breadth metrics
------------------
    - **Maximum Breadth**: 196
    - **Minimum Breadth**: 1
    - **Average Breadth**: 65.50
    - **Breadth Variance**: 6073.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 309
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import DUO

    # Initialize and load ontology
    ontology = DUO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
