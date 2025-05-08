General Formal Ontology (GFO)
========================================================================================================================

Overview
--------
The General Formal Ontology is a top-level ontology for conceptual modeling,
which is being constantly further developed by Onto-Med. It includes elaborations of categories like objects,
processes, time and space, properties, relations, roles, functions, facts, and situations.
Moreover, we are working on an integration with the notion of levels of reality in order
to more appropriately capture entities in the material, mental, and social areas.

:Domain: Upper Ontology
:Category: Upper Ontology
:Current Version: None
:Last Updated: 2024-11-18
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `General Formal Ontology (GFO) Homepage <https://onto-med.github.io/GFO/release/2024-11-18/index-en.html>`_

Graph Metrics
-------------
    - **Total Nodes**: 296
    - **Total Edges**: 708
    - **Root Nodes**: 42
    - **Leaf Nodes**: 71

Knowledge coverage
------------------
    - Classes: 94
    - Individuals: 1
    - Properties: 67

Hierarchical metrics
--------------------
    - **Maximum Depth**: 12
    - **Minimum Depth**: 0
    - **Average Depth**: 1.94
    - **Depth Variance**: 3.22

Breadth metrics
------------------
    - **Maximum Breadth**: 88
    - **Minimum Breadth**: 1
    - **Average Breadth**: 21.23
    - **Breadth Variance**: 874.02

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 143
    - **Non-taxonomic Relations**: 34
    - **Average Terms per Type**: 1.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import GFO

    # Initialize and load ontology
    ontology = GFO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
