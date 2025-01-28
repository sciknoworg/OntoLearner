Food Ontology Analysis Results
============================

Overview
------------------
The Food Ontology is a structured vocabulary and database resource that links food products,
ingredients, and recipes to nutritional data.

Basic Information
------------------
:Domain: Food Science, Nutrition
:Category:
:Current Version:
:Last Updated Date:
:Producer:
:License: Creative Commons 4.0
:Format: OWL
:Download: `FoodOn Ontology <http://purl.obolibrary.org/obo/foodon.owl>`_
:Documentation: `FoodOn Repository <https://github.com/FoodOntology/foodon/tree/master>`_

Ontology Statistics
------------------
Graph Metrics:
    - **Triples**: 428,965
    - **Nodes**: 47,230
    - **Total Edges**: 45,154

Hierarchical Structure:
    - **Maximum Depth**: 30
    - **Root Nodes**: 10,436
    - **:Leaf Nodes**: 35,925

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 40,134
    - **Taxonomic Relations**: 45,159
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 3,087.23

Relationship Types
------------------
Taxonomic Relations:

Non-taxonomic Relations:

Alignments
------------------

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology.food import FoodOntology

    # Initialize and load ontology
    food = FoodOntology()

    food.load("path/to/foodon.owl")

    # Extract datasets
    data = food.extract()
