Line Defect Ontology (LDO)
==========================

Overview
-----------------
LDO is an ontology designed to describe line defects in crystalline materials, such as dislocations and disclinations.

:Domain: Materials Science and Engineering
:Category: Materials Defects
:Current Version: 1.0.0
:Last Updated:
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `LDO Homepage <https://github.com/OCDO/ldo>`_
:Documentation: `LDO Documentation <https://github.com/OCDO/ldo>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 111
    - **Root Nodes**: 6
    - **Leaf Nodes**: 49
    - **Maximum Depth**: 4
    - **Edges**: 207

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 21
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import LDO

    # Initialize and load ontology
    ontology = LDO()
    ontology.load("path/to/ldo.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
