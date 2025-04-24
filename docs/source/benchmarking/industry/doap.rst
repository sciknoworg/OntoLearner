The Description of a Project (DOAP) vocabulary
========================================================================================================================

Overview
--------
The Description of a Project (DOAP) vocabulary, described using W3C RDF Schema and
the Web Ontology Language to describe software projects, and in particular open source projects.

:Domain: Industry
:Category: Software
:Current Version: None
:Last Updated: 2020-04-03
:Creator: Edd Wilder-James
:License: Apache License 2.0
:Format: RDF
:Download: `The Description of a Project (DOAP) vocabulary Homepage <https://github.com/ewilderj/doap/blob/master/schema/doap.rdf>`_

Graph Metrics
-------------
    - **Total Nodes**: 496
    - **Total Edges**: 634
    - **Root Nodes**: 1
    - **Leaf Nodes**: 435

Knowledge coverage
------------------
    - Classes: 14
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.75
    - **Depth Variance**: 0.19

Breadth metrics
------------------
    - **Maximum Breadth**: 3
    - **Minimum Breadth**: 1
    - **Average Breadth**: 2.00
    - **Breadth Variance**: 1.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 14
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import DOAP

    # Initialize and load ontology
    ontology = DOAP()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
