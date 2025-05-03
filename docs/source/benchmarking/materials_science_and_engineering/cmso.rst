Computational Material Sample Ontology (CMSO)
========================================================================================================================

Overview
--------
CMSO is an ontology that aims to describe computational materials science samples (or structures),
including crystalline defects. Initially focusing on the description at the atomic scale.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.0.1
:Last Updated: None
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `Computational Material Sample Ontology (CMSO) Homepage <https://github.com/OCDO/cmso/tree/main>`_

Graph Metrics
-------------
    - **Total Nodes**: 347
    - **Total Edges**: 556
    - **Root Nodes**: 40
    - **Leaf Nodes**: 192

Knowledge coverage
------------------
    - Classes: 45
    - Individuals: 0
    - Properties: 51

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.56
    - **Depth Variance**: 0.40

Breadth metrics
------------------
    - **Maximum Breadth**: 40
    - **Minimum Breadth**: 6
    - **Average Breadth**: 26.00
    - **Breadth Variance**: 210.67

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 22
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CMSO

    # Initialize and load ontology
    ontology = CMSO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
