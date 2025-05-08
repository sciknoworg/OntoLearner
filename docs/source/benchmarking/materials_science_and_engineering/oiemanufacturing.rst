Open Innovation Environment Manufacturing (OIEManufacturing)
========================================================================================================================

Overview
--------
The manufacturing module populates the physicalistic perspective with manufacturing subclasses categorised
according to modern applied physical sciences.

:Domain: Materials Science and Engineering
:Category: Materials
:Current Version: None
:Last Updated: None
:Creator: Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Open Innovation Environment Manufacturing (OIEManufacturing) Homepage <https://github.com/emmo-repo/OIE-Ontologies/>`_

Graph Metrics
-------------
    - **Total Nodes**: 380
    - **Total Edges**: 869
    - **Root Nodes**: 13
    - **Leaf Nodes**: 131

Knowledge coverage
------------------
    - Classes: 222
    - Individuals: 0
    - Properties: 3

Hierarchical metrics
--------------------
    - **Maximum Depth**: 5
    - **Minimum Depth**: 0
    - **Average Depth**: 1.39
    - **Depth Variance**: 1.07

Breadth metrics
------------------
    - **Maximum Breadth**: 30
    - **Minimum Breadth**: 1
    - **Average Breadth**: 12.00
    - **Breadth Variance**: 112.67

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 217
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OIEManufacturing

    # Initialize and load ontology
    ontology = OIEManufacturing()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
