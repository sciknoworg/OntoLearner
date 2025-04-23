Smart Applications REFerence ontology (SAREF)
==========================

Overview
--------
The Smart Applications REFerence (SAREF) suite of ontologies forms a shared model of consensus
intended to enable semantic interoperability between solutions from different providers
and among various activity sectors in the Internet of Things (IoT),
thus contributing to the development of data spaces. SAREF is published as a set of open standards
produced by ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M).

:Domain: Web & Internet
:Category: interoperability
:Current Version: 3.2.1
:Last Updated: 2020-12-31
:Creator: ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M)
:License: None
:Format: OWL, RDF/XML, TTL, JSON-LD
:Download: `Smart Applications REFerence ontology (SAREF) Homepage <https://saref.etsi.org/core/v3.2.1/>`_

Graph Metrics
-------------
    - **Total Nodes**: 804
    - **Total Edges**: 1720
    - **Root Nodes**: 14
    - **Leaf Nodes**: 376

Knowledge coverage
------------------
    - Classes: 129
    - Individuals: 10
    - Properties: 89

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.07
    - **Depth Variance**: 0.06

Breadth metrics
------------------
    - **Maximum Breadth**: 14
    - **Minimum Breadth**: 1
    - **Average Breadth**: 7.50
    - **Breadth Variance**: 42.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 10
    - **Taxonomic Relations**: 224
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 2.50

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SAREF

    # Initialize and load ontology
    ontology = SAREF()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
