Schema.org Ontology (SchemaOrg)
==========================

Overview
--------
Schema.org is a collaborative, community activity with a mission to create,
maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond.

:Domain: General Knowledge
:Category: Web Development
:Current Version: 28.1
:Last Updated: 2024-11-22
:Creator: Schema.org Community
:License: Creative Commons 4.0
:Format: OWL
:Download: `Schema.org Ontology (SchemaOrg) Homepage <https://github.com/schemaorg/schemaorg/blob/main/data/releases/28.1/schemaorg.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 15044
    - **Total Edges**: 32425
    - **Root Nodes**: 0
    - **Leaf Nodes**: 2128

Knowledge coverage
------------------
    - Classes: 3881
    - Individuals: 0
    - Properties: 1485

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
    - **Taxonomic Relations**: 1058
    - **Non-taxonomic Relations**: 635
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SchemaOrg

    # Initialize and load ontology
    ontology = SchemaOrg()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
