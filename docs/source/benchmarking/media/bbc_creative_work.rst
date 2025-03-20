BBC Creative Work Ontology
=======================

Overview
-----------------
This ontology defines the terms required to describe the creative works produced by the BBC and their associated metadata.
This ontology powers reading and writing creative works in the triplestore using tags associated with them (about)
their more specific types (BlogPost, NewsItem, Programme) and audiences (audience).

:Domain: Media
:Category: News
:Current Version: 1.19
:Last Updated: 2012-12-01
:Producer: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Creative Work Homepage <https://www.bbc.co.uk/ontologies/creative-work-ontology>`_
:Documentation: `BBC Creative Work Documentation <https://www.bbc.co.uk/ontologies/creative-work-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 137
    - **Root Nodes**: 0
    - **Leaf Nodes**: 80
    - **Maximum Depth**: 0
    - **Edges**: 300

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 15
    - **Taxonomic Relations**: 17
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.79

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCCreativeWork
   # Initialize and load ontology
   bbc_creative_work = BBCCreativeWork()
   bbc_creative_work.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_creative_work.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
