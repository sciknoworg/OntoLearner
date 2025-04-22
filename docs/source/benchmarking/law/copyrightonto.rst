Copyright Ontology
==========================

Overview
--------
The Copyright Ontology tries to formalise the copyright domain as a way to facilitate
automated (or computer-supported) copyright management through the whole content value chain,
as it is shaped by copyright law. Therefore, it does not focus just on the last step,
end-users permissions to consume content, like many rights languages and ontologies do.

:Domain: Law
:Category: Legal Knowledge
:Current Version: None
:Last Updated: 2019-09
:Creator: Rhizomik
:License: Creative Commons 4.0
:Format: RDF
:Download: `Copyright Ontology Homepage <https://rhizomik.net/ontologies/copyrightonto/>`_

Graph Metrics
-------------
    - **Total Nodes**: 218
    - **Total Edges**: 470
    - **Root Nodes**: 6
    - **Leaf Nodes**: 75

Knowledge coverage
------------------
    - Classes: 38
    - Individuals: 7
    - Properties: 12

Hierarchical metrics
--------------------
    - **Maximum Depth**: 8
    - **Minimum Depth**: 0
    - **Average Depth**: 2.93
    - **Depth Variance**: 6.62

Breadth metrics
------------------
    - **Maximum Breadth**: 6
    - **Minimum Breadth**: 2
    - **Average Breadth**: 3.22
    - **Breadth Variance**: 2.40

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 7
    - **Taxonomic Relations**: 403
    - **Non-taxonomic Relations**: 7
    - **Average Terms per Type**: 2.33

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CopyrightOnto

    # Initialize and load ontology
    ontology = CopyrightOnto()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
