Food Ontology (FoodON)
========================================================================================================================

Overview
--------
FoodOn, the food ontology, contains vocabulary for naming food materials and their anatomical and taxonomic origins,
from raw harvested food to processed food products, for humans and domesticated animals.
It provides a neutral and ontology-driven standard for government agencies,
industry, nonprofits and consumers to name and reference food products and their components
throughout the food supply chain.

:Domain: Agriculture
:Category: Diet, Metabolomics, and Nutrition
:Current Version: None
:Last Updated: 2025-01-16
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `Food Ontology (FoodON) Homepage <http://purl.obolibrary.org/obo/foodon.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 176584
    - **Total Edges**: 423840
    - **Root Nodes**: 4834
    - **Leaf Nodes**: 90848

Knowledge coverage
------------------
    - Classes: 47261
    - Individuals: 16
    - Properties: 197

Hierarchical metrics
--------------------
    - **Maximum Depth**: 23
    - **Minimum Depth**: 0
    - **Average Depth**: 2.24
    - **Depth Variance**: 4.81

Breadth metrics
------------------
    - **Maximum Breadth**: 11122
    - **Minimum Breadth**: 2
    - **Average Breadth**: 1217.12
    - **Breadth Variance**: 6546794.36

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 16
    - **Taxonomic Relations**: 76228
    - **Non-taxonomic Relations**: 2072
    - **Average Terms per Type**: 8.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import FoodOn

    # Initialize and load ontology
    ontology = FoodOn()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
