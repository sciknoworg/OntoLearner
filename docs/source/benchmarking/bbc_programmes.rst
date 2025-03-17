BBC Programmes Ontology
===================

Overview
-----------------
This ontology aims at providing a simple vocabulary for describing programmes.
It covers brands, series (seasons), episodes, broadcast events, broadcast services,etc.
Its development was funded by the BBC, and is heavily grounded on previous programmes data modelling work done there.

:Domain: Media
:Category: News
:Current Version: 1.1
:Last Updated: 2009/02/20
:Producer: https://moustaki.org/foaf.rdf#moustaki
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Programmes Homepage <https://www.bbc.co.uk/ontologies/programmes-ontology>`_
:Documentation: `BBC Programmes Documentation <https://www.bbc.co.uk/ontologies/programmes-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 218
    - **Root Nodes**: 2
    - **Leaf Nodes**: 129
    - **Maximum Depth**: 3
    - **Edges**: 620

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 40
    - **Non-taxonomic Relations**: 19
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCProgrammes
   # Initialize and load ontology
   bbc_programmes = BBCProgrammes()
   bbc_programmes.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_programmes.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
