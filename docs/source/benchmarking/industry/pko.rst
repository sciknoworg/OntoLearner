Provenance Knowledge Ontology (PKO)
========================================================================================================================

Overview
--------
Procedural Knowledge (PK) is knowing how to perform some tasks,
as opposed to descriptive/declarative knowledge, which is knowing
what in terms of facts and notions. In industry, PK refers in general
to structured processes to be followed, and can be related
to both production (e.g., procedure on the production line in a plant)
and services (e.g., procedure for troubleshooting during customer support);
to specific technical expertise (e.g., procedure to set up a specific machine)
and general regulations and best practices (e.g., safety procedures,
activities to minimise environmental impact).

:Domain: Industry
:Category: Provenance
:Current Version: 1.0.0
:Last Updated: 2025-03-01
:Creator: Mario Scrocca (Cefriel), Valentina Carriero (Cefriel)
:License: Creative Commons 4.0
:Format: RDF
:Download: `Provenance Knowledge Ontology (PKO) Homepage <https://github.com/perks-project/pk-ontology/tree/master>`_

Graph Metrics
-------------
    - **Total Nodes**: 302
    - **Total Edges**: 623
    - **Root Nodes**: 24
    - **Leaf Nodes**: 141

Knowledge coverage
------------------
    - Classes: 38
    - Individuals: 8
    - Properties: 93

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.50
    - **Depth Variance**: 0.51

Breadth metrics
------------------
    - **Maximum Breadth**: 24
    - **Minimum Breadth**: 5
    - **Average Breadth**: 12.67
    - **Breadth Variance**: 66.89

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 8
    - **Taxonomic Relations**: 11
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 4.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PKO

    # Initialize and load ontology from local file
    ontology = PKO()
    ontology.load("path/to/ontology.RDF")

    # Or load from a Hugging Face repository
    ontology = PKO()
    ontology.load()

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
