Materials Design Ontology (MDO)
==============================

Overview
-----------------
MDO is an ontology for materials design field, representing the domain knowledge specifically related
to solid-state physics and computational materials science.

:Domain: Materials Science
:Category: Materials Design
:Current Version: 1.1
:Last Updated: 2022-08-02
:Producer: Materials Design Division, National Institute for Materials Science (NIMS)
:License: Creative Commons 4.0
:Format: OWL, RDF/XML, TTL, JSON-LD
:Download: `MDO Homepage <https://github.com/LiUSemWeb/Materials-Design-Ontology/tree/master/>`_
:Documentation: `MDO Documentation <https://github.com/LiUSemWeb/Materials-Design-Ontology/tree/master>`_


Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Schema Metrics
---------------
    - Attribute Richness: 0
    - Inheritance Richness: 0
    - Relationship Richness: 0

Graph Metrics:
------------------
    - **Total Nodes**: 76
    - **Root Nodes**: 14
    - **Leaf Nodes**: 24
    - **Maximum Depth**: 5
    - **Edges**: 137

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 2
    - **Taxonomic Relations**: 8
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0.50

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MDO

   # Initialize and load ontology
   mdo = MDO()
   mdo.load("path/to/ontology.owl")
   # Extract datasets
   data = mdo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
