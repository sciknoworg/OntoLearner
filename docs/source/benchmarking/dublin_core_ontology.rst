Dublin Core Ontology
====================

Overview
-----------------
The Dublin Core Schema is a small set of vocabulary terms that can be used to describe several kinds of resources.
Dublin Core Metadata may be used for multiple purposes, from simple resource description,
to combining metadata vocabularies of different metadata standards, to providing interoperability
for metadata vocabularies in the Linked Data cloud and Semantic Web implementations.

:Domain: Metadata
:Category: General
:Current Version: 1.1
:Last Updated: February 17, 2017
:Producer: The Dublin Core Metadata Initiative
:License: Public Domain
:Format: RDF, OWL, TTL, CSV, NT
:Download: `Dublin Core Homepage <https://bioportal.bioontology.org/ontologies/DC>`_
:Documentation: `Dublin Core Documentation <https://bioportal.bioontology.org/ontologies/DC>`_

Base Metrics
---------------
    - Classes: 11
    - Individuals: 26
    - Properties: 0

Schema Metrics
---------------
    - Attribute Richness: 0
    - Inheritance Richness: 0
    - Relationship Richness: 0

Graph Metrics
------------------
    - **Total Nodes**: 297
    - **Root Nodes**: 1
    - **Leaf Nodes**: 211
    - **Maximum Depth**: 0
    - **Edges**: 643

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 30
    - **Taxonomic Relations**: 11
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.88

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import DublinCore

   # Initialize and load ontology
   dc = DublinCore()
   dc.load("path/to/ontology.owl")
   # Extract datasets
   data = dc.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
