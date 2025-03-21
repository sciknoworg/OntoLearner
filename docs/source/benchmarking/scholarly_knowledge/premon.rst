Predicate Model for Ontologies (PreMOn)
========================================

Overview
-----------------
The PreMOn Ontology is an extension of lemon (W3C Ontology Lexicon Community Group, 2015)
for representing predicate models and their mappings. The Core Module of the PreMOn Ontology
defines the main abstractions for modelling semantic classes with their semantic roles,
mappings between different predicate models, and annotations.

:Domain: Scholarly Knowledge
:Category: Linguistics
:Current Version: 2018a
:Last Updated: 2018-02-15
:Producer: Francesco Corcoglioniti, Marco Rospocher <https://dkm.fbk.eu/rospocher>
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `PreMOn Homepage <https://premon.fbk.eu/ontology/core#>`_
:Documentation: `PreMOn Documentation <https://premon.fbk.eu/ontology/core#>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics
-------------
    - **Total Nodes**: 115
    - **Root Nodes**: 13
    - **Leaf Nodes**: 45
    - **Maximum Depth**: 6
    - **Edges**: 213

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 50
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import PreMOn

   # Initialize and load ontology
   premon = PreMOn()
   premon.load("path/to/ontology.owl")
   # Extract datasets
   data = premon.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
