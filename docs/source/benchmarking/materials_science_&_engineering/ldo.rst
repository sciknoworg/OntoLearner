Line Defect Ontology (LDO)
==========================

Overview
--------
LDO is an ontology designed to describe line defects in crystalline materials,
such as dislocations and disclinations.

:Domain: Materials Science & Engineering
:Category: Materials Defects
:Current Version: 1.0.0
:Last Updated: None
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `Line Defect Ontology (LDO) Homepage <https://github.com/OCDO/ldo>`_

Graph Metrics
-------------
    - **Total Nodes**: 111
    - **Total Edges**: 207
    - **Root Nodes**: 6
    - **Leaf Nodes**: 49

Knowledge coverage
------------------
    - Classes: 30
    - Individuals: 0
    - Properties: 11

Hierarchical metrics
--------------------
    - **Maximum Depth**: 4
    - **Minimum Depth**: 0
    - **Average Depth**: 1.25
    - **Depth Variance**: 1.56

Breadth metrics
------------------
    - **Maximum Breadth**: 6
    - **Minimum Breadth**: 1
    - **Average Breadth**: 3.20
    - **Breadth Variance**: 2.96

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 21
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import LDO

    # Initialize and load ontology
    ontology = LDO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
