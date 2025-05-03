BBC Business News Ontology (BBCBusiness)
========================================================================================================================

Overview
--------
The Business News Ontology describes the concepts that occur in BBC business news.

:Domain: News & Media
:Category: Business News
:Current Version: 0.5
:Last Updated: 2014-11-09
:Creator: https://www.bbc.co.uk/blogs/internet/authors/Jeremy_Tarling, https://uk.linkedin.com/in/amaalmohamed
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Business News Ontology (BBCBusiness) Homepage <https://www.bbc.co.uk/ontologies/business-news-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 50
    - **Total Edges**: 95
    - **Root Nodes**: 0
    - **Leaf Nodes**: 35

Knowledge coverage
------------------
    - Classes: 5
    - Individuals: 0
    - Properties: 10

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

    from ontolearner.ontology import BBCBusiness

    # Initialize and load ontology
    ontology = BBCBusiness()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
