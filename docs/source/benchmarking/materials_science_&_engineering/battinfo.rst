Battery Interface Ontology (BattINFO)
========================================================================================================================

Overview
--------
BattINFO is a foundational resource for harmonizing battery knowledge representation
and enhancing data interoperability. The primary objective is to provide the necessary tools
to create FAIR (Findable, Accessible, Interoperable, Reusable) battery data
that can be integrated into the Semantic Web.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: None
:Last Updated: None
:Creator: None
:License: None
:Format: TTL
:Download: `Battery Interface Ontology (BattINFO) Homepage <https://github.com/BIG-MAP/BattINFO>`_

Graph Metrics
-------------
    - **Total Nodes**: 27319
    - **Total Edges**: 50787
    - **Root Nodes**: 2855
    - **Leaf Nodes**: 16852

Knowledge coverage
------------------
    - Classes: 4431
    - Individuals: 7
    - Properties: 304

Hierarchical metrics
--------------------
    - **Maximum Depth**: 27
    - **Minimum Depth**: 0
    - **Average Depth**: 2.09
    - **Depth Variance**: 7.40

Breadth metrics
------------------
    - **Maximum Breadth**: 10695
    - **Minimum Breadth**: 7
    - **Average Breadth**: 827.86
    - **Breadth Variance**: 4644992.84

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 12
    - **Taxonomic Relations**: 23611
    - **Non-taxonomic Relations**: 66
    - **Average Terms per Type**: 6.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BattINFO

    # Initialize and load ontology
    ontology = BattINFO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
