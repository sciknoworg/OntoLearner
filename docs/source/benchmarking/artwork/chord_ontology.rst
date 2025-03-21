The Chord Ontology
==================

Overview
-----------------
The Chord Ontology is an ontology for describing chords in musical pieces.

:Domain: Music Theory
:Category: Artwork
:Current Version: 1.0
:Last Updated: 2007-10-25
:Producer: Yves Raimond, Samer Abdallah, Centre for Digital Music, Queen Mary, University of London
:License: Creative Commons 3.0
:Format: RDF/XML
:Download: `Timeline Homepage <https://github.com/motools/chordontology>`_
:Documentation: `Timeline Documentation <https://github.com/motools/chordontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 196
    - **Root Nodes**: 11
    - **Leaf Nodes**: 66
    - **Maximum Depth**:
    - **Edges**: 456

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 108
    - **Taxonomic Relations**: 4
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 5.68

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import Chord

   # Initialize and load ontology
   chord = Chord()
   chord.load("path/to/ontology.rdf")
   # Extract datasets
   data = chord.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
