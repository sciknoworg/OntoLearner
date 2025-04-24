Flow Systems Ontology (FSO)
========================================================================================================================

Overview
--------
The Flow Systems Ontology (FSO) is an ontology for describing interconnected systems
with material or energy flow connections, and their components.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.1.0
:Last Updated: 2020-08-06
:Creator: Ali Kücükavci, Mads Holten Rasmussen, Ville Kukkonen
:License: Creative Commons 4.0
:Format: TTL
:Download: `Flow Systems Ontology (FSO) Homepage <https://github.com/alikucukavci/FSO/>`_

Graph Metrics
-------------
    - **Total Nodes**: 141
    - **Total Edges**: 279
    - **Root Nodes**: 10
    - **Leaf Nodes**: 56

Knowledge coverage
------------------
    - Classes: 14
    - Individuals: 1
    - Properties: 22

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.17
    - **Depth Variance**: 0.14

Breadth metrics
------------------
    - **Maximum Breadth**: 10
    - **Minimum Breadth**: 2
    - **Average Breadth**: 6.00
    - **Breadth Variance**: 16.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 11
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import FSO

    # Initialize and load ontology
    ontology = FSO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
