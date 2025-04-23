BBC Food Ontology
==========================

Overview
--------
The Food Ontology is a simple lightweight ontology for publishing data about recipes,
including the foods they are made from and the foods they create as well as the diets,
menus, seasons, courses and occasions they may be suitable for. Whilst it originates in a specific BBC use case,
the Food Ontology should be applicable to a wide range of recipe data publishing across the web.

:Domain: News & Media
:Category: Food & Beverage
:Current Version: 0.1
:Last Updated: 2014/03/18
:Creator: None
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Food Ontology Homepage <https://www.bbc.co.uk/ontologies/food-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 108
    - **Total Edges**: 267
    - **Root Nodes**: 0
    - **Leaf Nodes**: 63

Knowledge coverage
------------------
    - Classes: 17
    - Individuals: 0
    - Properties: 22

Hierarchical metrics
--------------------
    - **Maximum Depth**: 0
    - **Minimum Depth**: 0
    - **Average Depth**: 0.00
    - **Depth Variance**: 0.00

Breadth metrics
------------------
    - **Maximum Breadth**: 0
    - **Minimum Breadth**: 0
    - **Average Breadth**: 0.00
    - **Breadth Variance**: 0.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 5
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBCFood

    # Initialize and load ontology
    ontology = BBCFood()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
