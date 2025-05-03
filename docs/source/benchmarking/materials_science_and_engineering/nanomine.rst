NanoMine Ontology (NanoMine)
========================================================================================================================

Overview
--------
Polymer Nanocomposites based ontology which enable researchers to develop and test
broad-reaching hypotheses about how inter-relationships between different materials
processing methods and composition result in specific changes in material properties.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: None
:Last Updated: None
:Creator: None
:License: APACHE 2.0
:Format: TTL
:Download: `NanoMine Ontology (NanoMine) Homepage <https://github.com/tetherless-world/nanomine-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 496
    - **Total Edges**: 971
    - **Root Nodes**: 0
    - **Leaf Nodes**: 263

Knowledge coverage
------------------
    - Classes: 157
    - Individuals: 0
    - Properties: 0

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
    - **Term Types**: 0
    - **Taxonomic Relations**: 321
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import NanoMine

    # Initialize and load ontology
    ontology = NanoMine()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
