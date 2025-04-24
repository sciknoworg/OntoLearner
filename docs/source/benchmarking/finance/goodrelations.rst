Good Relations Language Reference (GoodRelations)
========================================================================================================================

Overview
--------
GoodRelations is a standardized vocabulary (also known as "schema", "data dictionary",
or "ontology") for product, price, store, and company data that can (1) be embedded
into existing static and dynamic Web pages and that (2) can be processed by other computers.
This increases the visibility of your products and services in the latest generation
of search engines, recommender systems, and other novel applications.

:Domain: Finance
:Category: E-commerce
:Current Version: 1.0
:Last Updated: 2011-10-01
:Creator: Martin Hepp
:License: Creative Commons 3.0
:Format: RDF/XML
:Download: `Good Relations Language Reference (GoodRelations) Homepage <https://www.heppnetz.de/ontologies/goodrelations/v1>`_

Graph Metrics
-------------
    - **Total Nodes**: 677
    - **Total Edges**: 1816
    - **Root Nodes**: 18
    - **Leaf Nodes**: 206

Knowledge coverage
------------------
    - Classes: 98
    - Individuals: 47
    - Properties: 102

Hierarchical metrics
--------------------
    - **Maximum Depth**: 30
    - **Minimum Depth**: 0
    - **Average Depth**: 7.81
    - **Depth Variance**: 73.22

Breadth metrics
------------------
    - **Maximum Breadth**: 33
    - **Minimum Breadth**: 2
    - **Average Breadth**: 5.77
    - **Breadth Variance**: 55.21

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 47
    - **Taxonomic Relations**: 25
    - **Non-taxonomic Relations**: 264
    - **Average Terms per Type**: 5.22

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import GoodRelations

    # Initialize and load ontology
    ontology = GoodRelations()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
