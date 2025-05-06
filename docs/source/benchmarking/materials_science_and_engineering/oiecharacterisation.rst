Open Innovation Environment (OIE) domain ontologies, Characterisation module (OIECharacterisation)
========================================================================================================================

Overview
--------
EMMO-compliant, domain-level OIE ontology tackling the areas of characterization methods.

:Domain: Materials Science and Engineering
:Category: Materials
:Current Version: None
:Last Updated: None
:Creator: Daniele Toti, Gerhard Goldbeck, Pierluigi Del Nostro
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Open Innovation Environment (OIE) domain ontologies, Characterisation module (OIECharacterisation) Homepage <https://github.com/emmo-repo/OIE-Ontologies/>`_

Graph Metrics
-------------
    - **Total Nodes**: 54
    - **Total Edges**: 135
    - **Root Nodes**: 1
    - **Leaf Nodes**: 11

Knowledge coverage
------------------
    - Classes: 42
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.88
    - **Depth Variance**: 0.11

Breadth metrics
------------------
    - **Maximum Breadth**: 7
    - **Minimum Breadth**: 1
    - **Average Breadth**: 4.00
    - **Breadth Variance**: 9.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 41
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OIECharacterisation

    # Initialize and load ontology
    ontology = OIECharacterisation()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
