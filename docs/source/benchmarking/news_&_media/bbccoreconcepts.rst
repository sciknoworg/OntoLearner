BBC Core Concepts Ontology (BBCCoreConcepts)
========================================================================================================================

Overview
--------
The generic BBC ontology for people, places, events, organisations, themes which represent things
that make sense across the BBC. This model is meant to be generic enough, and allow clients (domain experts)
link their own concepts e.g., athletes or politicians using rdfs:sublClassOf the particular concept.

:Domain: News & Media
:Category: Core Concepts
:Current Version: 1.30
:Last Updated: 2019-11-21
:Creator: jeremy.tarling@bbc.co.uk, tom.hodgkinson@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Core Concepts Ontology (BBCCoreConcepts) Homepage <https://www.bbc.co.uk/ontologies/core-concepts-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 122
    - **Total Edges**: 265
    - **Root Nodes**: 4
    - **Leaf Nodes**: 73

Knowledge coverage
------------------
    - Classes: 22
    - Individuals: 0
    - Properties: 29

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 1.35
    - **Depth Variance**: 0.63

Breadth metrics
------------------
    - **Maximum Breadth**: 11
    - **Minimum Breadth**: 4
    - **Average Breadth**: 6.67
    - **Breadth Variance**: 9.56

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 25
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBCCoreConcepts

    # Initialize and load ontology
    ontology = BBCCoreConcepts()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
