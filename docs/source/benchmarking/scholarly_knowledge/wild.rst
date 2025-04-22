Workflows in Linked Data (WiLD)
==========================

Overview
--------
Ontology to describe Workflows in Linked Data.

:Domain: Scholarly Knowledge
:Category: Materials Science
:Current Version: None
:Last Updated: 2020-06-10
:Creator: Tobias Käfer
:License: DBpedia License
:Format: TTL
:Download: `Workflows in Linked Data (WiLD) Homepage <https://databus.dbpedia.org/ontologies/purl.org/wild--vocab/2020.06.10-210552>`_

Graph Metrics
-------------
    - **Total Nodes**: 50
    - **Total Edges**: 91
    - **Root Nodes**: 21
    - **Leaf Nodes**: 9

Knowledge coverage
------------------
    - Classes: 16
    - Individuals: 4
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.58
    - **Depth Variance**: 0.33

Breadth metrics
------------------
    - **Maximum Breadth**: 22
    - **Minimum Breadth**: 2
    - **Average Breadth**: 15.00
    - **Breadth Variance**: 84.67

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 4
    - **Taxonomic Relations**: 9
    - **Non-taxonomic Relations**: 4
    - **Average Terms per Type**: 0.24

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import WiLD

    # Initialize and load ontology
    ontology = WiLD()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
