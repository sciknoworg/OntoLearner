MatoLab Brinell Test Ontology (MOL_BRINELL)
========================================================================================================================

Overview
--------
An ontology for describing the Brinell hardness testing process, made in the Materials Open Lab Project.

:Domain: Materials Science & Engineering
:Category: Materials Testing
:Current Version: 0.1
:Last Updated: 05/05/2022
:Creator: Birgit Skrotzki, Hossein Beygi Nasrabadi, Philipp von Hartrott, Vinicius Carrillo Beber, Yue Chen
:License: None
:Format: TTL, RDF/XML, OWL
:Download: `MatoLab Brinell Test Ontology (MOL_BRINELL) Homepage <https://matportal.org/ontologies/MOL_BRINELL>`_

Graph Metrics
-------------
    - **Total Nodes**: 3648
    - **Total Edges**: 16347
    - **Root Nodes**: 29
    - **Leaf Nodes**: 308

Knowledge coverage
------------------
    - Classes: 37
    - Individuals: 3053
    - Properties: 21

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.26
    - **Depth Variance**: 0.25

Breadth metrics
------------------
    - **Maximum Breadth**: 29
    - **Minimum Breadth**: 1
    - **Average Breadth**: 12.67
    - **Breadth Variance**: 141.56

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 3053
    - **Taxonomic Relations**: 14
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 105.28

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MOLBRINELL

    # Initialize and load ontology
    ontology = MOLBRINELL()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
