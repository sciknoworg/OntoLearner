LexInfo
==========================

Overview
--------
LexInfo allows us to associate linguistic information to elements in an ontology with respect
to any level of linguistic description and expressivity. LexInfo has been implemented as an OWL ontology
and is available together with an API.

:Domain: Scholarly Knowledge
:Category: Linguistics
:Current Version: 3.0
:Last Updated: None
:Creator: None
:License: Apache 2.0
:Format: RDF
:Download: `LexInfo Homepage <https://lexinfo.net/index.html>`_

Graph Metrics
-------------
    - **Total Nodes**: 3351
    - **Total Edges**: 5435
    - **Root Nodes**: 1
    - **Leaf Nodes**: 2308

Knowledge coverage
------------------
    - Classes: 334
    - Individuals: 276
    - Properties: 189

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.50
    - **Depth Variance**: 0.25

Breadth metrics
------------------
    - **Maximum Breadth**: 1
    - **Minimum Breadth**: 1
    - **Average Breadth**: 1.00
    - **Breadth Variance**: 0.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 288
    - **Taxonomic Relations**: 282
    - **Non-taxonomic Relations**: 75
    - **Average Terms per Type**: 11.52

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import LexInfo

    # Initialize and load ontology
    ontology = LexInfo()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
