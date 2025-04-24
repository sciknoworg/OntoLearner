Laser Powder Bed Fusion Ontology (LPBFO)
========================================================================================================================

Overview
--------
The LPBF Ontology can be used to describe the additive manufacturing of a component via
Laser Powder Bed Fusion (LPBF) / Selective Laser Melting (SLM). The ontology builds on BFO2.0
and BWMD_mid and has been developed to be used in conjunction with the digital workflows provided
by Fraunhofer IWM. If possible, the terminology within this ontology was used as provided by ISO/ASTM 52900:2015.
Recently, classes relevant for Life Cycle Analysis (LCA) were added that enable sustainability assessment.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 1.1.9
:Last Updated: 2022-09-20
:Creator: Fraunhofer IWM
:License: Creative Commons 4.0
:Format: OWL, RDF/XML, Turtle
:Download: `Laser Powder Bed Fusion Ontology (LPBFO) Homepage <https://matportal.org/ontologies/LPBFO>`_

Graph Metrics
-------------
    - **Total Nodes**: 1835
    - **Total Edges**: 3548
    - **Root Nodes**: 129
    - **Leaf Nodes**: 1056

Knowledge coverage
------------------
    - Classes: 508
    - Individuals: 0
    - Properties: 38

Hierarchical metrics
--------------------
    - **Maximum Depth**: 90
    - **Minimum Depth**: 0
    - **Average Depth**: 13.97
    - **Depth Variance**: 590.11

Breadth metrics
------------------
    - **Maximum Breadth**: 276
    - **Minimum Breadth**: 1
    - **Average Breadth**: 10.16
    - **Breadth Variance**: 1618.27

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 507
    - **Non-taxonomic Relations**: 22
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import LPBFO

    # Initialize and load ontology
    ontology = LPBFO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
