BBC Ontology
================

Overview
-----------------
The BBC ontology codifies the logic that connects web documents, BBC products and platforms
for which content is available. Currently, there are 10 major products in Future Media
which produce content for BBC online. The majority of those contain more products dedicated in thematic areas,
for example Education propositions are part of the K&L (Knowledge and Learning) product portfolio.

:Domain: Media
:Category: News
:Current Version: 1.37
:Last Updated: 	2012-12-01
:Producer: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Homepage <https://www.bbc.co.uk/ontologies/bbc-ontology/>`_
:Documentation: `BBC Documentation <https://www.bbc.co.uk/ontologies/bbc-ontology/>`_

Base Metrics
---------------
    - Classes: 10
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 164
    - **Root Nodes**: 0
    - **Leaf Nodes**: 101
    - **Maximum Depth**: 0
    - **Edges**: 316

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 10
    - **Taxonomic Relations**: 35
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.91

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBC
   # Initialize and load ontology
   bbc = BBC()
   bbc.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
