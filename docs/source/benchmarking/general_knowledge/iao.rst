Information Artifact Ontology (IAO)
===================================

Overview
-----------------
The Information Artifact Ontology (IAO) is an ontology of information entities,
originally driven by work by the OBI digital entity and realizable information entity branch.

:Domain: General Knowledge
:Category: Information, Data, Knowledge
:Current Version:
:Last Updated: 2022-11-07
:Producer:
:License: Creative Commons 4.0
:Format: OWL
:Download: `IAO Homepage <https://terminology.tib.eu/ts/ontologies/IAO>`_
:Documentation: `IAO Documentation <https://terminology.tib.eu/ts/ontologies/IAO>`_

Base Metrics
---------------
    - Classes: 263
    - Individuals: 127
    - Properties: 20

Graph Metrics:
------------------
    - **Total Nodes**: 2303
    - **Root Nodes**: 151
    - **Leaf Nodes**: 1523
    - **Maximum Depth**: 17
    - **Edges**: 4720

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 18
    - **Taxonomic Relations**: 567
    - **Non-taxonomic Relations**: 35
    - **Average Terms per Type**: 1.06

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import IAO

    # Initialize and load ontology
    ontology = IAO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
