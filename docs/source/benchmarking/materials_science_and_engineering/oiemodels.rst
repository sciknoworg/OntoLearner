Open Innovation Environment Models (OIEModels)
========================================================================================================================

Overview
--------
The models module defines models as semiotic signs that stands for an object by resembling or imitating it,
in shape or by sharing a similar logical structure.

:Domain: Materials Science and Engineering
:Category: Materials
:Current Version: None
:Last Updated: None
:Creator: Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Open Innovation Environment Models (OIEModels) Homepage <https://github.com/emmo-repo/OIE-Ontologies/>`_

Graph Metrics
-------------
    - **Total Nodes**: 186
    - **Total Edges**: 413
    - **Root Nodes**: 0
    - **Leaf Nodes**: 64

Knowledge coverage
------------------
    - Classes: 108
    - Individuals: 0
    - Properties: 1

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
    - **Term Types**: 0
    - **Taxonomic Relations**: 101
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OIEModels

    # Initialize and load ontology
    ontology = OIEModels()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
