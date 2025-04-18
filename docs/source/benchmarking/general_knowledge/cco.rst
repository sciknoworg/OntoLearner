Common Core Ontologies (CCO)
============================

Overview
-----------------
The Common Core Ontologies (CCO) is a widely-used suite of eleven ontologies that consist
of logically well-defined generic terms and relations among them reflecting entities across all domains of interest.

:Domain: General Knowledge
:Category: General
:Current Version: 2.0
:Last Updated: 2024-11-06
:Creator:
:License: BSD-3-Clause license
:Format: TTL
:Download: `CCO Homepage <https://github.com/CommonCoreOntology/CommonCoreOntologies>`_
:Documentation: `CCO Documentation <https://github.com/CommonCoreOntology/CommonCoreOntologies>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 6002
    - **Root Nodes**: 19
    - **Leaf Nodes**: 3389
    - **Maximum Depth**: 1
    - **Edges**: 13554

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 362
    - **Taxonomic Relations**: 1806
    - **Non-taxonomic Relations**: 86
    - **Average Terms per Type**: 8.83

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import CCO

    # Initialize and load ontology
    ontology = CCO()
    ontology.load("path/to/cco.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
