Computer Science Ontology (CSO)
========================================================================================================================

Overview
--------
The Computer Science Ontology (CSO) is a large-scale ontology of research areas in computer science.
It provides a comprehensive vocabulary of research topics in computing, organized in a hierarchical structure.

This class processes the Computer Science Ontology (CSO) with custom hooks for:
- Topic-based class detection
- superTopicOf relationships
- contributesTo relationships

:Domain: Scholarly Knowledge
:Category: Computer Science
:Current Version: 3.4
:Last Updated: None
:Creator: Knowledge Media Institute, Open University
:License: Creative Commons 4.0
:Format: OWL
:Download: `Computer Science Ontology (CSO) Homepage <https://cso.kmi.open.ac.uk/home>`_

Graph Metrics
-------------
    - **Total Nodes**: 25897
    - **Total Edges**: 152243
    - **Root Nodes**: 94
    - **Leaf Nodes**: 11199

Knowledge coverage
------------------
    - Classes: 0
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
    - **Maximum Breadth**: 187
    - **Minimum Breadth**: 94
    - **Average Breadth**: 140.50
    - **Breadth Variance**: 2162.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 44204
    - **Non-taxonomic Relations**: 49080
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CSO

    # Initialize and load ontology
    ontology = CSO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
