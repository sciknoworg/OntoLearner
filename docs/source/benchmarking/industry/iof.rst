Industrial Ontology Foundry (IOF)
========================================================================================================================

Overview
--------
The IOF Core Ontology contains notions found to be common across multiple manufacturing domains.
This file is an RDF implementation of these notions. The ontology utilizes the Basic Formal Ontology or BFO
as a top-level ontology but also borrows terms from various domain-independent or mid-level ontologies.
The purpose of the ontology is to serve as a foundation for ensuring consistency
and interoperability across various domain-specific reference ontologies the IOF publishes.

:Domain: Industry
:Category: Scholarly Knowledge
:Current Version: 1.0
:Last Updated: 2020
:Creator: IOF Core Working Group
:License: MIT
:Format: RDF
:Download: `Industrial Ontology Foundry (IOF) Homepage <https://oagi.org/pages/Released-Ontologies>`_

Graph Metrics
-------------
    - **Total Nodes**: 1442
    - **Total Edges**: 2686
    - **Root Nodes**: 13
    - **Leaf Nodes**: 716

Knowledge coverage
------------------
    - Classes: 212
    - Individuals: 0
    - Properties: 51

Hierarchical metrics
--------------------
    - **Maximum Depth**: 36
    - **Minimum Depth**: 0
    - **Average Depth**: 7.89
    - **Depth Variance**: 35.71

Breadth metrics
------------------
    - **Maximum Breadth**: 117
    - **Minimum Breadth**: 1
    - **Average Breadth**: 24.32
    - **Breadth Variance**: 922.11

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 87
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import IOF

    # Initialize and load ontology
    ontology = IOF()
    ontology.load("path/to/ontology.RDF")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
