EMMO-based ontology for microstructures (MicroStructures)
========================================================================================================================

Overview
--------
This is intended to be a domain ontology for metallic microstructures, covering aspects like: composition,
particles, both stable (primary) and metastable (precipitates), grains, subgrains,
grain boundaries & particle free zones (PFZs), texture, dislocations. The aim is to support
both microstructure modelling as well as characterisation.

:Domain: Materials Science & Engineering
:Category: Microstructure
:Current Version: None
:Last Updated: None
:Creator: None
:License: None
:Format: OWL/XML
:Download: `EMMO-based ontology for microstructures (MicroStructures) Homepage <https://github.com/jesper-friis/emmo-microstructure>`_

Graph Metrics
-------------
    - **Total Nodes**: 115
    - **Total Edges**: 287
    - **Root Nodes**: 1
    - **Leaf Nodes**: 37

Knowledge coverage
------------------
    - Classes: 43
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.67
    - **Depth Variance**: 0.22

Breadth metrics
------------------
    - **Maximum Breadth**: 2
    - **Minimum Breadth**: 1
    - **Average Breadth**: 1.50
    - **Breadth Variance**: 0.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 364
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MicroStructures

    # Initialize and load ontology
    ontology = MicroStructures()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
