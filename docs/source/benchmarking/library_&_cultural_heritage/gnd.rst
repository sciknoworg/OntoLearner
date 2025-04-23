Gemeinsame Normdatei (GND)
==========================

Overview
--------
GND stands for Gemeinsame Normdatei (Integrated Authority File) and offers a broad range of elements
to describe authorities. The GND originates from the German library community and aims
to solve the name ambiguity problem in the library world.

:Domain: Library & Cultural Heritage
:Category: Authority Files
:Current Version: 1.2.0
:Last Updated: 2024-08-26
:Creator: Alexander Haffner
:License: Creative Commons 1.0
:Format: RDF
:Download: `Gemeinsame Normdatei (GND) Homepage <https://d-nb.info/standards/elementset/gnd>`_

Graph Metrics
-------------
    - **Total Nodes**: 2100
    - **Total Edges**: 4128
    - **Root Nodes**: 0
    - **Leaf Nodes**: 1008

Knowledge coverage
------------------
    - Classes: 247
    - Individuals: 0
    - Properties: 236

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
    - **Term Types**: 0
    - **Taxonomic Relations**: 70
    - **Non-taxonomic Relations**: 3
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import GND

    # Initialize and load ontology
    ontology = GND()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
