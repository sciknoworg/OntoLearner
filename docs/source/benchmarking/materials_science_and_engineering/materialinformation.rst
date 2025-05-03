Material Information Ontology (MaterialInformation)
========================================================================================================================

Overview
--------
The Material Information ontology is divided into smaller ontologies (partitions).
The partitions are Environment, Geometry, Material Information, Manufacturing Process, Property,
Substance, Unit Dimension, Structure, Equation and Physical Constant.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: None
:Last Updated: None
:Creator: Toshihiro Ashino
:License: None
:Format: OWL, RDF/XML
:Download: `Material Information Ontology (MaterialInformation) Homepage <https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MaterialInformation.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 1155
    - **Total Edges**: 2343
    - **Root Nodes**: 596
    - **Leaf Nodes**: 48

Knowledge coverage
------------------
    - Classes: 548
    - Individuals: 410
    - Properties: 98

Hierarchical metrics
--------------------
    - **Maximum Depth**: 11
    - **Minimum Depth**: 0
    - **Average Depth**: 0.82
    - **Depth Variance**: 2.11

Breadth metrics
------------------
    - **Maximum Breadth**: 596
    - **Minimum Breadth**: 1
    - **Average Breadth**: 96.08
    - **Breadth Variance**: 36614.24

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 410
    - **Taxonomic Relations**: 611
    - **Non-taxonomic Relations**: 30
    - **Average Terms per Type**: 1.03

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MaterialInformation

    # Initialize and load ontology
    ontology = MaterialInformation()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
