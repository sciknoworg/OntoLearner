Quantities, Units, Dimensions and Data Types (QUDT)
========================================================================================================================

Overview
--------
QUDT is an advocate for the development and implementation of standards to quantify data expressed in RDF and JSON.

:Domain: Units and Measurements
:Category: Physics
:Current Version: 2.1
:Last Updated: March 1, 2022
:Creator: NASA Ames Research Center
:License: Creative Commons 4.0
:Format: TTL
:Download: `Quantities, Units, Dimensions and Data Types (QUDT) Homepage <https://qudt.org/>`_

Graph Metrics
-------------
    - **Total Nodes**: 772
    - **Total Edges**: 2288
    - **Root Nodes**: 0
    - **Leaf Nodes**: 233

Knowledge coverage
------------------
    - Classes: 73
    - Individuals: 24
    - Properties: 165

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
    - **Term Types**: 27
    - **Taxonomic Relations**: 400
    - **Non-taxonomic Relations**: 12
    - **Average Terms per Type**: 2.45

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import QUDT

    # Initialize and load ontology
    ontology = QUDT()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
