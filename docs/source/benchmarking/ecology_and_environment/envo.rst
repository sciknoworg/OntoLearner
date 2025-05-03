Environment Ontology (ENVO)
========================================================================================================================

Overview
--------
ENVO is an expressive, community ontology which helps humans, machines,
and semantic web applications understand environmental entities of all kinds,
from microscopic to intergalactic scales. As a FAIR-compliant resource, it promotes interoperability
through the concise, controlled description of all things environmental.

:Domain: Ecology & Environment
:Category: Environment, Ecosystems, Habitats
:Current Version: 2024-07-01
:Last Updated: 2024-07-01
:Creator: Pier Luigi Buttigieg (https://orcid.org/0000-0002-4366-3088)
:License: Creative Commons 1.0
:Format: OWL, OBO, JSON
:Download: `Environment Ontology (ENVO) Homepage <https://obofoundry.org/ontology/envo.html>`_

Graph Metrics
-------------
    - **Total Nodes**: 43986
    - **Total Edges**: 107616
    - **Root Nodes**: 4449
    - **Leaf Nodes**: 19297

Knowledge coverage
------------------
    - Classes: 9309
    - Individuals: 44
    - Properties: 208

Hierarchical metrics
--------------------
    - **Maximum Depth**: 28
    - **Minimum Depth**: 0
    - **Average Depth**: 2.69
    - **Depth Variance**: 9.89

Breadth metrics
------------------
    - **Maximum Breadth**: 8473
    - **Minimum Breadth**: 2
    - **Average Breadth**: 1056.21
    - **Breadth Variance**: 4840394.03

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 46
    - **Taxonomic Relations**: 28876
    - **Non-taxonomic Relations**: 148
    - **Average Terms per Type**: 5.75

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import ENVO

    # Initialize and load ontology
    ontology = ENVO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
