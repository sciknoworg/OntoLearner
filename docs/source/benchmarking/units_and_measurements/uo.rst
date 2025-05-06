Units of Measurement Ontology (UO)
========================================================================================================================

Overview
--------
Metrical units for use in conjunction with PATO.

:Domain: Units and Measurements
:Category: Units and Measurements
:Current Version: None
:Last Updated: 2023-05-25
:Creator: KAUST
:License: Creative Commons 3.0
:Format: OWL
:Download: `Units of Measurement Ontology (UO) Homepage <https://bioportal.bioontology.org/ontologies/UO>`_

Graph Metrics
-------------
    - **Total Nodes**: 2284
    - **Total Edges**: 5354
    - **Root Nodes**: 6
    - **Leaf Nodes**: 754

Knowledge coverage
------------------
    - Classes: 928
    - Individuals: 0
    - Properties: 2

Hierarchical metrics
--------------------
    - **Maximum Depth**: 4
    - **Minimum Depth**: 0
    - **Average Depth**: 1.14
    - **Depth Variance**: 1.12

Breadth metrics
------------------
    - **Maximum Breadth**: 11
    - **Minimum Breadth**: 1
    - **Average Breadth**: 4.40
    - **Breadth Variance**: 13.84

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 708
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import UO

    # Initialize and load ontology
    ontology = UO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
