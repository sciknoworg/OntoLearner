GIST Upper Ontology (GIST)
========================================================================================================================

Overview
--------
Gist is Semantic Arts' minimalist upper ontology for the enterprise.
It is designed to have the maximum coverage of typical business ontology concepts
with the fewest number of primitives and the least amount of ambiguity.

:Domain: General Knowledge
:Category: Upper Ontology
:Current Version: 12.1.0
:Last Updated: 2024-Feb-27
:Creator: Semantic Arts
:License: Creative Commons 4.0
:Format: OWL
:Download: `GIST Upper Ontology (GIST) Homepage <https://semanticarts.com/gist>`_

Graph Metrics
-------------
    - **Total Nodes**: 1352
    - **Total Edges**: 2543
    - **Root Nodes**: 77
    - **Leaf Nodes**: 633

Knowledge coverage
------------------
    - Classes: 199
    - Individuals: 8
    - Properties: 113

Hierarchical metrics
--------------------
    - **Maximum Depth**: 27
    - **Minimum Depth**: 0
    - **Average Depth**: 4.14
    - **Depth Variance**: 21.06

Breadth metrics
------------------
    - **Maximum Breadth**: 298
    - **Minimum Breadth**: 1
    - **Average Breadth**: 34.86
    - **Breadth Variance**: 3571.91

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 8
    - **Taxonomic Relations**: 78
    - **Non-taxonomic Relations**: 56
    - **Average Terms per Type**: 8.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import GIST

    # Initialize and load ontology
    ontology = GIST()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
