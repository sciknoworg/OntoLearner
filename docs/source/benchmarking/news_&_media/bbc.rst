BBC Ontology (BBC)
========================================================================================================================

Overview
--------
The BBC ontology codifies the logic that connects web documents, BBC products and platforms
for which content is available. Currently, there are 10 major products in Future Media
which produce content for BBC online. The majority of those contain more products dedicated in thematic areas,
for example Education propositions are part of the K&L (Knowledge and Learning) product portfolio.

:Domain: News & Media
:Category: News
:Current Version: 1.37
:Last Updated: 2012-12-01
:Creator: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Ontology (BBC) Homepage <https://www.bbc.co.uk/ontologies/bbc-ontology/>`_

Graph Metrics
-------------
    - **Total Nodes**: 164
    - **Total Edges**: 316
    - **Root Nodes**: 0
    - **Leaf Nodes**: 101

Knowledge coverage
------------------
    - Classes: 25
    - Individuals: 10
    - Properties: 24

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
    - **Term Types**: 10
    - **Taxonomic Relations**: 35
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 5.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBC

    # Initialize and load ontology
    ontology = BBC()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
