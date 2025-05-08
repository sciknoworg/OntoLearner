Reaction Ontology (RXNO)
========================================================================================================================

Overview
--------
RXNO is the name reaction ontology. It contains more than 500 classes representing organic reactions
such as the Diels–Alder cyclization.

:Domain: Chemistry
:Category: Chemistry
:Current Version: None
:Last Updated: 2021-12-16
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `Reaction Ontology (RXNO) Homepage <https://github.com/rsc-ontologies/rxno>`_

Graph Metrics
-------------
    - **Total Nodes**: 5676
    - **Total Edges**: 14841
    - **Root Nodes**: 845
    - **Leaf Nodes**: 2924

Knowledge coverage
------------------
    - Classes: 1109
    - Individuals: 0
    - Properties: 14

Hierarchical metrics
--------------------
    - **Maximum Depth**: 8
    - **Minimum Depth**: 0
    - **Average Depth**: 1.71
    - **Depth Variance**: 1.67

Breadth metrics
------------------
    - **Maximum Breadth**: 2230
    - **Minimum Breadth**: 12
    - **Average Breadth**: 623.00
    - **Breadth Variance**: 588146.89

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1990
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import RXNO

    # Initialize and load ontology
    ontology = RXNO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
