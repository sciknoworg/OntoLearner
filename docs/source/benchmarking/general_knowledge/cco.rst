Common Core Ontologies (CCO)
==========================

Overview
--------
The Common Core Ontologies (CCO) is a widely-used suite of eleven ontologies that consist
of logically well-defined generic terms and relations among them reflecting entities across all domains of interest.

:Domain: General Knowledge
:Category: General
:Current Version: 2.0
:Last Updated: 2024-11-06
:Creator: None
:License: BSD-3-Clause license
:Format: TTL
:Download: `Common Core Ontologies (CCO) Homepage <https://github.com/CommonCoreOntology/CommonCoreOntologies>`_

Graph Metrics
-------------
    - **Total Nodes**: 6002
    - **Total Edges**: 13554
    - **Root Nodes**: 19
    - **Leaf Nodes**: 3389

Knowledge coverage
------------------
    - Classes: 1539
    - Individuals: 350
    - Properties: 277

Hierarchical metrics
--------------------
    - **Maximum Depth**: 10
    - **Minimum Depth**: 0
    - **Average Depth**: 4.35
    - **Depth Variance**: 5.00

Breadth metrics
------------------
    - **Maximum Breadth**: 56
    - **Minimum Breadth**: 2
    - **Average Breadth**: 23.18
    - **Breadth Variance**: 276.88

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 362
    - **Taxonomic Relations**: 1806
    - **Non-taxonomic Relations**: 86
    - **Average Terms per Type**: 8.83

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CCO

    # Initialize and load ontology
    ontology = CCO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
