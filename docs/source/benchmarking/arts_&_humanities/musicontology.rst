Music Ontology (MusicOntology)
========================================================================================================================

Overview
--------
The Music Ontology Specification provides main concepts and
properties fo describing music (i.e. artists, albums and tracks)
on the Semantic Web.

:Domain: Arts & Humanities
:Category: Music Theory
:Current Version: 2.1.5
:Last Updated: 2013/07/22
:Creator: Knowledge Media Institute, Open University
:License: Creative Commons 4.0
:Format: RDF/XML
:Download: `Music Ontology (MusicOntology) Homepage <https://github.com/motools/musicontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 662
    - **Total Edges**: 1844
    - **Root Nodes**: 39
    - **Leaf Nodes**: 268

Knowledge coverage
------------------
    - Classes: 92
    - Individuals: 13
    - Properties: 165

Hierarchical metrics
--------------------
    - **Maximum Depth**: 7
    - **Minimum Depth**: 0
    - **Average Depth**: 1.70
    - **Depth Variance**: 1.89

Breadth metrics
------------------
    - **Maximum Breadth**: 66
    - **Minimum Breadth**: 2
    - **Average Breadth**: 26.25
    - **Breadth Variance**: 621.44

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 13
    - **Taxonomic Relations**: 67
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 6.50

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MusicOntology

    # Initialize and load ontology
    ontology = MusicOntology()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
