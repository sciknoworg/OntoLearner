GeoNames Ontology (GeoNames)
==========================

Overview
--------
The Geonames ontologies provides elements of description for geographical features,
in particular those defined in the geonames.org database.

:Domain: Geography
:Category: Geographic Knowledge
:Current Version: 3.3
:Last Updated: 2022-01-30
:Creator: Bernard Vatant
:License: Creative Commons 3.0
:Format: RDF/XML, Turtle, JSON-LD
:Download: `GeoNames Ontology (GeoNames) Homepage <https://www.geonames.org/ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 4879
    - **Total Edges**: 6631
    - **Root Nodes**: 2
    - **Leaf Nodes**: 4123

Knowledge coverage
------------------
    - Classes: 7
    - Individuals: 699
    - Properties: 30

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 1.18
    - **Depth Variance**: 0.43

Breadth metrics
------------------
    - **Maximum Breadth**: 21
    - **Minimum Breadth**: 2
    - **Average Breadth**: 7.00
    - **Breadth Variance**: 65.50

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 699
    - **Taxonomic Relations**: 150
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 99.86

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import GeoNames

    # Initialize and load ontology
    ontology = GeoNames()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
