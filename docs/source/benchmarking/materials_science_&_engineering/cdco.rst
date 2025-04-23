Crystallographic Defect Core Ontology (CDCO)
==========================

Overview
--------
CDCO defines the common terminology shared across all types of crystallographic defects,
providing a unified framework for data integration in materials science.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 1.0.0
:Last Updated: None
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `Crystallographic Defect Core Ontology (CDCO) Homepage <https://github.com/OCDO/cdco>`_

Graph Metrics
-------------
    - **Total Nodes**: 85
    - **Total Edges**: 123
    - **Root Nodes**: 8
    - **Leaf Nodes**: 53

Knowledge coverage
------------------
    - Classes: 7
    - Individuals: 0
    - Properties: 2

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.11
    - **Depth Variance**: 0.10

Breadth metrics
------------------
    - **Maximum Breadth**: 8
    - **Minimum Breadth**: 1
    - **Average Breadth**: 4.50
    - **Breadth Variance**: 12.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 4
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CDCO

    # Initialize and load ontology
    ontology = CDCO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
