Vibrational Spectroscopy Ontology (VIBSO)
==========================

Overview
--------
The Vibration Spectroscopy Ontology defines technical terms with which research data produced
in vibrational spectroscopy experiments can be semantically enriched, made machine readable and FAIR.

:Domain: Chemistry
:Category: Spectroscopy
:Current Version: 2024-09-23
:Last Updated: 2024-09-23
:Creator: VIBSO Workgroup
:License: Creative Commons Attribution 4.0
:Format: OWL
:Download: `Vibrational Spectroscopy Ontology (VIBSO) Homepage <https://terminology.tib.eu/ts/ontologies/vibso>`_

Graph Metrics
-------------
    - **Total Nodes**: 4007
    - **Total Edges**: 8009
    - **Root Nodes**: 328
    - **Leaf Nodes**: 2547

Knowledge coverage
------------------
    - Classes: 598
    - Individuals: 40
    - Properties: 53

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 2.03
    - **Depth Variance**: 2.77

Breadth metrics
------------------
    - **Maximum Breadth**: 1131
    - **Minimum Breadth**: 1
    - **Average Breadth**: 188.29
    - **Breadth Variance**: 98075.49

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 40
    - **Taxonomic Relations**: 856
    - **Non-taxonomic Relations**: 125
    - **Average Terms per Type**: 1.48

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import VIBSO

    # Initialize and load ontology
    ontology = VIBSO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
