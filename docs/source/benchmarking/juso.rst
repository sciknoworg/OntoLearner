Juso Ontology
================

Overview
-----------------
Juso Ontology is a Web vocabulary for describing geographical addresses and features.

:Domain: Geography
:Category: Geography
:Current Version: 0.1.1
:Last Updated: 2015-11-10
:Producer: James G. Kim, LiST Inc.
:License: Creative Commons 4.0
:Format: TTL
:Download: `JUSO Homepage <https://rdfs.co/juso/0.1.1/html>`_
:Documentation: `JUSO Documentation <https://rdfs.co/juso/0.1.1/html>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 319
    - **Root Nodes**: 19
    - **Leaf Nodes**: 227
    - **Maximum Depth**: 7
    - **Edges**: 607

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 61
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import Juso

   # Initialize and load ontology
   juso = Juso()
   juso.load("path/to/ontology.ttl")
   # Extract datasets
   data = juso.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
