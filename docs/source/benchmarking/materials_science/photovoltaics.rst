EMMO Domain Ontology for Photovoltaics (Photovoltaics)
======================================================

Overview
-----------------
This ontology is describing Perovskite solar cells.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 0.0.1
:Last Updated:
:Creator: Casper Welzel Andersen, Simon Clark
:License: Creative Commons license Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Photovoltaics Homepage <https://github.com/emmo-repo/domain-photovoltaics>`_
:Documentation: `Photovoltaics Documentation <https://github.com/emmo-repo/domain-photovoltaics>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 131
    - **Root Nodes**: 12
    - **Leaf Nodes**: 48
    - **Maximum Depth**: 1
    - **Edges**: 281

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 140
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import Photovoltaics

    # Initialize and load ontology
    ontology = Photovoltaics()
    ontology.load("path/to/photovoltaics.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
