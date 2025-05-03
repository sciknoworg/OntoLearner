BBC Creative Work Ontology (BBCCreativeWork)
========================================================================================================================

Overview
--------
This ontology defines the terms required to describe the creative works produced by the BBC and their associated metadata.
This ontology powers reading and writing creative works in the triplestore using tags associated with them (about)
their more specific types (BlogPost, NewsItem, Programme) and audiences (audience).

:Domain: News & Media
:Category: Creative Work
:Current Version: 1.19
:Last Updated: 2012-12-01
:Creator: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Creative Work Ontology (BBCCreativeWork) Homepage <https://www.bbc.co.uk/ontologies/creative-work-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 137
    - **Total Edges**: 300
    - **Root Nodes**: 0
    - **Leaf Nodes**: 80

Knowledge coverage
------------------
    - Classes: 20
    - Individuals: 15
    - Properties: 21

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
    - **Term Types**: 15
    - **Taxonomic Relations**: 17
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 5.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBCCreativeWork

    # Initialize and load ontology
    ontology = BBCCreativeWork()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
