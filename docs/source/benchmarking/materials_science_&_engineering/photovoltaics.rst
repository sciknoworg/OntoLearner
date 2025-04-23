EMMO Domain Ontology for Photovoltaics (Photovoltaics)
==========================

Overview
--------
This ontology is describing Perovskite solar cells.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.0.1
:Last Updated: None
:Creator: Casper Welzel Andersen, Simon Clark
:License: Creative Commons license Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `EMMO Domain Ontology for Photovoltaics (Photovoltaics) Homepage <https://github.com/emmo-repo/domain-photovoltaics>`_

Graph Metrics
-------------
    - **Total Nodes**: 131
    - **Total Edges**: 281
    - **Root Nodes**: 12
    - **Leaf Nodes**: 48

Knowledge coverage
------------------
    - Classes: 47
    - Individuals: 0
    - Properties: 3

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.40
    - **Depth Variance**: 0.24

Breadth metrics
------------------
    - **Maximum Breadth**: 12
    - **Minimum Breadth**: 8
    - **Average Breadth**: 10.00
    - **Breadth Variance**: 4.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 140
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import Photovoltaics

    # Initialize and load ontology
    ontology = Photovoltaics()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
