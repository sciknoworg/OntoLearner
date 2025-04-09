Linking Open Descriptions of Events (LODE)
==========================================

Overview
-----------------
People conventionally refer to an action or occurrence taking place at a certain time
at a specific location as an event. This notion is potentially useful for connecting individual facts
recorded in the rapidly growing collection of linked data sets and for discovering more complex relationships
between data. The LODE provide an overview and comparison of existing event models,
looking at the different choices they make of how to represent events. It is a model for publishing records
of events as Linked Data. A tools for populating this model and a prototype “event directory” web service,
which can be used to locate stable URIs for events that have occurred,
provide RDFS+OWL descriptions and link to related resources.

:Domain: Events
:Category: Events
:Current Version: 2020-10-31
:Last Updated: 2020-10-31
:Producer: Ryan Shaw
:License: Creative Commons Attribution 3.0
:Format: RDF, TTL
:Download: `LODE Homepage <https://linkedevents.org/ontology/>`_
:Documentation: `LODE Documentation <https://linkedevents.org/ontology/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 81
    - **Root Nodes**: 7
    - **Leaf Nodes**: 59
    - **Maximum Depth**: 4
    - **Edges**: 115

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 4
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import LODE

    # Initialize and load ontology
    ontology = LODE()
    ontology.load("path/to/ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
