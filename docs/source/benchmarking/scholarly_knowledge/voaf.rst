Vocabulary of a Friend (VOAF)
========================================================================================================================

Overview
--------
The Vocabulary of a Friend (VOAF) is a vocabulary specification providing elements allowing the description
of vocabularies (RDFS vocabularies or OWL ontologies). It is based on Dublin Core and VOID.

:Domain: Scholarly Knowledge
:Category: Social Network
:Current Version: 2.3
:Last Updated: 2013-05-24
:Creator: Bernard Vatant
:License: Creative Commons 3.0
:Format: RDF/XML
:Download: `Vocabulary of a Friend (VOAF) Homepage <https://lov.linkeddata.es/vocommons/voaf/v2.3/>`_

Graph Metrics
-------------
    - **Total Nodes**: 175
    - **Total Edges**: 304
    - **Root Nodes**: 0
    - **Leaf Nodes**: 129

Knowledge coverage
------------------
    - Classes: 3
    - Individuals: 1
    - Properties: 21

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
    - **Term Types**: 1
    - **Taxonomic Relations**: 4
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 1.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import VOAF

    # Initialize and load ontology
    ontology = VOAF()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
