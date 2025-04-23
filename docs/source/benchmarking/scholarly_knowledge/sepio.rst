Scientific Evidence and Provenance Information Ontology (SEPIO)
==========================

Overview
--------
The SEPIO ontology is in its early stages of development, undergoing iterative refinement
as new requirements emerge and alignment with existing standards is explored. The SEPIO core file imports two files
which can be resolved at the URLs below:
IAO ontology-metadata import: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/imports/ontology-metadata.owl
bfo mireot: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/mireots/bfo-mireot.owl

:Domain: Scholarly Knowledge
:Category: Scientific Evidence
:Current Version: None
:Last Updated: 2015-02-23
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `Scientific Evidence and Provenance Information Ontology (SEPIO) Homepage <https://terminology.tib.eu/ts/ontologies/SEPIO>`_

Graph Metrics
-------------
    - **Total Nodes**: 1262
    - **Total Edges**: 2385
    - **Root Nodes**: 72
    - **Leaf Nodes**: 781

Knowledge coverage
------------------
    - Classes: 129
    - Individuals: 21
    - Properties: 117

Hierarchical metrics
--------------------
    - **Maximum Depth**: 14
    - **Minimum Depth**: 0
    - **Average Depth**: 3.17
    - **Depth Variance**: 8.36

Breadth metrics
------------------
    - **Maximum Breadth**: 170
    - **Minimum Breadth**: 1
    - **Average Breadth**: 40.60
    - **Breadth Variance**: 2186.24

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 21
    - **Taxonomic Relations**: 223
    - **Non-taxonomic Relations**: 12
    - **Average Terms per Type**: 1.11

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SEPIO

    # Initialize and load ontology
    ontology = SEPIO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
