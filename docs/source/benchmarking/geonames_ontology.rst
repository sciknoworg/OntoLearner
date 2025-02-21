The Geonames Ontology
========================

Overview
-----------------
The Geonames ontologies provides elements of description for geographical features,
in particular those defined in the geonames.org data base.

:Domain: Geospatial
:Category: Geography
:Current Version: 3.3
:Last Updated: 2022-01-30
:Producer: Bernard Vatant
:License: Creative Commons 3.0
:Format: RDF/XML, Turtle, JSON-LD
:Download: `GNO Homepage <https://www.geonames.org/ontology>`_
:Documentation: `GNO Documentation <https://www.geonames.org/ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Schema Metrics
---------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics
------------------
    - **Total Nodes**: 4879
    - **Root Nodes**: 2
    - **Leaf Nodes**: 4123
    - **Maximum Depth**:
    - **Edges**: 6631

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 699
    - **Taxonomic Relations**: 150
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 99.86

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import Geonames

   # Initialize and load ontology
   gno = Geonames()
   gno.load("path/to/ontology.owl")
   # Extract datasets
   data = gno.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.non_type_taxonomies
