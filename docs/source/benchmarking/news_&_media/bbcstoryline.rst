BBC Storyline Ontology
==========================

Overview
--------
The News Storyline Ontology is a generic model for describing and organising the stories news organisations tell.
The ontology is intended to be flexible to support any given news or media publisher's approach to handling news stories.
At the heart of the ontology, is the concept of Storyline. As a nuance of the English language the word 'story'
has multiple meanings. In news organisations, a story can be an individual piece of content,
such as an article or news report. It can also be the editorial view on events occurring in the world.

:Domain: News & Media
:Category: Storyline
:Current Version: 0.3
:Last Updated: 2013-05-01
:Creator: http://uk.linkedin.com/in/paulwilton, http://www.bbc.co.uk/blogs/internet/authors/Jeremy_Tarling, http://uk.linkedin.com/in/jarredmcginnis
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Storyline Ontology Homepage <https://iptc.org/thirdparty/bbc-ontologies/storyline.html>`_

Graph Metrics
-------------
    - **Total Nodes**: 74
    - **Total Edges**: 157
    - **Root Nodes**: 0
    - **Leaf Nodes**: 53

Knowledge coverage
------------------
    - Classes: 6
    - Individuals: 0
    - Properties: 12

Hierarchical metrics
--------------------
    - **Maximum Depth**: 0
    - **Minimum Depth**: 0
    - **Average Depth**: 0.00
    - **Depth Variance**: 0.00

Breadth metrics
------------------
    - **Maximum Breadth**: 0
    - **Minimum Breadth**: 0
    - **Average Breadth**: 0.00
    - **Breadth Variance**: 0.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBCStoryline

    # Initialize and load ontology
    ontology = BBCStoryline()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
