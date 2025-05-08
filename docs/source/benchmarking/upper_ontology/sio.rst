Semanticscience Integrated Ontology (SIO)
========================================================================================================================

Overview
--------
The semanticscience integrated ontology (SIO) provides a simple, integrated upper level ontology (types, relations)
for consistent knowledge representation across physical, processual and informational entities.
This project provides foundational support for the Bio2RDF (http://bio2rdf.org) and SADI (http://sadiframework.org) projects.

:Domain: Upper Ontology
:Category: Basic
:Current Version: 1.59
:Last Updated: 03/25/2024
:Creator: M. Dumontier
:License: Creative Commons 4.0
:Format: OWL
:Download: `Semanticscience Integrated Ontology (SIO) Homepage <https://bioportal.bioontology.org/ontologies/SIO>`_

Graph Metrics
-------------
    - **Total Nodes**: 7811
    - **Total Edges**: 15701
    - **Root Nodes**: 18
    - **Leaf Nodes**: 4921

Knowledge coverage
------------------
    - Classes: 1726
    - Individuals: 0
    - Properties: 212

Hierarchical metrics
--------------------
    - **Maximum Depth**: 20
    - **Minimum Depth**: 0
    - **Average Depth**: 6.67
    - **Depth Variance**: 12.94

Breadth metrics
------------------
    - **Maximum Breadth**: 186
    - **Minimum Breadth**: 1
    - **Average Breadth**: 63.71
    - **Breadth Variance**: 3373.16

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2019
    - **Non-taxonomic Relations**: 65
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SIO

    # Initialize and load ontology
    ontology = SIO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
