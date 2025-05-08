Conference Ontology (Conference)
========================================================================================================================

Overview
--------
The conference-ontology is a new self-contained ontology for modeling knowledge about conferences.
The conference-ontology adopts the best ontology design practices (e.g., Ontology Design Patterns,
ontology reuse and interlinking) and guarantees interoperability with SWC ontology
and all other pertinent vocabularies.

:Domain: Events
:Category: Conferences
:Current Version: None
:Last Updated: 2016/04/30
:Creator: Aldo Gangemi et al.
:License: Creative Commons 3.0
:Format: OWL
:Download: `Conference Ontology (Conference) Homepage <http://www.scholarlydata.org/ontology/conference-ontology.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 243
    - **Total Edges**: 652
    - **Root Nodes**: 8
    - **Leaf Nodes**: 61

Knowledge coverage
------------------
    - Classes: 42
    - Individuals: 32
    - Properties: 52

Hierarchical metrics
--------------------
    - **Maximum Depth**: 11
    - **Minimum Depth**: 0
    - **Average Depth**: 4.60
    - **Depth Variance**: 6.67

Breadth metrics
------------------
    - **Maximum Breadth**: 25
    - **Minimum Breadth**: 3
    - **Average Breadth**: 12.42
    - **Breadth Variance**: 49.74

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 32
    - **Taxonomic Relations**: 49
    - **Non-taxonomic Relations**: 3
    - **Average Terms per Type**: 10.67

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import ConferenceOntology

    # Initialize and load ontology
    ontology = ConferenceOntology()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
