The Elementary Multiperspective Material Ontology (EMMO)
========================================================================================================================

Overview
--------
The Elementary Multiperspective Material Ontology (EMMO) is the result of a multidisciplinary effort within the EMMC,
aimed at the development of a standard representational ontology framework based on current materials modelling
and characterization knowledge. Instead of starting from general upper level concepts, as done by other ontologies,
the EMMO development started from the very bottom level, using the actual picture of the physical world coming
from applied sciences, and in particular from physics and material sciences.

:Domain: Materials Science and Engineering
:Category: Materials Modelling
:Current Version: 1.0.0-rc3
:Last Updated: 2024-03
:Creator: European Materials Modelling Council (EMMC)
:License: Creative Commons 4.0
:Format: OWL
:Download: `The Elementary Multiperspective Material Ontology (EMMO) Homepage <https://emmo-repo.github.io/>`_

Graph Metrics
-------------
    - **Total Nodes**: 13613
    - **Total Edges**: 30349
    - **Root Nodes**: 281
    - **Leaf Nodes**: 7742

Knowledge coverage
------------------
    - Classes: 2448
    - Individuals: 2
    - Properties: 181

Hierarchical metrics
--------------------
    - **Maximum Depth**: 41
    - **Minimum Depth**: 0
    - **Average Depth**: 8.16
    - **Depth Variance**: 107.87

Breadth metrics
------------------
    - **Maximum Breadth**: 552
    - **Minimum Breadth**: 1
    - **Average Breadth**: 67.24
    - **Breadth Variance**: 14619.32

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 2
    - **Taxonomic Relations**: 16281
    - **Non-taxonomic Relations**: 52
    - **Average Terms per Type**: 2.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import EMMO

    # Initialize and load ontology
    ontology = EMMO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
