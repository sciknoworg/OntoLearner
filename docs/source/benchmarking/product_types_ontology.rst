The Product Types Ontology
==========================

Overview
-----------------
The Product Types Ontology is designed to be used in combination with GoodRelations,
a standard vocabulary for the commercial aspects of offers.

:Domain: Product Types
:Category: Industry
:Current Version: 1.0
:Last Updated: 2025-02-21
:Producer: Martin Hepp
:License: Creative Commons 3.0
:Format: RDF, OWL, TTL, CSV, NT
:Download: `Product Types Homepage <http://www.productontology.org/>`_
:Documentation: `Product Types Documentation <http://www.productontology.org/>`_

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
    - **Total Nodes**: 4577
    - **Root Nodes**: 12
    - **Leaf Nodes**: 1012
    - **Maximum Depth**: 2
    - **Edges**: 14125

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 3001
    - **Taxonomic Relations**: 4000
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 375

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import ProductTypes

   # Initialize and load ontology
   pto = PTO()
   pto.load("path/to/ontology.rdf")
   # Extract datasets
   data = pto.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
