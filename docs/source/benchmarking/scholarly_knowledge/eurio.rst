EUropean Research Information Ontology
==========================

Overview
--------
EURIO (EUropean Research Information Ontology) conceptualises, formally encodes and makes available in an open,
structured and machine-readable format data about resarch projects funded by the EU's
framework programmes for research and innovation.

:Domain: Scholarly Knowledge
:Category: Research Information
:Current Version: 2.4
:Last Updated: 2023-10-19
:Creator: Publications Office of the European Commission
:License: Creative Commons 4.0
:Format: RDF
:Download: `EUropean Research Information Ontology Homepage <https://op.europa.eu/de/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurio>`_

Graph Metrics
-------------
    - **Total Nodes**: 502
    - **Total Edges**: 1193
    - **Root Nodes**: 18
    - **Leaf Nodes**: 204

Knowledge coverage
------------------
    - Classes: 44
    - Individuals: 0
    - Properties: 111

Hierarchical metrics
--------------------
    - **Maximum Depth**: 14
    - **Minimum Depth**: 0
    - **Average Depth**: 6.54
    - **Depth Variance**: 11.75

Breadth metrics
------------------
    - **Maximum Breadth**: 56
    - **Minimum Breadth**: 4
    - **Average Breadth**: 24.73
    - **Breadth Variance**: 192.33

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 700
    - **Non-taxonomic Relations**: 4
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import EURIO

    # Initialize and load ontology
    ontology = EURIO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
