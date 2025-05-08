The Platform MaterialDigital core ontology (PMDco)
========================================================================================================================

Overview
--------
The PMD Core Ontology (PMDco) is a comprehensive framework for representing knowledge that encompasses
fundamental concepts from the domains of materials science and engineering (MSE). The PMDco
has been designed as a mid-level ontology to establish a connection between specific MSE application ontologies
and the domain neutral concepts found in established top-level ontologies. The primary goal of the PMDco
is to promote interoperability between diverse domains.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 3.0.0-alpha1
:Last Updated: 2025-03-20
:Creator: Jannis Grundmann
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `The Platform MaterialDigital core ontology (PMDco) Homepage <https://github.com/materialdigital/core-ontology?tab=readme-ov-file>`_

Graph Metrics
-------------
    - **Total Nodes**: 4207
    - **Total Edges**: 8103
    - **Root Nodes**: 85
    - **Leaf Nodes**: 2365

Knowledge coverage
------------------
    - Classes: 1002
    - Individuals: 0
    - Properties: 66

Hierarchical metrics
--------------------
    - **Maximum Depth**: 19
    - **Minimum Depth**: 0
    - **Average Depth**: 3.90
    - **Depth Variance**: 11.78

Breadth metrics
------------------
    - **Maximum Breadth**: 161
    - **Minimum Breadth**: 1
    - **Average Breadth**: 40.45
    - **Breadth Variance**: 2084.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 903
    - **Non-taxonomic Relations**: 19
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PMDco

    # Initialize and load ontology
    ontology = PMDco()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
