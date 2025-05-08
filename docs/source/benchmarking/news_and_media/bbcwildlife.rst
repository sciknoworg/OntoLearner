BBC Wildlife Ontology (BBCWildlife)
========================================================================================================================

Overview
--------
A simple vocabulary for describing biological species and related taxa. The vocabulary defines terms
for describing the names and ranking of taxa, as well as providing support for describing their habitats,
conservation status, and behavioural characteristics, etc.

:Domain: News and Media
:Category: Wildlife
:Current Version: 1.1
:Last Updated: 2013/12/18
:Creator: https://www.ldodds.com#me, http://tomscott.name/
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Wildlife Ontology (BBCWildlife) Homepage <https://www.bbc.co.uk/ontologies/wildlife-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 157
    - **Total Edges**: 414
    - **Root Nodes**: 1
    - **Leaf Nodes**: 93

Knowledge coverage
------------------
    - Classes: 31
    - Individuals: 0
    - Properties: 31

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.67
    - **Depth Variance**: 0.22

Breadth metrics
------------------
    - **Maximum Breadth**: 2
    - **Minimum Breadth**: 1
    - **Average Breadth**: 1.50
    - **Breadth Variance**: 0.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 23
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBCWildlife

    # Initialize and load ontology
    ontology = BBCWildlife()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
