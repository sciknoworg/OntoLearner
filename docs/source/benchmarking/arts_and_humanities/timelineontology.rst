Timeline Ontology (TimelineOntology)
========================================================================================================================

Overview
--------
The Timeline Ontology is centered around the notion of timeline,
seen here as a way to identify a temporal backbone.
A timeline may support a signal, a video, a score, a work, etc.

:Domain: Arts and Humanities
:Category: Music Theory
:Current Version: 1.0
:Last Updated: 25th October 2007
:Creator: Christopher Sutton, Yves Raimond, Matthias Mauch
:License: Creative Commons 1.0
:Format: RDF
:Download: `Timeline Ontology (TimelineOntology) Homepage <https://github.com/motools/timelineontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 286
    - **Total Edges**: 652
    - **Root Nodes**: 20
    - **Leaf Nodes**: 89

Knowledge coverage
------------------
    - Classes: 47
    - Individuals: 2
    - Properties: 46

Hierarchical metrics
--------------------
    - **Maximum Depth**: 5
    - **Minimum Depth**: 0
    - **Average Depth**: 1.28
    - **Depth Variance**: 1.89

Breadth metrics
------------------
    - **Maximum Breadth**: 20
    - **Minimum Breadth**: 2
    - **Average Breadth**: 9.67
    - **Breadth Variance**: 56.89

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 2
    - **Taxonomic Relations**: 28
    - **Non-taxonomic Relations**: 10
    - **Average Terms per Type**: 1.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import TimelineOntology

    # Initialize and load ontology
    ontology = TimelineOntology()
    ontology.load("path/to/ontology.RDF")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
