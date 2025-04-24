Common Ontology (Common)
========================================================================================================================

Overview
--------
Ontology for the representation of commons elements in the Trias ontology

:Domain: Education
:Category: Computer Science
:Current Version: 0.1.0
:Last Updated: None
:Creator: Jhon Toledo, Miguel Angel García, Oscar Corcho
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: RDF/XML
:Download: `Common Ontology (Common) Homepage <https://w3id.org/mobility/trias/common/0.1.0>`_

Graph Metrics
-------------
    - **Total Nodes**: 67
    - **Total Edges**: 131
    - **Root Nodes**: 8
    - **Leaf Nodes**: 30

Knowledge coverage
------------------
    - Classes: 6
    - Individuals: 0
    - Properties: 15

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.27
    - **Depth Variance**: 0.20

Breadth metrics
------------------
    - **Maximum Breadth**: 8
    - **Minimum Breadth**: 3
    - **Average Breadth**: 5.50
    - **Breadth Variance**: 6.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 26
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import Common

    # Initialize and load ontology
    ontology = Common()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
