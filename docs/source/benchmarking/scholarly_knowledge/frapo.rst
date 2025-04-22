Funding, Research Administration and Projects Ontology (FRAPO)
==========================

Overview
--------
The Funding, Research Administration and Projects Ontology (FRAPO) is an ontology
for describing the administrative information of research projects, e.g., grant applications,
funding bodies, project partners, etc.

:Domain: Scholarly Knowledge
:Category: Administration
:Current Version: None
:Last Updated: None
:Creator: David Shotton
:License: Creative Commons 4.0
:Format: OWL, TTL, NT
:Download: `Funding, Research Administration and Projects Ontology (FRAPO) Homepage <http://www.sparontologies.net/ontologies/frapo>`_

Graph Metrics
-------------
    - **Total Nodes**: 539
    - **Total Edges**: 1076
    - **Root Nodes**: 18
    - **Leaf Nodes**: 274

Knowledge coverage
------------------
    - Classes: 97
    - Individuals: 25
    - Properties: 125

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 0.68
    - **Depth Variance**: 1.08

Breadth metrics
------------------
    - **Maximum Breadth**: 18
    - **Minimum Breadth**: 3
    - **Average Breadth**: 7.00
    - **Breadth Variance**: 40.50

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 25
    - **Taxonomic Relations**: 82
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 1.67

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import FRAPO

    # Initialize and load ontology
    ontology = FRAPO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
