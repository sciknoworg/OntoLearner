Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE)
========================================================================================================================

Overview
--------
The Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE) is a foundational ontology
that provides a conceptual framework for the formalization of domain ontologies.

:Domain: Upper Ontology
:Category: Linguistics, Cognitive Science
:Current Version: None
:Last Updated: None
:Creator: Laboratory for Applied Ontology, ISTC-CNR
:License: Creative Commons 4.0
:Format: OWL, RDF/XML, TTL
:Download: `Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE) Homepage <https://www.loa.istc.cnr.it/index.php/dolce/>`_

Graph Metrics
-------------
    - **Total Nodes**: 252
    - **Total Edges**: 689
    - **Root Nodes**: 10
    - **Leaf Nodes**: 86

Knowledge coverage
------------------
    - Classes: 44
    - Individuals: 0
    - Properties: 70

Hierarchical metrics
--------------------
    - **Maximum Depth**: 9
    - **Minimum Depth**: 0
    - **Average Depth**: 3.37
    - **Depth Variance**: 4.11

Breadth metrics
------------------
    - **Maximum Breadth**: 28
    - **Minimum Breadth**: 1
    - **Average Breadth**: 14.20
    - **Breadth Variance**: 75.56

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 231
    - **Non-taxonomic Relations**: 18
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import DOLCE

    # Initialize and load ontology
    ontology = DOLCE()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
