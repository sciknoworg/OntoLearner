The Timeline Ontology
======================

Overview
-----------------
The Timeline Ontology is centered around the notion of timeline, seen here as a way to identify a temporal backbone.
A timeline may support a signal, a video, a score, a work, etc.

:Domain: Music
:Category: Artwork
:Current Version: 1.0
:Last Updated: 25th October 2007
:Producer: Christopher Sutton, Yves Raimond, Matthias Mauch
:License: Creative Commons 1.0
:Format: RDF/XML
:Download: `Timeline Homepage <https://github.com/motools/timelineontology>`_
:Documentation: `Timeline Documentation <https://github.com/motools/timelineontology>`_


Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 286
    - **Root Nodes**: 20
    - **Leaf Nodes**: 89
    - **Maximum Depth**: 5
    - **Edges**: 652

Dataset Statistics
-------------------
    - **Term Types**: 2
    - **Taxonomic Relations**: 106
    - **Non-taxonomic Relations**: 17
    - **Average Terms per Type**: 0.12

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import Timeline

    # Initialize and load ontology
    timeline = Timeline()
    timeline.load("path/to/ontology.rdf")
    # Extract datasets
    data = timeline.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
