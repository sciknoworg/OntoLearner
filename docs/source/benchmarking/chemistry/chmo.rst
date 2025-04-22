Chemical Methods Ontology (ChMO)
==========================

Overview
--------
The Chemical Methods Ontology contains more than 3000 classes and describes methods used to:
- collect data in chemical experiments, such as mass spectrometry and electron microscopy.
- prepare and separate material for further analysis, such as sample ionisation, chromatography, and electrophoresis
- synthesise materials, such as epitaxy and continuous vapour deposition It also describes the instruments used
    in these experiments, such as mass spectrometers and chromatography columns and their outputs.

:Domain: Chemistry
:Category: Chemistry
:Current Version: None
:Last Updated: 2022-04-19
:Creator: None
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `Chemical Methods Ontology (ChMO) Homepage <https://github.com/rsc-ontologies/rsc-cmo>`_

Graph Metrics
-------------
    - **Total Nodes**: 24075
    - **Total Edges**: 44651
    - **Root Nodes**: 3100
    - **Leaf Nodes**: 17250

Knowledge coverage
------------------
    - Classes: 3202
    - Individuals: 0
    - Properties: 27

Hierarchical metrics
--------------------
    - **Maximum Depth**: 7
    - **Minimum Depth**: 0
    - **Average Depth**: 1.49
    - **Depth Variance**: 0.63

Breadth metrics
------------------
    - **Maximum Breadth**: 13439
    - **Minimum Breadth**: 1
    - **Average Breadth**: 2993.88
    - **Breadth Variance**: 20855464.86

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 4268
    - **Non-taxonomic Relations**: 216
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import ChMO

    # Initialize and load ontology
    ontology = ChMO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
