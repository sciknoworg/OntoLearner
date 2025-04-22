Life Ontology (LifO)
==========================

Overview
--------
The Life Ontology (LifO) is an ontology of the life of organism. LifO represents the
life processes of organisms and related entities and relations. LifO is a general
purpose ontology that covers the common features associated with different
organisms such as unicellular prokaryotes (e.g., E. coli) and multicellular organisms (e.g., human).

:Domain: Biology & Life Sciences
:Category: General Purpose
:Current Version: 1.0.17
:Last Updated: March 11, 2018
:Creator: Yongqun "Oliver" He (YH)
:License: Creative Commons 4.0
:Format: OWL
:Download: `Life Ontology (LifO) Homepage <https://bioportal.bioontology.org/ontologies/LIFO>`_

Graph Metrics
-------------
    - **Total Nodes**: 2140
    - **Total Edges**: 4179
    - **Root Nodes**: 43
    - **Leaf Nodes**: 1522

Knowledge coverage
------------------
    - Classes: 239
    - Individuals: 9
    - Properties: 98

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 1.18
    - **Depth Variance**: 0.83

Breadth metrics
------------------
    - **Maximum Breadth**: 65
    - **Minimum Breadth**: 17
    - **Average Breadth**: 41.67
    - **Breadth Variance**: 384.89

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 9
    - **Taxonomic Relations**: 581
    - **Non-taxonomic Relations**: 15
    - **Average Terms per Type**: 0.69

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import LIFO

    # Initialize and load ontology
    ontology = LIFO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
