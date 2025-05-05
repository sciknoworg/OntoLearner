Nomisma Ontology (Nomisma)
========================================================================================================================

Overview
--------
Nomisma Ontology is a collaborative project to provide stable digital representations of numismatic concepts according
to the principles of Linked Open Data. These take the form of http URIs that provide access to the information
about a concept in various formats. The project is a collaborative effort of the American Numismatic Society
and the Institute for the Study of the Ancient World at New York University.

:Domain: Arts and Humanities
:Category: Numismatics
:Current Version: None
:Last Updated: 2025-01-22
:Creator: American Numismatic Society, Institute for the Study of the Ancient World
:License: Creative Commons 4.0
:Format: TTL
:Download: `Nomisma Ontology (Nomisma) Homepage <https://www.dainst.org/forschung/projekte/noslug/2098>`_

Graph Metrics
-------------
    - **Total Nodes**: 245
    - **Total Edges**: 431
    - **Root Nodes**: 22
    - **Leaf Nodes**: 113

Knowledge coverage
------------------
    - Classes: 36
    - Individuals: 0
    - Properties: 71

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 0.97
    - **Depth Variance**: 0.73

Breadth metrics
------------------
    - **Maximum Breadth**: 22
    - **Minimum Breadth**: 1
    - **Average Breadth**: 15.00
    - **Breadth Variance**: 67.50

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 13
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import Nomisma

    # Initialize and load ontology
    ontology = Nomisma()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
