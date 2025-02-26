The Flow Systems Ontology (FSO)
=====================

Overview
-----------------
The Flow Systems Ontology (FSO) is an ontology for describing interconnected systems
with material or energy flow connections, and their components.

:Domain: Engineering
:Category: Material Science and Engineering
:Current Version: 0.1.0
:Last Updated: 2020-08-06
:Producer: Ali Kücükavci, Mads Holten Rasmussen, Ville Kukkonen
:License: Creative Commons 4.0
:Format: TTL
:Download: `FSO Homepage <https://github.com/alikucukavci/FSO/>`_
:Documentation: `FSO Documentation <https://github.com/alikucukavci/FSO/>`_

Base Metrics
-----------------
    - Classes:
    - Individuals:
    - Properties:

Schema Metrics
-----------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics
------------------
    - **Total Nodes**: 141
    - **Root Nodes**: 10
    - **Leaf Nodes**: 56
    - **Maximum Depth**: 5
    - **Edges**: 279

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 11
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import FSO

   # Initialize and load ontology
   fso = FSO()
   fso.load("path/to/ontology.ttl")
   # Extract datasets
   data = fso.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
