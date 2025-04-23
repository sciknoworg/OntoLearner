Digital Buildings Ontology (DBO)
==========================

Overview
--------
The Digital Buildings ontology (DBO) is used by Google to represent structured information
about buildings and building-installed equipment.

:Domain: Industry
:Category: Building Information
:Current Version: 0.0.1
:Last Updated: 02/23/2023
:Creator: Google
:License: Apache 2.0
:Format: OWL, CSV, RDF/XML
:Download: `Digital Buildings Ontology (DBO) Homepage <https://github.com/google/digitalbuildings?tab=readme-ov-file>`_

Graph Metrics
-------------
    - **Total Nodes**: 13152
    - **Total Edges**: 32491
    - **Root Nodes**: 1
    - **Leaf Nodes**: 686

Knowledge coverage
------------------
    - Classes: 3032
    - Individuals: 35
    - Properties: 7

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 1.57
    - **Depth Variance**: 0.82

Breadth metrics
------------------
    - **Maximum Breadth**: 3
    - **Minimum Breadth**: 1
    - **Average Breadth**: 1.75
    - **Breadth Variance**: 0.69

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 35
    - **Taxonomic Relations**: 37016
    - **Non-taxonomic Relations**: 12
    - **Average Terms per Type**: 1.09

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import DBO

    # Initialize and load ontology
    ontology = DBO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
