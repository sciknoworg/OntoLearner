Battery Value Chain Ontology (BVCO)
========================================================================================================================

Overview
--------
Basically, Battery Value Chain Ontology (BVCO) aims to model processes along the Battery value chain. Processes are
holistic perspective elements that transform inputs/educts (matter, energy, information)
into output/products (matter, energy, information) with the help of tools (devices, algorithms).
They can be decomposed into sub-processes and have predecessor and successor processes.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.4.3
:Last Updated: None
:Creator: Lukas Gold, Simon Stier
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Battery Value Chain Ontology (BVCO) Homepage <https://github.com/Battery-Value-Chain-Ontology/ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 804
    - **Total Edges**: 1719
    - **Root Nodes**: 85
    - **Leaf Nodes**: 283

Knowledge coverage
------------------
    - Classes: 262
    - Individuals: 0
    - Properties: 6

Hierarchical metrics
--------------------
    - **Maximum Depth**: 14
    - **Minimum Depth**: 0
    - **Average Depth**: 2.47
    - **Depth Variance**: 5.27

Breadth metrics
------------------
    - **Maximum Breadth**: 230
    - **Minimum Breadth**: 2
    - **Average Breadth**: 52.20
    - **Breadth Variance**: 4920.43

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1396
    - **Non-taxonomic Relations**: 5
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BVCO

    # Initialize and load ontology
    ontology = BVCO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
