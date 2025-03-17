Geographical Entities Ontology (GEO)
====================================

Overview
-----------------
An ontology and inventory of geopolitical entities (such as sovereign states and their administrative subdivisions)
as well as various geographical regions (including but not limited to the specific ones
over which the governments have jurisdiction)

:Domain: Geography
:Category: Geographic Knowledge
:Current Version:
:Last Updated: 2019-02-17
:Producer: William R Hogan
:License: Creative Commons 4.0
:Format: OWL
:Download: `GEO Homepage <http://purl.obolibrary.org/obo/geo.owl>`_
:Documentation: `GEO Documentation <http://purl.obolibrary.org/obo/geo.owl>`_

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

Graph Metrics:
------------------
    - **Total Nodes**: 108564
    - **Root Nodes**: 298
    - **Leaf Nodes**: 54168
    - **Maximum Depth**: 17
    - **Edges**: 246390

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 46949
    - **Taxonomic Relations**: 664
    - **Non-taxonomic Relations**: 65
    - **Average Terms per Type**: 1877

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import GEO

   # Initialize and load ontology
   geo = GEO()
   geo.load("path/to/ontology.owl")
   # Extract datasets
   data = geo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
