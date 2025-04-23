Functional Requirements for Bibliographic Records - object-oriented (FRBRoo)
==========================

Overview
--------
The FRBRoo (Functional Requirements for Bibliographic Records - object-oriented) initiative
is a joint effort of the CIDOC Conceptual Reference Model
and Functional Requirements for Bibliographic Records international working groups to establish
a formal ontology intended to capture and represent the underlying semantics of bibliographic information
and to facilitate the integration, mediation, and interchange of bibliographic and museum information.

:Domain: Scholarly Knowledge
:Category: Bibliographic Records
:Current Version: 2.4
:Last Updated: November 2015
:Creator: None
:License: Creative Commons 4.0
:Format: OWL, RDF
:Download: `Functional Requirements for Bibliographic Records - object-oriented (FRBRoo) Homepage <https://ontome.net/namespace/6#summary>`_

Graph Metrics
-------------
    - **Total Nodes**: 491
    - **Total Edges**: 886
    - **Root Nodes**: 0
    - **Leaf Nodes**: 344

Knowledge coverage
------------------
    - Classes: 83
    - Individuals: 0
    - Properties: 0

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
    - **Taxonomic Relations**: 83
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import FRBRoo

    # Initialize and load ontology
    ontology = FRBRoo()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
