FOAF Ontology
================

Overview
-----------------
FOAF is a project devoted to linking people and information using the Web.
Regardless of whether information is in people's heads, in physical or digital documents,
or in the form of factual data, it can be linked.

:Domain: Web
:Category: Social
:Current Version: 0.1
:Last Updated: 14 January 2014
:Producer: Dan Brickley, Libby Miller
:License: Creative Commons
:Format: RDF/XML
:Download: `FOAF Homepage <http://xmlns.com/foaf/0.1/>`_
:Documentation: `FOAF Documentation <http://xmlns.com/foaf/0.1/>`_

Base Metrics
---------------
    - Classes: 13
    - Individuals: 0
    - Properties: 62

Graph Metrics
------------------
    - **Total Nodes**: 168
    - **Root Nodes**: 5
    - **Leaf Nodes**: 87
    - **Maximum Depth**: 5
    - **Edges**: 504

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 13
    - **Taxonomic Relations**: 11
    - **Non-taxonomic Relations**: 21
    - **Average Terms per Type**: 3.25

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import FOAF

   # Initialize and load ontology
   foaf = FOAF()
   foaf.load("path/to/ontology.rdf")
   # Extract datasets
   data = foaf.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.non_type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
