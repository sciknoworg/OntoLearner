Music Ontology
==============

Overview
-----------------
The Music Ontology Specification provides main concepts and
properties fo describing music (i.e. artists, albums and tracks)
on the Semantic Web.

:Domain: Music
:Category: Scholarly Knowledge
:Current Version: 2.1.5
:Last Updated: 2013/07/22
:Producer: Knowledge Media Institute, Open University
:License: Creative Commons 4.0
:Format: RDF/XML
:Download: `Music Ontology Homepage <https://github.com/motools/musicontology>`_
:Documentation: `Music Ontology Documentation <https://github.com/motools/musicontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 662
    - **Root Nodes**: 39
    - **Leaf Nodes**: 268
    - **Maximum Depth**: 11
    - **Edges**: 1844

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 13
    - **Taxonomic Relations**: 67
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 1.18

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MusicOntology

   # Initialize and load ontology
   music = MusicOntology()
   music.load("path/to/ontology.owl")
   # Extract datasets
   data = music.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
