DBpedia Ontology (DBpedia)
========================================================================================================================

Overview
--------
The DBpedia ontology is generated from the manually created specifications in the DBpedia Mappings Wiki.
Each release of this ontology corresponds to a new release of the DBpedia dataset, which contains
instance data extracted from various language versions of Wikipedia. The DBpedia ontology has evolved
into a crowd-sourced effort, resulting in a shallow cross-domain ontology.

:Domain: General Knowledge
:Category: Knowledge Graph
:Current Version: None
:Last Updated: 2008-11-17
:Creator: DBpedia Maintainers and Contributors
:License: Creative Commons 3.0
:Format: OWL
:Download: `DBpedia Ontology (DBpedia) Homepage <https://wiki.dbpedia.org/>`_

Graph Metrics
-------------
    - **Total Nodes**: 18819
    - **Total Edges**: 32745
    - **Root Nodes**: 16
    - **Leaf Nodes**: 14867

Knowledge coverage
------------------
    - Classes: 790
    - Individuals: 0
    - Properties: 3029

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 2.61
    - **Depth Variance**: 1.66

Breadth metrics
------------------
    - **Maximum Breadth**: 145
    - **Minimum Breadth**: 12
    - **Average Breadth**: 61.57
    - **Breadth Variance**: 2369.67

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 799
    - **Non-taxonomic Relations**: 2007
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import DBpedia

    # Initialize and load ontology
    ontology = DBpedia()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
