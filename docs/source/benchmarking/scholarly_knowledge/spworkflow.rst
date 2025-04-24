SMART Protocols Ontology: Workflow Module (SP-Workflow)
========================================================================================================================

Overview
--------
SP-Workflow module represents: i) the executable  elements of a protocol; ii) the experimental actions
and material entities that participates in instructions (sample/specimen, organisms, reagents,
instruments);  and iii) the order of execution of the instructions.

:Domain: Scholarly Knowledge
:Category: Workflows
:Current Version: 4.0
:Last Updated: 2013-07-01
:Creator: http://oxgiraldo.wordpress.com
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `SMART Protocols Ontology: Workflow Module (SP-Workflow) Homepage <https://github.com/SMARTProtocols/SMART-Protocols>`_

Graph Metrics
-------------
    - **Total Nodes**: 1446
    - **Total Edges**: 3017
    - **Root Nodes**: 4
    - **Leaf Nodes**: 834

Knowledge coverage
------------------
    - Classes: 419
    - Individuals: 5
    - Properties: 17

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 7.23
    - **Depth Variance**: 8.19

Breadth metrics
------------------
    - **Maximum Breadth**: 36
    - **Minimum Breadth**: 3
    - **Average Breadth**: 14.07
    - **Breadth Variance**: 120.78

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 5
    - **Taxonomic Relations**: 1079
    - **Non-taxonomic Relations**: 22
    - **Average Terms per Type**: 1.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SPWorkflow

    # Initialize and load ontology
    ontology = SPWorkflow()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
