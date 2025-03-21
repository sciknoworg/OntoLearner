Schema.org Vocabulary
==================

Overview
-----------------
Schema.org is a collaborative, community activity with a mission to create,
maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond.

:Domain: General Knowledge
:Category: Web Development
:Current Version: 28.1
:Last Updated: 2024-11-22
:Producer: Schema.org Community
:License: Creative Commons 4.0
:Format: OWL,
:Download: `Schema.org Homepage <https://github.com/schemaorg/schemaorg/blob/main/data/releases/28.1/schemaorg.owl>`_
:Documentation: `Schema.org Documentation <https://github.com/schemaorg/schemaorg/blob/main/data/releases/28.1/schemaorg.owl>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 15044
    - **Root Nodes**: 0
    - **Leaf Nodes**: 2128
    - **Maximum Depth**: 0
    - **Edges**: 32,425

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1058
    - **Non-taxonomic Relations**: 635
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import SchemaOrg

   # Initialize and load ontology
   schema = SchemaOrg()
   schema.load("path/to/ontology.owl")
   # Extract datasets
   data = schema.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
