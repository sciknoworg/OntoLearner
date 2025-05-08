Material Properties Ontology (MAT)
========================================================================================================================

Overview
--------
The Material Properties Ontology aims to provide the vocabulary to describe the building components,
materials, and their corresponding properties, relevant within the construction industry. More specifically,
the building elements and properties covered in this ontology support applications
focused on the design of building renovation projects.

:Domain: Materials Science and Engineering
:Category: Materials Properties
:Current Version: 0.0.8
:Last Updated: None
:Creator: María Poveda-Villalón, Serge Chávez-Feria
:License: Creative Commons 4.0
:Format: RDF
:Download: `Material Properties Ontology (MAT) Homepage <https://bimerr.iot.linkeddata.es/def/material-properties/>`_

Graph Metrics
-------------
    - **Total Nodes**: 263
    - **Total Edges**: 691
    - **Root Nodes**: 7
    - **Leaf Nodes**: 52

Knowledge coverage
------------------
    - Classes: 140
    - Individuals: 0
    - Properties: 21

Hierarchical metrics
--------------------
    - **Maximum Depth**: 11
    - **Minimum Depth**: 0
    - **Average Depth**: 5.21
    - **Depth Variance**: 11.10

Breadth metrics
------------------
    - **Maximum Breadth**: 12
    - **Minimum Breadth**: 2
    - **Average Breadth**: 5.67
    - **Breadth Variance**: 7.22

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 128
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MAT

    # Initialize and load ontology
    ontology = MAT()
    ontology.load("path/to/ontology.RDF")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
