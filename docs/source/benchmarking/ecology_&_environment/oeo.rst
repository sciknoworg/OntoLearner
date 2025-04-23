The Open Energy Ontology (OEO)
==========================

Overview
--------
The Open Energy Ontology (OEO) is a domain ontology of the energy system analysis context.
It is developed as part of the Open Energy Family. The OEO is published on GitHub under
an open source license. The language used is the Manchester OWL Syntax, which was chosen
because it is user-friendly for editing and viewing differences of edited files. The OEO is constantly
being extended. The first version of the OEO has been released on June 11th 2020. A Steering Committee (OEO-SC)
was created to accompany the development, increase awareness of the ontology and include it in current projects.

:Domain: Ecology & Environment
:Category: Energy
:Current Version: 2.7.0
:Last Updated: 03/2025
:Creator: None
:License: Creative Commons Attribution 1.0 Generic (CC BY 1.0)
:Format: OWL/XML
:Download: `The Open Energy Ontology (OEO) Homepage <https://github.com/OpenEnergyPlatform/ontology?tab=readme-ov-file>`_

Graph Metrics
-------------
    - **Total Nodes**: 10
    - **Total Edges**: 8
    - **Root Nodes**: 8
    - **Leaf Nodes**: 2

Knowledge coverage
------------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.20
    - **Depth Variance**: 0.16

Breadth metrics
------------------
    - **Maximum Breadth**: 8
    - **Minimum Breadth**: 2
    - **Average Breadth**: 5.00
    - **Breadth Variance**: 9.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 0
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OEO

    # Initialize and load ontology
    ontology = OEO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
