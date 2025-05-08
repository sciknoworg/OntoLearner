Materials Design Ontology (MDO)
========================================================================================================================

Overview
--------
MDO is an ontology for materials design field, representing the domain knowledge specifically related
to solid-state physics and computational materials science.

:Domain: Materials Science and Engineering
:Category: Materials Design
:Current Version: 1.1
:Last Updated: 2022-08-02
:Creator: Materials Design Division, National Institute for Materials Science (NIMS)
:License: Creative Commons 4.0
:Format: OWL
:Download: `Materials Design Ontology (MDO) Homepage <https://github.com/LiUSemWeb/Materials-Design-Ontology/tree/master/>`_

Graph Metrics
-------------
    - **Total Nodes**: 76
    - **Total Edges**: 137
    - **Root Nodes**: 14
    - **Leaf Nodes**: 24

Knowledge coverage
------------------
    - Classes: 13
    - Individuals: 2
    - Properties: 13

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.46
    - **Depth Variance**: 0.33

Breadth metrics
------------------
    - **Maximum Breadth**: 14
    - **Minimum Breadth**: 1
    - **Average Breadth**: 8.00
    - **Breadth Variance**: 28.67

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 2
    - **Taxonomic Relations**: 3
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 2.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MDO

    # Initialize and load ontology
    ontology = MDO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
