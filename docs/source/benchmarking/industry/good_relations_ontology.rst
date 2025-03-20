Good Relations Language Reference (GoodRelations)
=================================================

Overview
-----------------
GoodRelations is a standardized vocabulary (also known as "schema", "data dictionary", or "ontology") for product,
price, store, and company data that can (1) be embedded into existing static and dynamic Web pages and that
(2) can be processed by other computers. This increases the visibility of your products and services
in the latest generation of search engines, recommender systems, and other novel applications.

:Domain: E-commerce
:Category: Industry
:Current Version: 1.0
:Last Updated: 2011-10-01
:Producer: Martin Hepp
:License: Creative Commons 3.0
:Format: RDF/XML
:Download: `GoodRelations Homepage <https://www.heppnetz.de/ontologies/goodrelations/v1>`_
:Documentation: `GoodRelations Documentation <https://www.heppnetz.de/ontologies/goodrelations/v1>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics
------------------
    - **Total Nodes**: 677
    - **Root Nodes**: 18
    - **Leaf Nodes**: 206
    - **Maximum Depth**:
    - **Edges**: 1816

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 47
    - **Taxonomic Relations**: 25
    - **Non-taxonomic Relations**: 265
    - **Average Terms per Type**: 1.74

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import GoodRelations

   # Initialize and load ontology
   gr = GoodRelations()
   gr.load("path/to/ontology.owl")
   # Extract datasets
   data = gr.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
