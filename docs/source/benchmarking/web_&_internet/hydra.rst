Hydra Ontology
==========================

Overview
--------
Hydra is a lightweight vocabulary to create hypermedia-driven Web APIs. By specifying a number of concepts
commonly used in Web APIs it enables the creation of generic API clients.

:Domain: Web & Internet
:Category: Web Development
:Current Version: None
:Last Updated: 13 July 2021
:Creator: Hydra W3C Community Group
:License: Creative Commons 4.0
:Format: JSON-LD, RDF, TTL
:Download: `Hydra Ontology Homepage <https://www.hydra-cg.com/spec/latest/core/#references>`_

Graph Metrics
-------------
    - **Total Nodes**: 154
    - **Total Edges**: 452
    - **Root Nodes**: 0
    - **Leaf Nodes**: 86

Knowledge coverage
------------------
    - Classes: 2
    - Individuals: 14
    - Properties: 0

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
    - **Term Types**: 14
    - **Taxonomic Relations**: 15
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 1.56

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import Hydra

    # Initialize and load ontology
    ontology = Hydra()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
