BBC Food Ontology
=============

Overview
-----------------
The Food Ontology is a simple lightweight ontology for publishing data about recipes,
including the foods they are made from and the foods they create as well as the diets,
menus, seasons, courses and occasions they may be suitable for. Whilst it originates in a specific BBC use case,
the Food Ontology should be applicable to a wide range of recipe data publishing across the web.

:Domain: Food
:Category: Food
:Current Version: 0.1
:Last Updated: 2014/03/18
:Producer:
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Food Homepage <https://www.bbc.co.uk/ontologies/food-ontology>`_
:Documentation: `BBC Food Documentation <https://www.bbc.co.uk/ontologies/food-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 108
    - **Root Nodes**: 0
    - **Leaf Nodes**: 63
    - **Maximum Depth**: 0
    - **Edges**: 267

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 5
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCFood
   # Initialize and load ontology
   bbc_food = BBCFood()
   bbc_food.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_food.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
