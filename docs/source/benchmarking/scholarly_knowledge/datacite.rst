DataCite Ontology (DataCite)
========================================================================================================================

Overview
--------
The DataCite Ontology (DataCite) is an ontology that enables the metadata properties
of the DataCite Metadata Schema Specification (i.e., a list of metadata properties
for the accurate and consistent identification of a resource for citation
and retrieval purposes) to be described in RDF.

:Domain: Scholarly Knowledge
:Category: Metadata
:Current Version: 3.1
:Last Updated: 15/09/2022
:Creator: David Shotton, Silvio Peroni
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `DataCite Ontology (DataCite) Homepage <https://schema.datacite.org/>`_

Graph Metrics
-------------
    - **Total Nodes**: 260
    - **Total Edges**: 519
    - **Root Nodes**: 14
    - **Leaf Nodes**: 120

Knowledge coverage
------------------
    - Classes: 19
    - Individuals: 70
    - Properties: 10

Hierarchical metrics
--------------------
    - **Maximum Depth**: 8
    - **Minimum Depth**: 0
    - **Average Depth**: 3.21
    - **Depth Variance**: 5.93

Breadth metrics
------------------
    - **Maximum Breadth**: 14
    - **Minimum Breadth**: 3
    - **Average Breadth**: 7.56
    - **Breadth Variance**: 9.80

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 71
    - **Taxonomic Relations**: 55
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 8.88

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import DataCite

    # Initialize and load ontology
    ontology = DataCite()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
