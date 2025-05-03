BBC Politics News Ontology (BBCPolitics)
========================================================================================================================

Overview
--------
The Politics Ontology describes the concepts that occur in BBC politics news.

:Domain: News & Media
:Category: Politics
:Current Version: 0.9
:Last Updated: 2014-01-06
:Creator: https://www.r4isstatic.com/
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Politics News Ontology (BBCPolitics) Homepage <https://www.bbc.co.uk/ontologies/politics-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 43
    - **Total Edges**: 75
    - **Root Nodes**: 0
    - **Leaf Nodes**: 30

Knowledge coverage
------------------
    - Classes: 7
    - Individuals: 0
    - Properties: 5

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
    - **Taxonomic Relations**: 6
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBCPolitics

    # Initialize and load ontology
    ontology = BBCPolitics()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
