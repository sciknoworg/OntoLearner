Juso Ontology
==========================

Overview
--------
Juso Ontology is a Web vocabulary for describing geographical addresses and features.

:Domain: Geography
:Category: geographical knowledge
:Current Version: 0.1.1
:Last Updated: 2015-11-10
:Creator: James G. Kim, LiST Inc.
:License: Creative Commons 4.0
:Format: TTL
:Download: `Juso Ontology Homepage <https://rdfs.co/juso/0.1.1/html>`_

Graph Metrics
-------------
    - **Total Nodes**: 319
    - **Total Edges**: 607
    - **Root Nodes**: 19
    - **Leaf Nodes**: 227

Knowledge coverage
------------------
    - Classes: 30
    - Individuals: 0
    - Properties: 24

Hierarchical metrics
--------------------
    - **Maximum Depth**: 5
    - **Minimum Depth**: 0
    - **Average Depth**: 1.93
    - **Depth Variance**: 1.85

Breadth metrics
------------------
    - **Maximum Breadth**: 37
    - **Minimum Breadth**: 4
    - **Average Breadth**: 21.33
    - **Breadth Variance**: 132.89

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 61
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import Juso

    # Initialize and load ontology
    ontology = Juso()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
