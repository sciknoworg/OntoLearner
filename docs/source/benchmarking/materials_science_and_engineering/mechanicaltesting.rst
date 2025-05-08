Mechanical Testing Ontology (MechanicalTesting)
========================================================================================================================

Overview
--------
A domain ontology for mechanical testing based on EMMO.

:Domain: Materials Science and Engineering
:Category: Mechanical Testing
:Current Version: 1.0.0
:Last Updated: None
:Creator: Fraunhofer IWM
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `Mechanical Testing Ontology (MechanicalTesting) Homepage <https://github.com/emmo-repo/domain-mechanical-testing>`_

Graph Metrics
-------------
    - **Total Nodes**: 1365
    - **Total Edges**: 2569
    - **Root Nodes**: 174
    - **Leaf Nodes**: 713

Knowledge coverage
------------------
    - Classes: 369
    - Individuals: 0
    - Properties: 5

Hierarchical metrics
--------------------
    - **Maximum Depth**: 18
    - **Minimum Depth**: 0
    - **Average Depth**: 2.14
    - **Depth Variance**: 4.98

Breadth metrics
------------------
    - **Maximum Breadth**: 466
    - **Minimum Breadth**: 1
    - **Average Breadth**: 66.89
    - **Breadth Variance**: 14051.46

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 36
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MechanicalTesting

    # Initialize and load ontology
    ontology = MechanicalTesting()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
