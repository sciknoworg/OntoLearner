Materials Data Science Ontology (MDS)
========================================================================================================================

Overview
--------
Materials Data Science (MDS) is an ontology encompassing multiple domains relevant to materials science,
chemical synthesis and characterizations, photovoltaics and geospatial datasets. The terms used for classes,
subclasses and instances are mapped to PMDCo and BFO Ontologies.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 0.3.0.0
:Last Updated: 03/24/2024
:Creator: SDLE Research Center
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Materials Data Science Ontology (MDS) Homepage <https://matportal.org/ontologies/MDS>`_

Graph Metrics
-------------
    - **Total Nodes**: 657
    - **Total Edges**: 1457
    - **Root Nodes**: 63
    - **Leaf Nodes**: 303

Knowledge coverage
------------------
    - Classes: 363
    - Individuals: 0
    - Properties: 10

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 0.86
    - **Depth Variance**: 0.57

Breadth metrics
------------------
    - **Maximum Breadth**: 87
    - **Minimum Breadth**: 4
    - **Average Breadth**: 46.00
    - **Breadth Variance**: 997.50

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 351
    - **Non-taxonomic Relations**: 128
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MDS

    # Initialize and load ontology
    ontology = MDS()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
