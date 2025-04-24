The ontology of data analysis and management (EDAM)
========================================================================================================================

Overview
--------
EDAM is a domain ontology of data analysis and data management in bio- and other sciences, and science-based applications.
It comprises concepts related to analysis, modelling, optimisation, and data life cycle. Targetting usability by diverse users,
the structure of EDAM is relatively simple, divided into 4 main sections: Topic, Operation, Data (incl. Identifier), and Format.

:Domain: General Knowledge
:Category: General
:Current Version: 1.25-20240924T0027Z-unstable(1.26)
:Last Updated: 24.09.2024
:Creator: Federico Bianchini, Hervé Ménager, Jon Ison, Matúš Kalaš
:License: Creative Commons 4.0
:Format: owl
:Download: `The ontology of data analysis and management (EDAM) Homepage <https://terminology.tib.eu/ts/ontologies/edam>`_

Graph Metrics
-------------
    - **Total Nodes**: 12367
    - **Total Edges**: 36215
    - **Root Nodes**: 176
    - **Leaf Nodes**: 8223

Knowledge coverage
------------------
    - Classes: 3513
    - Individuals: 0
    - Properties: 12

Hierarchical metrics
--------------------
    - **Maximum Depth**: 10
    - **Minimum Depth**: 0
    - **Average Depth**: 2.75
    - **Depth Variance**: 4.24

Breadth metrics
------------------
    - **Maximum Breadth**: 635
    - **Minimum Breadth**: 5
    - **Average Breadth**: 196.55
    - **Breadth Variance**: 31795.52

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 9745
    - **Non-taxonomic Relations**: 1314
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import EDAM

    # Initialize and load ontology
    ontology = EDAM()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
