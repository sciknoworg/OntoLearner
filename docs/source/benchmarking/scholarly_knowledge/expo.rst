Ontology of Scientific Experiments (EXPO)
========================================================================================================================

Overview
--------
Formalise generic knowledge about scientific experimental design, methodology, and results representation.

:Domain: Scholarly Knowledge
:Category: Scientific Experiments
:Current Version: None
:Last Updated: None
:Creator: None
:License: Academic Free License (AFL)
:Format: OWL
:Download: `Ontology of Scientific Experiments (EXPO) Homepage <https://expo.sourceforge.net/>`_

Graph Metrics
-------------
    - **Total Nodes**: 858
    - **Total Edges**: 2921
    - **Root Nodes**: 13
    - **Leaf Nodes**: 265

Knowledge coverage
------------------
    - Classes: 347
    - Individuals: 0
    - Properties: 78

Hierarchical metrics
--------------------
    - **Maximum Depth**: 19
    - **Minimum Depth**: 0
    - **Average Depth**: 6.55
    - **Depth Variance**: 13.84

Breadth metrics
------------------
    - **Maximum Breadth**: 71
    - **Minimum Breadth**: 1
    - **Average Breadth**: 24.15
    - **Breadth Variance**: 438.53

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1012
    - **Non-taxonomic Relations**: 726
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import EXPO

    # Initialize and load ontology
    ontology = EXPO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
