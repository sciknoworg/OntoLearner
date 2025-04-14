Ontology of Scientific Experiments (EXPO)
=========================================

Overview
-----------------
Formalise generic knowledge about scientific experimental design, methodology, and results representation.

:Domain: Scholarly Knowledge
:Category: Bio-Informatics, Artificial Intelligence
:Current Version:
:Last Updated:
:Creator:
:License: Academic Free License (AFL)
:Format: OWL
:Download: `EXPO Homepage <https://expo.sourceforge.net/>`_
:Documentation: `EXPO Documentation <https://expo.sourceforge.net/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 858
    - **Root Nodes**: 13
    - **Leaf Nodes**: 265
    - **Maximum Depth**: 37
    - **Edges**: 2921

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1012
    - **Non-taxonomic Relations**: 726
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import EXPO

    # Initialize and load ontology
    ontology = EXPO()
    ontology.load("path/to/expo.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
