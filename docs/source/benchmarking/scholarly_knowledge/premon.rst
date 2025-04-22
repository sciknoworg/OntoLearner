Pre-Modern Ontology (PreMOn)
==========================

Overview
--------
The PreMOn Ontology is an extension of lemon (W3C Ontology Lexicon Community Group, 2015)
for representing predicate models and their mappings. The Core Module of the PreMOn Ontology
defines the main abstractions for modelling semantic classes with their semantic roles,
mappings between different predicate models, and annotations.

:Domain: Scholarly Knowledge
:Category: Linguistics
:Current Version: 2018a
:Last Updated: 2018-02-15
:Creator: Francesco Corcoglioniti, Marco Rospocher <https://dkm.fbk.eu/rospocher>
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `Pre-Modern Ontology (PreMOn) Homepage <https://premon.fbk.eu/ontology/core#>`_

Graph Metrics
-------------
    - **Total Nodes**: 115
    - **Total Edges**: 213
    - **Root Nodes**: 13
    - **Leaf Nodes**: 45

Knowledge coverage
------------------
    - Classes: 15
    - Individuals: 0
    - Properties: 16

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 1.80
    - **Depth Variance**: 3.33

Breadth metrics
------------------
    - **Maximum Breadth**: 20
    - **Minimum Breadth**: 2
    - **Average Breadth**: 7.29
    - **Breadth Variance**: 38.49

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 50
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PreMOn

    # Initialize and load ontology
    ontology = PreMOn()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
