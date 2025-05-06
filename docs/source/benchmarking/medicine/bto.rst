BRENDA Tissue Ontology (BTO)
========================================================================================================================

Overview
--------
A structured controlled vocabulary for the source of an enzyme comprising tissues,
cell lines, cell types and cell cultures.

:Domain: Medicine
:Category: Enzyme
:Current Version: 2021-10-26
:Last Updated: 2021-10-26
:Creator: None
:License: Creative Commons 4.0
:Format: OWL
:Download: `BRENDA Tissue Ontology (BTO) Homepage <https://terminology.tib.eu/ts/ontologies/BTO>`_

Graph Metrics
-------------
    - **Total Nodes**: 37130
    - **Total Edges**: 86188
    - **Root Nodes**: 5619
    - **Leaf Nodes**: 21886

Knowledge coverage
------------------
    - Classes: 6569
    - Individuals: 0
    - Properties: 10

Hierarchical metrics
--------------------
    - **Maximum Depth**: 7
    - **Minimum Depth**: 0
    - **Average Depth**: 1.37
    - **Depth Variance**: 0.68

Breadth metrics
------------------
    - **Maximum Breadth**: 16002
    - **Minimum Breadth**: 9
    - **Average Breadth**: 4411.62
    - **Breadth Variance**: 36150459.73

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 5888
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BTO

    # Initialize and load ontology
    ontology = BTO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
