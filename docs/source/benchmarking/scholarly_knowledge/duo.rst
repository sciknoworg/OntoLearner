The Data Use Ontology (DUO)
===========================

Overview
-----------------
DUO is an ontology which represent data use conditions.

:Domain: Scholarly Knowledge
:Category: Scholarly Knowledge
:Current Version: 1.0
:Last Updated: 2025-02-17
:Producer: N/A
:License: Creative Commons 4.0
:Format: OWL
:Download: `DUO Homepage <https://terminology.tib.eu/ts/ontologies/DUO/>`_
:Documentation: `DUO Documentation <https://terminology.tib.eu/ts/ontologies/DUO/>`_

Base Metrics
---------------
    - Classes: 308
    - Properties: 134
    - Individuals: 20

Graph Metrics:
------------------
    - **Nodes**: 476
    - **Root Nodes**: 196
    - **Leaf Nodes**: 168
    - **Maximum Depth**: 10
    - **Edges**: 583

Dataset Statistics
------------------
Generated Benchmarks:
    * **Term Types**: 0
    * **Taxonomic Relations**: 309
    * **Non-taxonomic Relations**: 0
    * **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology import DUOOntology

    # Initialize and load ontology
    duo = DUOOntology()
    # Load ontology from file
    duo.load("path/to/duo.owl")
    # Extract datasets
    data = duo.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
