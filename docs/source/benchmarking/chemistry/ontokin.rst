Chemical Kinetics Ontology (OntoKin)
========================================================================================================================

Overview
--------
OntoKin is an ontology developed for representing chemical kinetic reaction mechanisms.

:Domain: Chemistry
:Category: Chemistry
:Current Version: 1.0
:Last Updated: 08 February 2022
:Creator: IEEE
:License: Creative Commons 4.0
:Format: OWL
:Download: `Chemical Kinetics Ontology (OntoKin) Homepage <https://www.ontologyportal.org/>`_

Graph Metrics
-------------
    - **Total Nodes**: 407
    - **Total Edges**: 1011
    - **Root Nodes**: 122
    - **Leaf Nodes**: 103

Knowledge coverage
------------------
    - Classes: 83
    - Individuals: 0
    - Properties: 136

Hierarchical metrics
--------------------
    - **Maximum Depth**: 8
    - **Minimum Depth**: 0
    - **Average Depth**: 1.64
    - **Depth Variance**: 2.39

Breadth metrics
------------------
    - **Maximum Breadth**: 122
    - **Minimum Breadth**: 1
    - **Average Breadth**: 45.22
    - **Breadth Variance**: 1858.40

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 138
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OntoKin

    # Initialize and load ontology
    ontology = OntoKin()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
