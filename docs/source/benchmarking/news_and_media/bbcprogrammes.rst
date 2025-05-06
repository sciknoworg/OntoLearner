BBC Programmes Ontology (BBCProgrammes)
========================================================================================================================

Overview
--------
This ontology aims at providing a simple vocabulary for describing programmes.
It covers brands, series (seasons), episodes, broadcast events, broadcast services,etc.
Its development was funded by the BBC, and is heavily grounded on previous programmes data modelling work done there.

:Domain: News and Media
:Category: Programmes
:Current Version: 1.1
:Last Updated: 2009/02/20
:Creator: https://moustaki.org/foaf.rdf#moustaki
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Programmes Ontology (BBCProgrammes) Homepage <https://www.bbc.co.uk/ontologies/programmes-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 218
    - **Total Edges**: 620
    - **Root Nodes**: 2
    - **Leaf Nodes**: 129

Knowledge coverage
------------------
    - Classes: 40
    - Individuals: 0
    - Properties: 48

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 1.57
    - **Depth Variance**: 0.39

Breadth metrics
------------------
    - **Maximum Breadth**: 18
    - **Minimum Breadth**: 2
    - **Average Breadth**: 9.33
    - **Breadth Variance**: 43.56

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 40
    - **Non-taxonomic Relations**: 19
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BBCProgrammes

    # Initialize and load ontology
    ontology = BBCProgrammes()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
