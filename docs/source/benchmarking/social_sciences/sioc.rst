Semantically-Interlinked Online Communities (SIOC)
========================================================================================================================

Overview
--------
The SIOC (Semantically-Interlinked Online Communities) Ontology is an ontology for describing the
information in online communities. This includes sites that support online discussions, blogging,
file sharing, photo sharing, social networking, etc.

:Domain: Social Sciences
:Category: Social Networks
:Current Version: 1.36
:Last Updated: 2018/02/28
:Creator: Data Science Institute, NUI Galway
:License: Creative Commons 3.0
:Format: RDF/XML
:Download: `Semantically-Interlinked Online Communities (SIOC) Homepage <http://rdfs.org/sioc/spec/>`_

Graph Metrics
-------------
    - **Total Nodes**: 230
    - **Total Edges**: 551
    - **Root Nodes**: 0
    - **Leaf Nodes**: 123

Knowledge coverage
------------------
    - Classes: 14
    - Individuals: 0
    - Properties: 91

Hierarchical metrics
--------------------
    - **Maximum Depth**: 0
    - **Minimum Depth**: 0
    - **Average Depth**: 0.00
    - **Depth Variance**: 0.00

Breadth metrics
------------------
    - **Maximum Breadth**: 0
    - **Minimum Breadth**: 0
    - **Average Breadth**: 0.00
    - **Breadth Variance**: 0.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 9
    - **Non-taxonomic Relations**: 31
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SIOC

    # Initialize and load ontology
    ontology = SIOC()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
