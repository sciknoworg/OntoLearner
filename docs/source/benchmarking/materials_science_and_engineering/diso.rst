Dislocation Ontology (DISO)
========================================================================================================================

Overview
--------
DISO is an ontology that defines the linear defect, in particular dislocation concepts
and relations between them in crystalline materials.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 1.0
:Last Updated: 21.03.202
:Creator: Ahmad Zainul Ihsan
:License: Creative Commons Attribution 3.0 International (CC BY 3.0)
:Format: OWL/XML, RDF/XML, Turtle
:Download: `Dislocation Ontology (DISO) Homepage <https://github.com/Materials-Data-Science-and-Informatics/dislocation-ontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 324
    - **Total Edges**: 739
    - **Root Nodes**: 9
    - **Leaf Nodes**: 91

Knowledge coverage
------------------
    - Classes: 62
    - Individuals: 0
    - Properties: 45

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.18
    - **Depth Variance**: 0.15

Breadth metrics
------------------
    - **Maximum Breadth**: 9
    - **Minimum Breadth**: 2
    - **Average Breadth**: 5.50
    - **Breadth Variance**: 12.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 202
    - **Non-taxonomic Relations**: 6
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import DISO

    # Initialize and load ontology
    ontology = DISO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
