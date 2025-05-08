Icon Ontology (ICON)
========================================================================================================================

Overview
--------
The ICON ontology deals with high granularity art interpretation. It was developed by conceptualizing
Panofsky's theory of levels of interpretation, therefore artworks can be described according
to Pre-iconographical, Iconographical and Iconological information.

:Domain: Arts and Humanities
:Category: Art History, Cultural Heritage
:Current Version: 2.1.0
:Last Updated: April 26th, 2024
:Creator: Knowledge Media Institute
:License: Creative Commons 4.0
:Format: OWL
:Download: `Icon Ontology (ICON) Homepage <https://w3id.org/icon/ontology/>`_

Graph Metrics
-------------
    - **Total Nodes**: 408
    - **Total Edges**: 1091
    - **Root Nodes**: 11
    - **Leaf Nodes**: 131

Knowledge coverage
------------------
    - Classes: 76
    - Individuals: 0
    - Properties: 68

Hierarchical metrics
--------------------
    - **Maximum Depth**: 12
    - **Minimum Depth**: 0
    - **Average Depth**: 5.92
    - **Depth Variance**: 13.34

Breadth metrics
------------------
    - **Maximum Breadth**: 13
    - **Minimum Breadth**: 5
    - **Average Breadth**: 8.62
    - **Breadth Variance**: 4.24

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 65
    - **Non-taxonomic Relations**: 4
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import ICON

    # Initialize and load ontology
    ontology = ICON()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
