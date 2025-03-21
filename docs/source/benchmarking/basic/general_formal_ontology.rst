General Formal Ontology (GFO)
=======================

Overview
-----------------
The General Formal Ontology is a top-level ontology for conceptual modeling,
which is being constantly further developed by Onto-Med. It includes elaborations of categories like objects,
processes, time and space, properties, relations, roles, functions, facts, and situations.
Moreover, we are working on an integration with the notion of levels of reality in order
to more appropriately capture entities in the material, mental, and social areas.

:Domain: Basic
:Category: Upper-Level Ontology
:Current Version:
:Last Updated: 2024-11-18
:Producer:
:License: Creative Commons 4.0
:Format: OWL
:Download: `GFO Homepage <https://onto-med.github.io/GFO/release/2024-11-18/index-en.html>`_
:Documentation: `GFO Documentation <https://www.onto-med.de/en/ontologies/gfo/>`_

Base Metrics
---------------
    - Classes: 77
    - Individuals: 1
    - Properties: 78

Graph Metrics:
------------------
    - **Total Nodes**: 296
    - **Root Nodes**: 42
    - **Leaf Nodes**: 71
    - **Maximum Depth**: 6
    - **Edges**: 708

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 203
    - **Non-taxonomic Relations**: 40
    - **Average Terms per Type**: 0.33

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import GFO

   # Initialize and load ontology
   gfo = GFO()
   gfo.load("path/to/ontology.owl")
   # Extract datasets
   data = gfo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
