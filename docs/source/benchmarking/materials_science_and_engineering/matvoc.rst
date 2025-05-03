Materials Vocabulary (MatVoc)
========================================================================================================================

Overview
--------
The official ontology produced in the context of the STREAM project.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 1.0.0
:Last Updated: 2022-12-12
:Creator: Tatyana Sheveleva, Javad Chamanara
:License: MIT License
:Format: RDF/XML,TTL
:Download: `Materials Vocabulary (MatVoc) Homepage <https://stream-project.github.io/#overv>`_

Graph Metrics
-------------
    - **Total Nodes**: 94
    - **Total Edges**: 161
    - **Root Nodes**: 16
    - **Leaf Nodes**: 44

Knowledge coverage
------------------
    - Classes: 28
    - Individuals: 0
    - Properties: 15

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.62
    - **Depth Variance**: 0.48

Breadth metrics
------------------
    - **Maximum Breadth**: 16
    - **Minimum Breadth**: 4
    - **Average Breadth**: 10.67
    - **Breadth Variance**: 24.89

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 6
    - **Non-taxonomic Relations**: 7
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MatVoc

    # Initialize and load ontology
    ontology = MatVoc()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
