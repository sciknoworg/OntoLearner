SMART Protocols Ontology: Document Module (SP-Document)
========================================================================================================================

Overview
--------
SMART Protocols Ontology: Document Module is an ontology designed
to represent metadata used to report an experimental protocol.

:Domain: Scholarly Knowledge
:Category: Materials Science
:Current Version: 4.0
:Last Updated: 2013-07-01
:Creator: http://oxgiraldo.wordpress.com
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `SMART Protocols Ontology: Document Module (SP-Document) Homepage <https://github.com/SMARTProtocols/SMART-Protocols>`_

Graph Metrics
-------------
    - **Total Nodes**: 1489
    - **Total Edges**: 3044
    - **Root Nodes**: 18
    - **Leaf Nodes**: 908

Knowledge coverage
------------------
    - Classes: 400
    - Individuals: 45
    - Properties: 43

Hierarchical metrics
--------------------
    - **Maximum Depth**: 9
    - **Minimum Depth**: 0
    - **Average Depth**: 3.96
    - **Depth Variance**: 4.49

Breadth metrics
------------------
    - **Maximum Breadth**: 69
    - **Minimum Breadth**: 8
    - **Average Breadth**: 32.80
    - **Breadth Variance**: 369.36

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 45
    - **Taxonomic Relations**: 474
    - **Non-taxonomic Relations**: 73
    - **Average Terms per Type**: 2.65

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SPDocument

    # Initialize and load ontology
    ontology = SPDocument()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
