SIOC Core Ontology
==================

Overview
-----------------
The SIOC Core Ontology is an ontology that describes the structure and content of online communities.
It is designed to enable the integration of online community information across various online community services.

:Domain: Social Networks
:Category: Social
:Current Version: 1.36
:Last Updated: 2018/02/28
:Producer: Data Science Institute, NUI Galway.
:License: Creative Commons 3.0
:Format: RDF/XML
:Download: `SIOC Homepage <http://rdfs.org/sioc/spec/>`_
:Documentation: `SIOC Documentation <http://rdfs.org/sioc/spec/>`_


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
    - **Total Nodes**: 230
    - **Root Nodes**: 0
    - **Leaf Nodes**: 123
    - **Maximum Depth**: 0
    - **Edges**: 551

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 9
    - **Non-taxonomic Relations**: 31
    - **Average Terms per Type**: 0


Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import SIOC

   # Initialize and load ontology
   sioc = SIOC()
   sioc.load("path/to/ontology.owl")
   # Extract datasets
   data = sioc.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
