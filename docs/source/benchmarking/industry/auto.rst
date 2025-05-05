Automotive Ontology (AUTO)
========================================================================================================================

Overview
--------
The AUTOMOTIVE ONTOLOGY (AUTO) defines the shared conceptual structures
in the automotive industry. It is an OWL ontology. It is built upon the auto schema.org
extension created by the W3C Automotive Ontology Community Group. AUTO's development process
follows the best practices established by the EDMC FIBO Community.

:Domain: Industry
:Category: Automotive
:Current Version: None
:Last Updated: 2021-03-01
:Creator: EDM Council
:License: MIT
:Format: RDF
:Download: `Automotive Ontology (AUTO) Homepage <https://github.com/edmcouncil/auto/tree/master>`_

Graph Metrics
-------------
    - **Total Nodes**: 6344
    - **Total Edges**: 17693
    - **Root Nodes**: 417
    - **Leaf Nodes**: 2589

Knowledge coverage
------------------
    - Classes: 1372
    - Individuals: 58
    - Properties: 336

Hierarchical metrics
--------------------
    - **Maximum Depth**: 25
    - **Minimum Depth**: 0
    - **Average Depth**: 4.72
    - **Depth Variance**: 17.16

Breadth metrics
------------------
    - **Maximum Breadth**: 574
    - **Minimum Breadth**: 1
    - **Average Breadth**: 116.38
    - **Breadth Variance**: 20295.70

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 58
    - **Taxonomic Relations**: 2731
    - **Non-taxonomic Relations**: 42
    - **Average Terms per Type**: 3.62

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import AUTO

    # Initialize and load ontology
    ontology = AUTO()
    ontology.load("path/to/ontology.RDF")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
