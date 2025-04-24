Molecular Process Ontology (MOP)
========================================================================================================================

Overview
--------
MOP is the molecular process ontology. It contains the molecular processes that underlie
the name reaction ontology RXNO, for example cyclization, methylation and demethylation.

:Domain: Chemistry
:Category: Chemistry, Molecular Biology
:Current Version: 2022-05-11
:Last Updated: 2022-05-11
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `Molecular Process Ontology (MOP) Homepage <https://terminology.tib.eu/ts/ontologies/MOP>`_

Graph Metrics
-------------
    - **Total Nodes**: 15794
    - **Total Edges**: 41157
    - **Root Nodes**: 3693
    - **Leaf Nodes**: 8182

Knowledge coverage
------------------
    - Classes: 3717
    - Individuals: 0
    - Properties: 11

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 1.09
    - **Depth Variance**: 0.63

Breadth metrics
------------------
    - **Maximum Breadth**: 7300
    - **Minimum Breadth**: 3
    - **Average Breadth**: 2253.14
    - **Breadth Variance**: 7474153.55

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 4171
    - **Non-taxonomic Relations**: 47
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MOP

    # Initialize and load ontology
    ontology = MOP()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
