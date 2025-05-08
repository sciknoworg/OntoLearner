Allotrope Foundation Ontology (AFO)
========================================================================================================================

Overview
--------
The AFO is an ontology suite that provides a standard vocabulary and semantic model
for the representation of laboratory analytical processes. The AFO suite is aligned at the upper layer
to the Basic Formal Ontology (BFO). The core domains modeled include, Equipment, Material, Process, and Results.
This artifact contains all triples of Allotrope Foundation Merged Without QUDT Ontology Suite (REC/2023/12)
together with triples inferred with HermiT.

:Domain: Chemistry
:Category: Laboratory Analytical Processes
:Current Version: 2024-06
:Last Updated: 2024-06-28
:Creator: Allotrope Foundation
:License: CC BY 4.0
:Format: TTL
:Download: `Allotrope Foundation Ontology (AFO) Homepage <https://terminology.tib.eu/ts/ontologies/AFO>`_

Graph Metrics
-------------
    - **Total Nodes**: 15547
    - **Total Edges**: 36699
    - **Root Nodes**: 142
    - **Leaf Nodes**: 8003

Knowledge coverage
------------------
    - Classes: 3871
    - Individuals: 38
    - Properties: 318

Hierarchical metrics
--------------------
    - **Maximum Depth**: 24
    - **Minimum Depth**: 0
    - **Average Depth**: 5.14
    - **Depth Variance**: 22.60

Breadth metrics
------------------
    - **Maximum Breadth**: 368
    - **Minimum Breadth**: 1
    - **Average Breadth**: 75.84
    - **Breadth Variance**: 8251.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 37
    - **Taxonomic Relations**: 6904
    - **Non-taxonomic Relations**: 34
    - **Average Terms per Type**: 3.36

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import AFO

    # Initialize and load ontology
    ontology = AFO()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
