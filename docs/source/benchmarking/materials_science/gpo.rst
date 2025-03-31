General Process Ontology (GPO)
==============================

Overview
-----------------
Basically, this ontology aims to model processes. Processes are holistic perspective elements
that transform inputs/educts (matter, energy, information) into output/products (matter, energy, information)
with the help of tools (devices, algorithms). They can be decomposed into sub-processes
and have predecessor and successor processes.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version:
:Last Updated:
:Producer: Simon Stier
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: Turtle
:Download: `GPO Homepage <https://github.com/General-Process-Ontology/ontology>`_
:Documentation: `GPO Documentation <https://github.com/General-Process-Ontology/ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics
------------------
    - **Total Nodes**: 548
    - **Root Nodes**: 99
    - **Leaf Nodes**: 270
    - **Maximum Depth**: 15
    - **Edges**: 923

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 516
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import GPO

    # Initialize and load ontology
    ontology = GPO()
    ontology.load("path/to/gpo.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
