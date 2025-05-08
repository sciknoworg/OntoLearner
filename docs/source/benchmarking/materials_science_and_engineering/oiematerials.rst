Open Innovation Environment Materials (OIEMaterials)
========================================================================================================================

Overview
--------
The materials module populates the physicalistic perspective with materials subclasses categorised
according to modern applied physical sciences.

:Domain: Materials Science and Engineering
:Category: Materials
:Current Version: None
:Last Updated: None
:Creator: Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Open Innovation Environment Materials (OIEMaterials) Homepage <https://github.com/emmo-repo/OIE-Ontologies/>`_

Graph Metrics
-------------
    - **Total Nodes**: 278
    - **Total Edges**: 561
    - **Root Nodes**: 13
    - **Leaf Nodes**: 115

Knowledge coverage
------------------
    - Classes: 119
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 4
    - **Minimum Depth**: 0
    - **Average Depth**: 1.64
    - **Depth Variance**: 1.87

Breadth metrics
------------------
    - **Maximum Breadth**: 14
    - **Minimum Breadth**: 6
    - **Average Breadth**: 10.00
    - **Breadth Variance**: 10.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 156
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OIEMaterials

    # Initialize and load ontology
    ontology = OIEMaterials()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
