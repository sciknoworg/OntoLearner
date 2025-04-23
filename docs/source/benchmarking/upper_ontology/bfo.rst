Basic Formal Ontology (BFO)
==========================

Overview
--------
The Basic Formal Ontology (BFO) is a small, upper-level ontology that describes
the basic types of entities in the world and how they relate to each other.

:Domain: Upper Ontology
:Category: Basic
:Current Version: 2.0
:Last Updated: 2020
:Creator: University at Buffalo
:License: Creative Commons 4.0
:Format: OWL, TTL
:Download: `Basic Formal Ontology (BFO) Homepage <https://github.com/BFO-ontology/BFO-2020/>`_

Graph Metrics
-------------
    - **Total Nodes**: 538
    - **Total Edges**: 1002
    - **Root Nodes**: 16
    - **Leaf Nodes**: 276

Knowledge coverage
------------------
    - Classes: 84
    - Individuals: 0
    - Properties: 40

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 4.21
    - **Depth Variance**: 6.56

Breadth metrics
------------------
    - **Maximum Breadth**: 54
    - **Minimum Breadth**: 1
    - **Average Breadth**: 19.79
    - **Breadth Variance**: 293.74

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 162
    - **Non-taxonomic Relations**: 18
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BFO

    # Initialize and load ontology
    ontology = BFO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
