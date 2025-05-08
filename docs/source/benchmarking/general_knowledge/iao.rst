Information Artifact Ontology (IAO)
========================================================================================================================

Overview
--------
The Information Artifact Ontology (IAO) is an ontology of information entities,
originally driven by work by the OBI digital entity and realizable information entity branch.

:Domain: General Knowledge
:Category: Information, Data, Knowledge
:Current Version: None
:Last Updated: 2022-11-07
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `Information Artifact Ontology (IAO) Homepage <https://terminology.tib.eu/ts/ontologies/IAO>`_

Graph Metrics
-------------
    - **Total Nodes**: 2303
    - **Total Edges**: 4720
    - **Root Nodes**: 151
    - **Leaf Nodes**: 1523

Knowledge coverage
------------------
    - Classes: 292
    - Individuals: 18
    - Properties: 57

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 2.05
    - **Depth Variance**: 4.06

Breadth metrics
------------------
    - **Maximum Breadth**: 280
    - **Minimum Breadth**: 1
    - **Average Breadth**: 63.00
    - **Breadth Variance**: 8210.29

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 18
    - **Taxonomic Relations**: 347
    - **Non-taxonomic Relations**: 19
    - **Average Terms per Type**: 6.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import IAO

    # Initialize and load ontology
    ontology = IAO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
