Crystallography Ontology (EMMOCrystallography)
==========================

Overview
--------
A crystallography domain ontology based on EMMO and the CIF core dictionary. It is implemented as a formal language.

:Domain: Materials Science & Engineering
:Category: Crystallography
:Current Version: 0.0.1
:Last Updated: None
:Creator: None
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: Turtle
:Download: `Crystallography Ontology (EMMOCrystallography) Homepage <https://github.com/emmo-repo/domain-crystallography>`_

Graph Metrics
-------------
    - **Total Nodes**: 337
    - **Total Edges**: 586
    - **Root Nodes**: 29
    - **Leaf Nodes**: 166

Knowledge coverage
------------------
    - Classes: 61
    - Individuals: 0
    - Properties: 5

Hierarchical metrics
--------------------
    - **Maximum Depth**: 14
    - **Minimum Depth**: 0
    - **Average Depth**: 5.20
    - **Depth Variance**: 9.99

Breadth metrics
------------------
    - **Maximum Breadth**: 74
    - **Minimum Breadth**: 1
    - **Average Breadth**: 22.07
    - **Breadth Variance**: 290.60

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 331
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import EMMOCrystallography

    # Initialize and load ontology
    ontology = EMMOCrystallography()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
