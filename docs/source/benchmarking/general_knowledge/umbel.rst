Upper Mapping and Binding Exchange Layer Vocabulary (UMBEL)
========================================================================================================================

Overview
--------
UMBEL is the Upper Mapping and Binding Exchange Layer, designed to help content interoperate on the Web.
UMBEL provides two valuable functions: First, it is a broad, general reference structure of 34,000 concepts,
which provides a scaffolding to link and interoperate other datasets and domain vocabularies.
Second, it is a base vocabulary for the construction of other concept-based domain ontologies,
also designed for interoperation.

:Domain: General Knowledge
:Category: Web Development
:Current Version: 1.50
:Last Updated: May 10, 2016
:Creator: None
:License: None
:Format: n3
:Download: `Upper Mapping and Binding Exchange Layer Vocabulary (UMBEL) Homepage <https://github.com/structureddynamics/UMBEL/tree/master/Ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 1185
    - **Total Edges**: 2868
    - **Root Nodes**: 64
    - **Leaf Nodes**: 302

Knowledge coverage
------------------
    - Classes: 99
    - Individuals: 10
    - Properties: 42

Hierarchical metrics
--------------------
    - **Maximum Depth**: 42
    - **Minimum Depth**: 0
    - **Average Depth**: 10.19
    - **Depth Variance**: 83.14

Breadth metrics
------------------
    - **Maximum Breadth**: 162
    - **Minimum Breadth**: 1
    - **Average Breadth**: 27.42
    - **Breadth Variance**: 1013.69

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 10
    - **Taxonomic Relations**: 64
    - **Non-taxonomic Relations**: 33
    - **Average Terms per Type**: 10.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import UMBEL

    # Initialize and load ontology
    ontology = UMBEL()
    ontology.load("path/to/ontology.n3")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
