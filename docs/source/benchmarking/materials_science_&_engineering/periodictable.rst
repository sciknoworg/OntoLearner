Periodic Table of the Elements Ontology (PeriodicTable)
==========================

Overview
--------
PeriodicTable.owl is a representation of the Periodic Table of the Elements in the OWL Web Ontology Language.
It provides reference data to support Semantic Web applications in chemistry and related disciplines.

:Domain: Materials Science & Engineering
:Category: Periodic Table of Elements
:Current Version: 1.10
:Last Updated: 2004/02/05
:Creator: Michael Cook
:License: None
:Format: OWL
:Download: `Periodic Table of the Elements Ontology (PeriodicTable) Homepage <https://www.daml.org/2003/01/periodictable/>`_

Graph Metrics
-------------
    - **Total Nodes**: 730
    - **Total Edges**: 1845
    - **Root Nodes**: 2
    - **Leaf Nodes**: 521

Knowledge coverage
------------------
    - Classes: 6
    - Individuals: 156
    - Properties: 13

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.75
    - **Depth Variance**: 0.19

Breadth metrics
------------------
    - **Maximum Breadth**: 6
    - **Minimum Breadth**: 2
    - **Average Breadth**: 4.00
    - **Breadth Variance**: 4.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 156
    - **Taxonomic Relations**: 302
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 7.09

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PeriodicTable

    # Initialize and load ontology
    ontology = PeriodicTable()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
