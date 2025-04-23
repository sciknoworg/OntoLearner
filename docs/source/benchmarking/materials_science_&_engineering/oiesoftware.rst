Open Innovation Environment (OIE) domain ontologies, Software module (OIESoftware)
==========================

Overview
--------
Software module.

:Domain: Materials Science & Engineering
:Category: Materials
:Current Version: 0.1
:Last Updated: None
:Creator: Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Open Innovation Environment (OIE) domain ontologies, Software module (OIESoftware) Homepage <https://github.com/emmo-repo/OIE-Ontologies/>`_

Graph Metrics
-------------
    - **Total Nodes**: 205
    - **Total Edges**: 489
    - **Root Nodes**: 17
    - **Leaf Nodes**: 49

Knowledge coverage
------------------
    - Classes: 155
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 1.01
    - **Depth Variance**: 0.59

Breadth metrics
------------------
    - **Maximum Breadth**: 37
    - **Minimum Breadth**: 3
    - **Average Breadth**: 17.25
    - **Breadth Variance**: 155.19

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 188
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OIESoftware

    # Initialize and load ontology
    ontology = OIESoftware()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
