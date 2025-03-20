YAGO Ontology
=======================

Overview
-----------------
YAGO is a large knowledge base with general knowledge about people, cities, countries, movies, and organizations.
The YAGO 4.5 knowledge base consists of the following set of Turtle files:
    - Schema: The upper taxonomy, constraints, and property definitions in SHACL.
    - Taxonomy: The full taxonomy of classes.
    - Facts: All facts about entities that have an English Wikipedia page.
    - Facts beyond Wikipedia: All facts about entities that do not have an English Wikipedia page.
    - Meta: The fact annotations in RDF.

:Domain: General Knowledge
:Category: General Knowledge
:Current Version: 4.5
:Last Updated: April, 2024
:Producer: Max Planck Institute for Informatics
:License: Creative Commons 3.0
:Format: TTL
:Download: `YAGO Homepage <https://yago-knowledge.org/downloads/yago-4-5>`_
:Documentation: `YAGO Documentation <https://yago-knowledge.org/downloads/yago-4-5>`_

YAGO Schema
-----------------

Overview
-----------------
The upper taxonomy, constraints, and property definitions in SHACL

Graph Metrics
------------------
    - **Total Nodes**: 656
    - **Root Nodes**: 23
    - **Leaf Nodes**: 331
    - **Maximum Depth**:
    - **Edges**: 1060

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 39
    - **Taxonomic Relations**: 30
    - **Non-taxonomic Relations**: 58
    - **Average Terms per Type**: 9

YAGO Taxonomy
-----------------

Overview
-----------------
The full taxonomy of classes.

Graph Metrics
------------------
    - **Total Nodes**: 132877
    - **Root Nodes**: 92148
    - **Leaf Nodes**: 9
    - **Edges**: 166351

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 252725
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import YAGO

   # Initialize and load ontology
   yago = YAGO()
   yago.load("path/to/ontology.ttl")
   # Extract datasets
   data = yago.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
