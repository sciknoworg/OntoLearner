Friend of a Friend (FOAF) Ontology
==========================

Overview
--------
FOAF is a project devoted to linking people and information using the Web.
Regardless of whether information is in people's heads, in physical or digital documents,
or in the form of factual data, it can be linked.

:Domain: Social Sciences
:Category: Social
:Current Version: 0.1
:Last Updated: 14 January 2014
:Creator: Dan Brickley, Libby Miller
:License: Creative Commons
:Format: RDF/XML
:Download: `Friend of a Friend (FOAF) Ontology Homepage <http://xmlns.com/foaf/0.1/>`_

Graph Metrics
-------------
    - **Total Nodes**: 168
    - **Total Edges**: 504
    - **Root Nodes**: 5
    - **Leaf Nodes**: 87

Knowledge coverage
------------------
    - Classes: 15
    - Individuals: 13
    - Properties: 60

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.17
    - **Depth Variance**: 0.14

Breadth metrics
------------------
    - **Maximum Breadth**: 5
    - **Minimum Breadth**: 1
    - **Average Breadth**: 3.00
    - **Breadth Variance**: 4.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 13
    - **Taxonomic Relations**: 11
    - **Non-taxonomic Relations**: 21
    - **Average Terms per Type**: 3.25

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import FOAF

    # Initialize and load ontology
    ontology = FOAF()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
