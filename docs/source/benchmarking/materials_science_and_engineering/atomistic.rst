Atomistic Ontology (Atomistic)
========================================================================================================================

Overview
--------
An EMMO-based domain ontology for atomistic and electronic modelling.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.0.2
:Last Updated: None
:Creator: Francesca L. Bleken, Jesper Friis
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: Turtle
:Download: `Atomistic Ontology (Atomistic) Homepage <https://github.com/emmo-repo/domain-atomistic>`_

Graph Metrics
-------------
    - **Total Nodes**: 93
    - **Total Edges**: 107
    - **Root Nodes**: 11
    - **Leaf Nodes**: 70

Knowledge coverage
------------------
    - Classes: 12
    - Individuals: 0
    - Properties: 2

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 1.80
    - **Depth Variance**: 2.27

Breadth metrics
------------------
    - **Maximum Breadth**: 44
    - **Minimum Breadth**: 3
    - **Average Breadth**: 13.29
    - **Breadth Variance**: 182.78

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 38
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import Atomistic

    # Initialize and load ontology
    ontology = Atomistic()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
