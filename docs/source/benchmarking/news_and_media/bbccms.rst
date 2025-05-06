BBC CMS Ontology (BBCCMS)
========================================================================================================================

Overview
--------
The Content Management Systems ontology defines the terms that LDP needs to interact with systems that produce content.
The linked data platform contain semantic metadata for the creative content and also the things the BBC produces content about.
The CMS ontology defines how these things and content are associated with other BBC instances of the same thing.

:Domain: News and Media
:Category: Content Management Systems
:Current Version: 3.7
:Last Updated: 2012-12-01
:Creator: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC CMS Ontology (BBCCMS) Homepage <https://www.bbc.co.uk/ontologies/cms-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 68
    - **Total Edges**: 137
    - **Root Nodes**: 0
    - **Leaf Nodes**: 41

Knowledge coverage
------------------
    - Classes: 20
    - Individuals: 4
    - Properties: 2

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
    - **Term Types**: 4
    - **Taxonomic Relations**: 17
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 4.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBCCMS

    # Initialize and load ontology
    ontology = BBCCMS()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
