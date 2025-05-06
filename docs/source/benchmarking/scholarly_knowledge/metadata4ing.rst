Metadata for Intelligent Engineering (Metadata4Ing)
========================================================================================================================

Overview
--------
The ontology Metadata4Ing provides a framework for the semantic description of research data
and of the whole data generation process, embracing the object of investigation,
all sample and data manipulation methods and tools, the data files themselves,
and the roles of persons and institutions. The structure and application of the ontology
are based on the principles of modularity and inheritance.

:Domain: Scholarly Knowledge
:Category: Materials Science
:Current Version: 1.3.1
:Last Updated: 2025-03-10
:Creator: Metadata4Ing Workgroup
:License: Creative Commons 4.0
:Format: TTL
:Download: `Metadata for Intelligent Engineering (Metadata4Ing) Homepage <https://git.rwth-aachen.de/nfdi4ing/metadata4ing/metadata4ing>`_

Graph Metrics
-------------
    - **Total Nodes**: 1032
    - **Total Edges**: 1517
    - **Root Nodes**: 109
    - **Leaf Nodes**: 731

Knowledge coverage
------------------
    - Classes: 48
    - Individuals: 47
    - Properties: 100

Hierarchical metrics
--------------------
    - **Maximum Depth**: 7
    - **Minimum Depth**: 0
    - **Average Depth**: 1.54
    - **Depth Variance**: 1.36

Breadth metrics
------------------
    - **Maximum Breadth**: 413
    - **Minimum Breadth**: 4
    - **Average Breadth**: 109.75
    - **Breadth Variance**: 18099.19

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 37
    - **Taxonomic Relations**: 44
    - **Non-taxonomic Relations**: 6
    - **Average Terms per Type**: 9.25

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import Metadata4Ing

    # Initialize and load ontology
    ontology = Metadata4Ing()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
