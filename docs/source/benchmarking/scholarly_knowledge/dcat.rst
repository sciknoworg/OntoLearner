Data Catalog Vocabulary (DCAT)
========================================================================================================================

Overview
--------
Data Catalog Vocabulary (DCAT) is an RDF vocabulary designed to facilitate interoperability
between data catalogs published on the Web. This document defines the schema and provides examples for its use.
DCAT enables a publisher to describe datasets and data services in a catalog using a standard model
and vocabulary that facilitates the consumption and aggregation of metadata from multiple catalogs.
This can increase the discoverability of datasets and data services. It also makes it possible
to have a decentralized approach to publishing data catalogs and makes federated search for datasets across catalogs
in multiple sites possible using the same query mechanism and structure. Aggregated DCAT metadata
can serve as a manifest file as part of the digital preservation process.

:Domain: Scholarly Knowledge
:Category: Data Catalogs
:Current Version: 3.0
:Last Updated: 22 August 2024
:Creator: Digital Enterprise Research Institute (DERI)
:License: W3C Document License
:Format: RDF/XML, Turtle, JSON-LD
:Download: `Data Catalog Vocabulary (DCAT) Homepage <https://www.w3.org/TR/vocab-dcat-3/>`_

Graph Metrics
-------------
    - **Total Nodes**: 987
    - **Total Edges**: 1313
    - **Root Nodes**: 7
    - **Leaf Nodes**: 908

Knowledge coverage
------------------
    - Classes: 10
    - Individuals: 0
    - Properties: 39

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 2.42
    - **Depth Variance**: 0.58

Breadth metrics
------------------
    - **Maximum Breadth**: 121
    - **Minimum Breadth**: 7
    - **Average Breadth**: 54.50
    - **Breadth Variance**: 2135.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 12
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import DCAT

    # Initialize and load ontology
    ontology = DCAT()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
