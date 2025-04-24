Product Types Ontology (PTO)
========================================================================================================================

Overview
--------
The Product Types Ontology is designed to be used in combination with GoodRelations,
a standard vocabulary for the commercial aspects of offers.

:Domain: Industry
:Category: Industry
:Current Version: 1.0
:Last Updated: 2025-02-21
:Creator: Martin Hepp
:License: Creative Commons 3.0
:Format: RDF, OWL, TTL, CSV, NT
:Download: `Product Types Ontology (PTO) Homepage <http://www.productontology.org/>`_

Graph Metrics
-------------
    - **Total Nodes**: 4577
    - **Total Edges**: 14125
    - **Root Nodes**: 12
    - **Leaf Nodes**: 1012

Knowledge coverage
------------------
    - Classes: 1002
    - Individuals: 3002
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.92
    - **Depth Variance**: 0.87

Breadth metrics
------------------
    - **Maximum Breadth**: 12
    - **Minimum Breadth**: 3
    - **Average Breadth**: 8.33
    - **Breadth Variance**: 14.89

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 3001
    - **Taxonomic Relations**: 4000
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 3001.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PTO

    # Initialize and load ontology
    ontology = PTO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
