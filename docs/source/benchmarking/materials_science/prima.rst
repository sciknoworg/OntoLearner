PRovenance Information in MAterials science (PRIMA)
===================

Overview
-----------------
An ontology that captures the provenance information in the materials science domain.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 2.0
:Last Updated: 2024-01-29
:Producer: Ahmad Zainul Ihsan, Mehrdad Jalali, Rossella Aversa
:License: Creative Commons Attribution 3.0 Unported (CC BY 3.0)
:Format: TTL, OWL
:Download: `PRIMA Homepage <https://materials-data-science-and-informatics.github.io/MDMC-NEP-top-level-ontology/PRIMA/complete/ver_2_0/index.html>`_
:Documentation: `PRIMA Documentation <https://github.com/Materials-Data-Science-and-Informatics/MDMC-NEP-top-level-ontology?tab=readme-ov-file>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 444
    - **Root Nodes**: 18
    - **Leaf Nodes**: 135
    - **Maximum Depth**: 14
    - **Edges**: 1073

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1117
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import PRIMA

    # Initialize and load ontology
    ontology = PRIMA()
    ontology.load("path/to/prima.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
