Citation Typing Ontology (CiTO)
==========================

Overview
--------
The Citation Typing Ontology (CiTO) is an ontology that enables characterization of the nature or type of citations,
both factually and rhetorically.

:Domain: Scholarly Knowledge
:Category: Scholarly Communication
:Current Version: 2.8.1
:Last Updated: 2018-02-16
:Creator: Silvio Peroni, David Shotton
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `Citation Typing Ontology (CiTO) Homepage <https://github.com/SPAROntologies/cito/tree/master/docs/current>`_

Graph Metrics
-------------
    - **Total Nodes**: 312
    - **Total Edges**: 574
    - **Root Nodes**: 11
    - **Leaf Nodes**: 182

Knowledge coverage
------------------
    - Classes: 10
    - Individuals: 0
    - Properties: 101

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.56
    - **Depth Variance**: 0.25

Breadth metrics
------------------
    - **Maximum Breadth**: 14
    - **Minimum Breadth**: 11
    - **Average Breadth**: 12.50
    - **Breadth Variance**: 2.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 11
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CiTO

    # Initialize and load ontology
    ontology = CiTO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
