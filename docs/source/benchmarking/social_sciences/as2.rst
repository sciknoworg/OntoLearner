Activity Streams 2.0 Ontology (AS2)
========================================================================================================================

Overview
--------
The Activity Streams 2.0 ontology is a vocabulary for describing social activities and actions.
It is based on the Activity Streams 2.0 specification and provides a set of classes and properties
for describing activities on the web.

:Domain: Social Sciences
:Category: Social
:Current Version: 2.0
:Last Updated: 23 May 2017
:Creator: None
:License: W3C Document License
:Format: TTL
:Download: `Activity Streams 2.0 Ontology (AS2) Homepage <https://github.com/w3c/activitystreams?tab=License-1-ov-file#readme>`_

Graph Metrics
-------------
    - **Total Nodes**: 426
    - **Total Edges**: 945
    - **Root Nodes**: 0
    - **Leaf Nodes**: 120

Knowledge coverage
------------------
    - Classes: 107
    - Individuals: 1
    - Properties: 69

Hierarchical metrics
--------------------
    - **Maximum Depth**: 0
    - **Minimum Depth**: 0
    - **Average Depth**: 0.00
    - **Depth Variance**: 0.00

Breadth metrics
------------------
    - **Maximum Breadth**: 0
    - **Minimum Breadth**: 0
    - **Average Breadth**: 0.00
    - **Breadth Variance**: 0.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 55
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 1.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import AS2

    # Initialize and load ontology
    ontology = AS2()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
