Business News Ontology
=======================

Overview
-----------------
The Business News Ontology describes the concepts that occur in BBC business news.

:Domain: Media
:Category: News
:Current Version: 0.5
:Last Updated: 	2014-11-09
:Producer: https://www.bbc.co.uk/blogs/internet/authors/Jeremy_Tarling, https://uk.linkedin.com/in/amaalmohamed
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Business Homepage <https://www.bbc.co.uk/ontologies/business-news-ontology>`_
:Documentation: `BBC Business Documentation <https://www.bbc.co.uk/ontologies/business-news-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 50
    - **Root Nodes**: 0
    - **Leaf Nodes**: 35
    - **Maximum Depth**: 0
    - **Edges**: 95

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 5
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCBusiness
   # Initialize and load ontology
   bbc_business = BBCBusiness()
   bbc_business.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_business.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
