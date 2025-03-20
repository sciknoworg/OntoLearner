BBC CMS Ontology
============

Overview
-----------------
The Content Management Systems ontology defines the terms that LDP needs to interact with systems that produce content.
The linked data platform contain semantic metadata for the creative content and also the things the BBC produces content about.
The CMS ontology defines how these things and content are associated with other BBC instances of the same thing.

:Domain: Media
:Category: News
:Current Version: 3.7
:Last Updated: 	2012-12-01
:Producer: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC CMS Homepage <https://www.bbc.co.uk/ontologies/cms-ontology>`_
:Documentation: `BBC CMS Documentation <https://www.bbc.co.uk/ontologies/cms-ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 68
    - **Root Nodes**: 0
    - **Leaf Nodes**: 41
    - **Maximum Depth**: 0
    - **Edges**: 137

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 4
    - **Taxonomic Relations**: 17
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.67

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBC_CMS
   # Initialize and load ontology
   bbc_cms = BBC_CMS()
   bbc_cms.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_cms.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
