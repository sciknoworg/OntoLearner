Physico-chemical process ontology (REX)
========================================================================================================================

Overview
--------
REX is an ontology of physico-chemical processes, i.e. physico-chemical changes occurring in course of time.
REX includes both microscopic processes (involving molecular entities or subatomic particles) and macroscopic processes.
Some biochemical processes from Gene Ontology (GO Biological process) can be described as instances of REX.

:Domain: Chemistry
:Category: Chemistry
:Current Version: 1.0
:Last Updated: 2025-03-11
:Creator: University of Warsaw
:License: Creative Commons 4.0
:Format: OWL, RDF
:Download: `Physico-chemical process ontology (REX) Homepage <https://terminology.tib.eu/ts/ontologies/REX>`_

Graph Metrics
-------------
    - **Total Nodes**: 2461
    - **Total Edges**: 5630
    - **Root Nodes**: 356
    - **Leaf Nodes**: 1457

Knowledge coverage
------------------
    - Classes: 552
    - Individuals: 0
    - Properties: 6

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 1.35
    - **Depth Variance**: 0.97

Breadth metrics
------------------
    - **Maximum Breadth**: 978
    - **Minimum Breadth**: 5
    - **Average Breadth**: 304.57
    - **Breadth Variance**: 116930.53

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1126
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import REX

    # Initialize and load ontology
    ontology = REX()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
