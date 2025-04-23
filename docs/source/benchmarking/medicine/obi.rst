Ontology for Biomedical Investigations (OBI)
==========================

Overview
--------
The Ontology for Biomedical Investigations (OBI) helps you communicate clearly about scientific investigations
by defining more than 2500 terms for assays, devices, objectives, and more.

:Domain: Medicine
:Category: Biomedical Investigations
:Current Version: None
:Last Updated: 2025-01-09
:Creator: None
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `Ontology for Biomedical Investigations (OBI) Homepage <https://github.com/obi-ontology/obi/tree/master>`_

Graph Metrics
-------------
    - **Total Nodes**: 40613
    - **Total Edges**: 104537
    - **Root Nodes**: 177
    - **Leaf Nodes**: 10917

Knowledge coverage
------------------
    - Classes: 9703
    - Individuals: 301
    - Properties: 94

Hierarchical metrics
--------------------
    - **Maximum Depth**: 28
    - **Minimum Depth**: 0
    - **Average Depth**: 5.15
    - **Depth Variance**: 23.70

Breadth metrics
------------------
    - **Maximum Breadth**: 386
    - **Minimum Breadth**: 1
    - **Average Breadth**: 81.62
    - **Breadth Variance**: 11040.03

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 288
    - **Taxonomic Relations**: 22953
    - **Non-taxonomic Relations**: 1121
    - **Average Terms per Type**: 6.70

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OBI

    # Initialize and load ontology
    ontology = OBI()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
