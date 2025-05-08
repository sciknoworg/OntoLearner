FIX Ontology (FIX)
========================================================================================================================

Overview
--------
An ontology of physico-chemical methods and properties.

:Domain: Chemistry
:Category: Chemicals, Properties
:Current Version: 2020-04-13
:Last Updated: 2020-04-13
:Creator: None
:License: None
:Format: OWL
:Download: `FIX Ontology (FIX) Homepage <https://terminology.tib.eu/ts/ontologies/FIX>`_

Graph Metrics
-------------
    - **Total Nodes**: 3402
    - **Total Edges**: 7621
    - **Root Nodes**: 22
    - **Leaf Nodes**: 2147

Knowledge coverage
------------------
    - Classes: 1163
    - Individuals: 0
    - Properties: 5

Hierarchical metrics
--------------------
    - **Maximum Depth**: 7
    - **Minimum Depth**: 0
    - **Average Depth**: 2.46
    - **Depth Variance**: 2.32

Breadth metrics
------------------
    - **Maximum Breadth**: 75
    - **Minimum Breadth**: 2
    - **Average Breadth**: 36.25
    - **Breadth Variance**: 666.69

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2751
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import FIX

    # Initialize and load ontology
    ontology = FIX()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
