Marine Taxonomy and Life Ontology (MarineTLO)
==========================

Overview
--------
MarineTLO is a top level ontology, generic enough to provide consistent abstractions or
specifications of concepts included in all data models or ontologies of marine data sources and
provide the necessary properties to make this distributed knowledge base a coherent source of
facts relating observational data with the respective spatiotemporal context and categorical
(systematic) domain knowledge. It can be used as the core schema for publishing Linked Data, as
well as for setting up integration systems for the marine domain. It can be extended to any level
of detail on demand, while preserving monotonicity. For its development and evolution we have
adopted an iterative and incremental methodology where a new version is released every two
months. For the implementation we use OWL 2, and to evaluate it we use a set of competency
queries, formulating the domain requirements provided by the related communities.

:Domain: Biology & Life Sciences
:Category: Marine Science, Oceanography
:Current Version: 1.0
:Last Updated: 2017-01-05
:Creator: Information System Laboratory (ISL), Institute of Computer Science (ICS), Foundation for Research and Technology - Hellas (FORTH)
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `Marine Taxonomy and Life Ontology (MarineTLO) Homepage <https://projects.ics.forth.gr/isl/MarineTLO/>`_

Graph Metrics
-------------
    - **Total Nodes**: 372
    - **Total Edges**: 1205
    - **Root Nodes**: 3
    - **Leaf Nodes**: 171

Knowledge coverage
------------------
    - Classes: 104
    - Individuals: 3
    - Properties: 94

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.75
    - **Depth Variance**: 0.44

Breadth metrics
------------------
    - **Maximum Breadth**: 4
    - **Minimum Breadth**: 1
    - **Average Breadth**: 2.67
    - **Breadth Variance**: 1.56

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 113
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.17

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MarineTLO

    # Initialize and load ontology
    ontology = MarineTLO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
