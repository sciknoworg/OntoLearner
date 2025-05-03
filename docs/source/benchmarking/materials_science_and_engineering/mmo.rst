Materials Mechanics Ontology (MMO)
========================================================================================================================

Overview
--------
The materials mechanics ontology is an application-level ontology that was created
for supporting named entity recognition tasks for materials fatigue domain. The ontology covers
some fairly general MSE concepts that could prospectively be merged into PMDco or other upper materials ontologies
such as descriptions of crystallographic defects and microstructural entities.
Furthermore, concepts related to the materials fatigue subdomain are also heavily incorporated.

:Domain: Materials Science & Engineering
:Category: Scholarly Knowledge
:Current Version: 1.0.1
:Last Updated: 2024-01-30
:Creator: Akhil Thomas, Ali Riza Durmaz
:License: Creative Commons 4.0
:Format: OWL, TTL
:Download: `Materials Mechanics Ontology (MMO) Homepage <https://iwm-micro-mechanics-public.pages.fraunhofer.de/ontologies/materials-mechanics-ontology/index-en.html>`_

Graph Metrics
-------------
    - **Total Nodes**: 1043
    - **Total Edges**: 2402
    - **Root Nodes**: 11
    - **Leaf Nodes**: 509

Knowledge coverage
------------------
    - Classes: 428
    - Individuals: 0
    - Properties: 17

Hierarchical metrics
--------------------
    - **Maximum Depth**: 8
    - **Minimum Depth**: 0
    - **Average Depth**: 2.92
    - **Depth Variance**: 5.32

Breadth metrics
------------------
    - **Maximum Breadth**: 17
    - **Minimum Breadth**: 1
    - **Average Breadth**: 8.89
    - **Breadth Variance**: 21.65

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 876
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MMO

    # Initialize and load ontology
    ontology = MMO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
