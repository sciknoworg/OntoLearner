CHEBI Integrated Role Ontology (CHIRO)
==========================

Overview
--------
CHEBI provides a distinct role hierarchy. Chemicals in the structural hierarchy are connected via a 'has role' relation.
CHIRO provides links from these roles to useful other classes in other ontologies.
This will allow direct connection between chemical structures (small molecules, drugs) and what they do.
This could be formalized using 'capable of', in the same way Uberon and the Cell Ontology link structures to processes.

:Domain: Chemistry
:Category: Chemicals, Roles
:Current Version: 2015-11-23
:Last Updated: 2015-11-23
:Creator: None
:License: Creative Commons 1.0
:Format: OWL
:Download: `CHEBI Integrated Role Ontology (CHIRO) Homepage <https://terminology.tib.eu/ts/ontologies/chiro>`_

Graph Metrics
-------------
    - **Total Nodes**: 81778
    - **Total Edges**: 197071
    - **Root Nodes**: 14636
    - **Leaf Nodes**: 50439

Knowledge coverage
------------------
    - Classes: 13930
    - Individuals: 0
    - Properties: 15

Hierarchical metrics
--------------------
    - **Maximum Depth**: 16
    - **Minimum Depth**: 0
    - **Average Depth**: 1.36
    - **Depth Variance**: 1.13

Breadth metrics
------------------
    - **Maximum Breadth**: 34719
    - **Minimum Breadth**: 2
    - **Average Breadth**: 4620.24
    - **Breadth Variance**: 105924794.30

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 27299
    - **Non-taxonomic Relations**: 647
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CHIRO

    # Initialize and load ontology
    ontology = CHIRO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
