System capabilities, operating ranges, and survival ranges ontology (SystemCapabilities)
========================================================================================================================

Overview
--------
This ontology describes system capabilities, operating ranges, and survival ranges.

:Domain: Materials Science and Engineering
:Category: Materials Science, Engineering, Systems
:Current Version: None
:Last Updated: 2017-05-14
:Creator: W3C/OGC Spatial Data on the Web Working Group
:License: W3C Software and Document License
:Format: OWL
:Download: `System capabilities, operating ranges, and survival ranges ontology (SystemCapabilities) Homepage <https://terminology.tib.eu/ts/ontologies/SSNSYSTEM>`_

Graph Metrics
-------------
    - **Total Nodes**: 137
    - **Total Edges**: 268
    - **Root Nodes**: 14
    - **Leaf Nodes**: 47

Knowledge coverage
------------------
    - Classes: 25
    - Individuals: 3
    - Properties: 8

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.22
    - **Depth Variance**: 0.17

Breadth metrics
------------------
    - **Maximum Breadth**: 14
    - **Minimum Breadth**: 4
    - **Average Breadth**: 9.00
    - **Breadth Variance**: 25.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 45
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SystemCapabilities

    # Initialize and load ontology
    ontology = SystemCapabilities()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
