Phenotype and Trait Ontology (PATO)
==========================

Overview
--------
An ontology of phenotypic qualities (properties, attributes or characteristics).

:Domain: Biology & Life Sciences
:Category: Biology
:Current Version: 1.2
:Last Updated: 2025-02-01
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `Phenotype and Trait Ontology (PATO) Homepage <https://terminology.tib.eu/ts/ontologies/PATO>`_

Graph Metrics
-------------
    - **Total Nodes**: 98691
    - **Total Edges**: 259386
    - **Root Nodes**: 16564
    - **Leaf Nodes**: 45644

Knowledge coverage
------------------
    - Classes: 13544
    - Individuals: 0
    - Properties: 252

Hierarchical metrics
--------------------
    - **Maximum Depth**: 20
    - **Minimum Depth**: 0
    - **Average Depth**: 1.73
    - **Depth Variance**: 2.02

Breadth metrics
------------------
    - **Maximum Breadth**: 35876
    - **Minimum Breadth**: 1
    - **Average Breadth**: 4564.14
    - **Breadth Variance**: 92888669.36

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 62605
    - **Non-taxonomic Relations**: 5456
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PATO

    # Initialize and load ontology
    ontology = PATO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
