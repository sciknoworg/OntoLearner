BBC Wildlife Ontology
=================

Overview
-----------------
A simple vocabulary for describing biological species and related taxa. The vocabulary defines terms
for describing the names and ranking of taxa, as well as providing support for describing their habitats,
conservation status, and behavioural characteristics, etc.

:Domain: Biology
:Category: Biology
:Current Version: 	1.1
:Last Updated: 2013/12/18
:Producer: https://www.ldodds.com#me, http://tomscott.name/
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Wildlife Homepage <https://www.bbc.co.uk/ontologies/wildlife-ontology>`_
:Documentation: `BBC Wildlife Documentation <https://www.bbc.co.uk/ontologies/wildlife-ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 157
    - **Root Nodes**: 1
    - **Leaf Nodes**: 93
    - **Maximum Depth**: 1
    - **Edges**: 414

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 23
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCWildlife
   # Initialize and load ontology
   bbc_wildlife = BBCWildlife()
   bbc_wildlife.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_wildlife.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
