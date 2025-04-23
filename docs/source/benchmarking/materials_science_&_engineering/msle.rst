Material Science Lab Equipment Ontology (MSLE)
==========================

Overview
--------
The current ontology describes Material Science Lab Equipment.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 1.1
:Last Updated: Sep 15, 2022
:Creator: None
:License: None
:Format: TTL
:Download: `Material Science Lab Equipment Ontology (MSLE) Homepage <https://github.com/MehrdadJalali-AI/MSLE-Ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 146
    - **Total Edges**: 479
    - **Root Nodes**: 16
    - **Leaf Nodes**: 52

Knowledge coverage
------------------
    - Classes: 45
    - Individuals: 3
    - Properties: 10

Hierarchical metrics
--------------------
    - **Maximum Depth**: 7
    - **Minimum Depth**: 0
    - **Average Depth**: 1.77
    - **Depth Variance**: 1.70

Breadth metrics
------------------
    - **Maximum Breadth**: 53
    - **Minimum Breadth**: 1
    - **Average Breadth**: 17.75
    - **Breadth Variance**: 353.69

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 4
    - **Taxonomic Relations**: 83
    - **Non-taxonomic Relations**: 229
    - **Average Terms per Type**: 0.16

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MSLE

    # Initialize and load ontology
    ontology = MSLE()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
