Food Ontology (FoodOn)
============================

Overview
------------------
FoodOn, the food ontology, contains vocabulary for naming food materials and their anatomical and taxonomic origins,
from raw harvested food to processed food products, for humans and domesticated animals.
As an open-source inter-agency supported project, it provides a neutral and ontology-driven standard for government agencies,
industry, nonprofits and consumers to name and reference food products and their components throughout the food supply chain.
In partnership with other ontologies, the project also explores the semantic bedrock of vocabulary involved in modelling food composition,
food processing, nutrition and food related disease.

:Domain: diet, metabolomics, and nutrition
:Category:
:Current Version:
:Last Updated Date: 2025-01-16
:Producer:
:License: Creative Commons 4.0
:Format: OWL
:Download: `FoodOn Ontology <http://purl.obolibrary.org/obo/foodon.owl>`_
:Documentation: `FoodOn Repository <https://obofoundry.org/ontology/foodon>`_

Base Metrics
---------------
    - Classes:
    - Properties:
    - Annotation Assertions:
    - DL Expressivity:

Schema Metrics
---------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics:
------------------
    - **Nodes**: 39361
    - **Root Nodes**: 25986
    - **Leaf Nodes**: 164
    - **Maximum Depth**: 30
    - **Edges**: 111841

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 16
    - **Taxonomic Relations**: 76063
    - **Non-taxonomic Relations**: 2055
    - **Average Terms per Type**: 0.94

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology.food import FoodOntology

    # Initialize and load ontology
    food = FoodOntology()
    food.load("path/to/foodon.owl")
    # Extract datasets
    data = food.extract()
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
