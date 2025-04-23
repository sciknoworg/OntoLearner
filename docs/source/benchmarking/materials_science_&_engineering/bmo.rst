Building Material Ontology (BMO)
==========================

Overview
--------
Building Material Ontology defines the main concepts of building material,
types, layers, and properties.

:Domain: Materials Science & Engineering
:Category: Materials
:Current Version: 0.1
:Last Updated: 2019-12-10
:Creator: Janakiram Karlapudi, Prathap Valluru
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL, OWL, RDF/XML
:Download: `Building Material Ontology (BMO) Homepage <https://matportal.org/ontologies/BUILDMAT>`_

Graph Metrics
-------------
    - **Total Nodes**: 203
    - **Total Edges**: 420
    - **Root Nodes**: 83
    - **Leaf Nodes**: 68

Knowledge coverage
------------------
    - Classes: 24
    - Individuals: 12
    - Properties: 62

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 0.91
    - **Depth Variance**: 1.30

Breadth metrics
------------------
    - **Maximum Breadth**: 83
    - **Minimum Breadth**: 1
    - **Average Breadth**: 27.29
    - **Breadth Variance**: 1092.20

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 12
    - **Taxonomic Relations**: 20
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.67

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BMO

    # Initialize and load ontology
    ontology = BMO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
