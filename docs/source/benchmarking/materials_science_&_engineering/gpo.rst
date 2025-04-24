General Process Ontology (GPO)
========================================================================================================================

Overview
--------
Basically, this ontology aims to model processes. Processes are holistic perspective elements
that transform inputs/educts (matter, energy, information) into output/products (matter, energy, information)
with the help of tools (devices, algorithms). They can be decomposed into sub-processes
and have predecessor and successor processes.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: None
:Last Updated: None
:Creator: Simon Stier
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `General Process Ontology (GPO) Homepage <https://github.com/General-Process-Ontology/ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 548
    - **Total Edges**: 923
    - **Root Nodes**: 99
    - **Leaf Nodes**: 270

Knowledge coverage
------------------
    - Classes: 187
    - Individuals: 0
    - Properties: 17

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 1.41
    - **Depth Variance**: 1.20

Breadth metrics
------------------
    - **Maximum Breadth**: 223
    - **Minimum Breadth**: 3
    - **Average Breadth**: 76.14
    - **Breadth Variance**: 5799.55

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 516
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import GPO

    # Initialize and load ontology
    ontology = GPO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
