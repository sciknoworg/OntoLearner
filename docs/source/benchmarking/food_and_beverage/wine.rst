Wine Ontology (Wine)
========================================================================================================================

Overview
--------
A project to define an RDF style ontology for wines and the wine-industry

:Domain: Food & Beverage
:Category: Wine
:Current Version: None
:Last Updated: None
:Creator: None
:License: None
:Format: RDF/XML
:Download: `Wine Ontology (Wine) Homepage <https://github.com/UCDavisLibrary/wine-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 729
    - **Total Edges**: 1816
    - **Root Nodes**: 84
    - **Leaf Nodes**: 22

Knowledge coverage
------------------
    - Classes: 101
    - Individuals: 161
    - Properties: 13

Hierarchical metrics
--------------------
    - **Maximum Depth**: 41
    - **Minimum Depth**: 0
    - **Average Depth**: 3.51
    - **Depth Variance**: 29.20

Breadth metrics
------------------
    - **Maximum Breadth**: 164
    - **Minimum Breadth**: 1
    - **Average Breadth**: 17.19
    - **Breadth Variance**: 1612.73

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 161
    - **Taxonomic Relations**: 504
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 4.13

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import Wine

    # Initialize and load ontology
    ontology = Wine()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
