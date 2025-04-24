TUBES System Ontology (TUBES)
========================================================================================================================

Overview
--------
The scope of the TUBES System Ontology is to explicitly define interconnected building service system
in the AECO industry, their hierarchical subdivisions, structural and functional aspects,
and links to spatial entities. As such, TSO supports the effort to represent linkable information
in a future semantic web of building data. It has a strong alignment to other ontologies within the W3C community.

:Domain: Industry
:Category: Building Services
:Current Version: 0.3.0
:Last Updated: 2022-02-01
:Creator: Nicolas Pauen
:License: Creative Commons 4.0
:Format: RDF/XML, Turtle, JSON-LD
:Download: `TUBES System Ontology (TUBES) Homepage <https://rwth-e3d.github.io/tso/>`_

Graph Metrics
-------------
    - **Total Nodes**: 610
    - **Total Edges**: 1122
    - **Root Nodes**: 9
    - **Leaf Nodes**: 412

Knowledge coverage
------------------
    - Classes: 52
    - Individuals: 0
    - Properties: 101

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.10
    - **Depth Variance**: 0.09

Breadth metrics
------------------
    - **Maximum Breadth**: 9
    - **Minimum Breadth**: 1
    - **Average Breadth**: 5.00
    - **Breadth Variance**: 16.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 31
    - **Non-taxonomic Relations**: 3
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import TUBES

    # Initialize and load ontology
    ontology = TUBES()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
