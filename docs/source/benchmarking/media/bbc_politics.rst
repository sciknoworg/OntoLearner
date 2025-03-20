BBC Politics Ontology
=================

Overview
-----------------
An ontology which describes a model for politics, specifically in terms of local government and elections.

:Domain: Politics
:Category: News
:Current Version: 0.9
:Last Updated: 2014-01-06
:Producer: https://www.r4isstatic.com/
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Politics Homepage <https://www.bbc.co.uk/ontologies/politics-ontology>`_
:Documentation: `BBC Politics Documentation <https://www.bbc.co.uk/ontologies/politics-ontology>`_

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

   from ontolearner.ontology import BBCPolitics
   # Initialize and load ontology
   bbc_politics = BBCPolitics()
   bbc_politics.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_politics.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
