Chemical Information Ontology (CHEMINF)
========================================================================================================================

Overview
--------
The chemical information ontology (cheminf) describes information entities about chemical entities.
It provides qualitative and quantitative attributes to richly describe chemicals.
Includes terms for the descriptors commonly used in cheminformatics software applications
and the algorithms which generate them.

:Domain: Chemistry
:Category: Chemistry
:Current Version: 2.1.0
:Last Updated: None
:Creator: Egon Willighagen, Nina Jeliazkova, Ola Spjuth, Valery Tkachenko
:License: Creative Commons 1.0
:Format: OWL
:Download: `Chemical Information Ontology (CHEMINF) Homepage <https://terminology.tib.eu/ts/ontologies/CHEMINF>`_

Graph Metrics
-------------
    - **Total Nodes**: 1467
    - **Total Edges**: 2837
    - **Root Nodes**: 213
    - **Leaf Nodes**: 435

Knowledge coverage
------------------
    - Classes: 358
    - Individuals: 0
    - Properties: 52

Hierarchical metrics
--------------------
    - **Maximum Depth**: 16
    - **Minimum Depth**: 0
    - **Average Depth**: 1.73
    - **Depth Variance**: 9.21

Breadth metrics
------------------
    - **Maximum Breadth**: 213
    - **Minimum Breadth**: 1
    - **Average Breadth**: 29.24
    - **Breadth Variance**: 3411.59

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 594
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CHEMINF

    # Initialize and load ontology
    ontology = CHEMINF()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
