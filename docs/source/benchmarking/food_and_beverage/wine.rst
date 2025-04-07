Wine Ontology
===================

Overview
-----------------
A project to define an RDF style ontology for wines and the wine-industry

:Domain: Food and Beverage
:Category: wine
:Current Version:
:Last Updated:
:Creator:
:License:
:Format: RDF/XML
:Download: `Wine Ontology Homepage <https://github.com/UCDavisLibrary/wine-ontology>`_
:Documentation: `Wine Ontology Documentation <https://github.com/UCDavisLibrary/wine-ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 729
    - **Root Nodes**: 84
    - **Leaf Nodes**: 22
    - **Maximum Depth**: 42
    - **Edges**: 1816

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 161
    - **Taxonomic Relations**: 504
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 3.83

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import Wine

    # Initialize and load ontology
    ontology = Wine()
    ontology.load("path/to/wine.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
