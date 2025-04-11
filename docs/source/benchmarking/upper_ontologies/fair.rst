FAIR Vocabulary (FAIR)
================

Overview
-----------------
This is the formal vocabulary (ontology) describing the FAIR principles.

:Domain: Upper Ontology
:Category: Data, Metadata, Ontology
:Current Version:
:Last Updated:
:Producer:
:License: Creative Commons 4.0
:Format: OWL
:Download: `FAIR Homepage <https://terminology.tib.eu/ts/ontologies/FAIR>`_
:Documentation: `FAIR Documentation <https://terminology.tib.eu/ts/ontologies/FAIR>`_

Base Metrics
---------------
    - Classes: 5
    - Individuals: 9
    - Properties: 20

Graph Metrics:
------------------
    - **Total Nodes**: 92
    - **Root Nodes**: 9
    - **Leaf Nodes**: 37
    - **Maximum Depth**: 1
    - **Edges**: 180

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 19
    - **Taxonomic Relations**: 3
    - **Non-taxonomic Relations**: 5
    - **Average Terms per Type**: 1.19

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import FAIR

    # Initialize and load ontology
    ontology = FAIR()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
