BBC Provenance News Ontology
==========================

Overview
--------
An ontology to capture data about the provenance of data in an RDF Triple Store.
This provenance is focused on the immediate providers and not the ultimate source,
so for example, this would record that geodata was provided by the BBC Locator team,
and not geonames. In the Linked Data Platform, this data is applied to contexts or named graphs.
A named graph is, in effect, a 'fourth part' to a triple, hence the term 'quad store'.

:Domain: News & Media
:Category: Provenance
:Current Version: 1.9
:Last Updated: 2012-12-01
:Creator: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Provenance News Ontology Homepage <https://www.bbc.co.uk/ontologies/provenance-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 74
    - **Total Edges**: 151
    - **Root Nodes**: 0
    - **Leaf Nodes**: 48

Knowledge coverage
------------------
    - Classes: 7
    - Individuals: 1
    - Properties: 18

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
    - **Term Types**: 1
    - **Taxonomic Relations**: 6
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.14

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBCProvenance

    # Initialize and load ontology
    ontology = BBCProvenance()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
