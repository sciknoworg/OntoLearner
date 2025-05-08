Material Ontology (MatOnto)
========================================================================================================================

Overview
--------
The Material Ontology (MatOnto) is based on the upper level ontology, the BFO.

:Domain: Materials Science and Engineering
:Category: Scholarly Knowledge
:Current Version: None
:Last Updated: None
:Creator: None
:License: None
:Format: OWL
:Download: `Material Ontology (MatOnto) Homepage <https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MatOnto.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 4753
    - **Total Edges**: 11287
    - **Root Nodes**: 33
    - **Leaf Nodes**: 1063

Knowledge coverage
------------------
    - Classes: 1307
    - Individuals: 122
    - Properties: 95

Hierarchical metrics
--------------------
    - **Maximum Depth**: 129
    - **Minimum Depth**: 0
    - **Average Depth**: 38.24
    - **Depth Variance**: 1437.88

Breadth metrics
------------------
    - **Maximum Breadth**: 155
    - **Minimum Breadth**: 1
    - **Average Breadth**: 18.92
    - **Breadth Variance**: 522.53

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 122
    - **Taxonomic Relations**: 1215
    - **Non-taxonomic Relations**: 167
    - **Average Terms per Type**: 1.94

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MatOnto

    # Initialize and load ontology
    ontology = MatOnto()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
