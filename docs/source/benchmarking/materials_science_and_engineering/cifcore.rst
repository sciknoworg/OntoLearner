Crystallographic Information Framework Core Dictionary (CIFCore)
========================================================================================================================

Overview
--------
(1) to explain the historical development of CIF dictionaries to define in a machine-actionable manner the contents
of data files covering various aspects of crystallography and related structural sciences; (2) to demonstrate
some of the more complex types of information that can be handled with this approach.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 0.1.0
:Last Updated: May 24, 2023
:Creator: None
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Crystallographic Information Framework Core Dictionary (CIFCore) Homepage <https://github.com/emmo-repo/CIF-ontology?tab=readme-ov-file>`_

Graph Metrics
-------------
    - **Total Nodes**: 4494
    - **Total Edges**: 15377
    - **Root Nodes**: 1
    - **Leaf Nodes**: 3310

Knowledge coverage
------------------
    - Classes: 1182
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.75
    - **Depth Variance**: 0.19

Breadth metrics
------------------
    - **Maximum Breadth**: 3
    - **Minimum Breadth**: 1
    - **Average Breadth**: 2.00
    - **Breadth Variance**: 1.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 27150
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CIFCore

    # Initialize and load ontology
    ontology = CIFCore()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
