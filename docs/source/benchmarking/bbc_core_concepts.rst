BBC Core Concepts Ontology
=======================

Overview
-----------------
The generic BBC ontology for people, places, events, organisations, themes which represent things
that make sense across the BBC. This model is meant to be generic enough, and allow clients (domain experts)
link their own concepts e.g., athletes or politicians using rdfs:sublClassOf the particular concept.

:Domain: Media
:Category: News
:Current Version: 1.30
:Last Updated: 2019-11-21
:Producer: jeremy.tarling@bbc.co.uk, tom.hodgkinson@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Core Concepts Homepage <https://www.bbc.co.uk/ontologies/core-concepts-ontology>`_
:Documentation: `BBC Core Concepts Documentation <https://www.bbc.co.uk/ontologies/core-concepts-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 122
    - **Root Nodes**: 4
    - **Leaf Nodes**: 73
    - **Maximum Depth**: 2
    - **Edges**: 265

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 25
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCCoreConcepts
   # Initialize and load ontology
   bbc_core_concepts = BBCCoreConcepts()
   bbc_core_concepts.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_core_concepts.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
