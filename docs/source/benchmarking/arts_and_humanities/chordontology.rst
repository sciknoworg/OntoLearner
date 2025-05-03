Chord Ontology (ChordOntology)
========================================================================================================================

Overview
--------
The Chord Ontology is an ontology for describing chords in musical pieces.

:Domain: Arts & Humanities
:Category: Musical Works
:Current Version: 1.0
:Last Updated: 2007-10-25
:Creator: Yves Raimond, Samer Abdallah, Centre for Digital Music, Queen Mary, University of London
:License: Creative Commons 3.0
:Format: RDF/XML
:Download: `Chord Ontology (ChordOntology) Homepage <https://github.com/motools/chordontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 196
    - **Total Edges**: 456
    - **Root Nodes**: 11
    - **Leaf Nodes**: 66

Knowledge coverage
------------------
    - Classes: 9
    - Individuals: 108
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 4
    - **Minimum Depth**: 0
    - **Average Depth**: 1.19
    - **Depth Variance**: 0.77

Breadth metrics
------------------
    - **Maximum Breadth**: 31
    - **Minimum Breadth**: 1
    - **Average Breadth**: 11.60
    - **Breadth Variance**: 109.44

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 108
    - **Taxonomic Relations**: 4
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 21.60

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import ChordOntology

    # Initialize and load ontology
    ontology = ChordOntology()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
