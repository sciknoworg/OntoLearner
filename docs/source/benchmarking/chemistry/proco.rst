PROcess Chemistry Ontology (PROCO)
==========================

Overview
--------
PROCO (PROcess Chemistry Ontology) is a formal ontology that aims to standardly represent entities
and relations among entities in the domain of process chemistry.

:Domain: Chemistry
:Category: Chemicals, Processes
:Current Version: 04-14-2022
:Last Updated: 04-14-2022
:Creator: Anna Dun, Wes A. Schafer, Yongqun "Oliver" He (YH), Zachary Dance
:License: Creative Commons 4.0
:Format: OWL
:Download: `PROcess Chemistry Ontology (PROCO) Homepage <https://github.com/proco-ontology/PROCO>`_

Graph Metrics
-------------
    - **Total Nodes**: 6258
    - **Total Edges**: 11796
    - **Root Nodes**: 89
    - **Leaf Nodes**: 4646

Knowledge coverage
------------------
    - Classes: 970
    - Individuals: 14
    - Properties: 61

Hierarchical metrics
--------------------
    - **Maximum Depth**: 15
    - **Minimum Depth**: 0
    - **Average Depth**: 3.35
    - **Depth Variance**: 8.54

Breadth metrics
------------------
    - **Maximum Breadth**: 228
    - **Minimum Breadth**: 1
    - **Average Breadth**: 60.19
    - **Breadth Variance**: 4521.40

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 14
    - **Taxonomic Relations**: 2975
    - **Non-taxonomic Relations**: 17
    - **Average Terms per Type**: 0.93

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PROCO

    # Initialize and load ontology
    ontology = PROCO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
