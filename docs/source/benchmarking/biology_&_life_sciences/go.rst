Gene Ontology (GO)
==========================

Overview
--------
The Gene Ontology (GO) Provides structured controlled vocabularies for the annotation of gene products
with respect to their molecular function, cellular component, and biological role.

:Domain: Biology & Life Sciences
:Category: Molecular Biology, Genetics
:Current Version: None
:Last Updated: 2024-11-03
:Creator: None
:License: Creative Commons 4.0
:Format: OWL, OBO, JSON
:Download: `Gene Ontology (GO) Homepage <https://geneontology.org/docs/download-ontology/>`_

Graph Metrics
-------------
    - **Total Nodes**: 534820
    - **Total Edges**: 1419487
    - **Root Nodes**: 133995
    - **Leaf Nodes**: 293179

Knowledge coverage
------------------
    - Classes: 62046
    - Individuals: 0
    - Properties: 9

Hierarchical metrics
--------------------
    - **Maximum Depth**: 7
    - **Minimum Depth**: 0
    - **Average Depth**: 1.24
    - **Depth Variance**: 1.08

Breadth metrics
------------------
    - **Maximum Breadth**: 204650
    - **Minimum Breadth**: 5
    - **Average Breadth**: 66849.38
    - **Breadth Variance**: 6433980645.23

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 206031
    - **Non-taxonomic Relations**: 14155
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import GO

    # Initialize and load ontology
    ontology = GO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
