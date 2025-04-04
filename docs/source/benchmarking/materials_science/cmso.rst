Computational Material Sample Ontology (CMSO)
===================

Overview
-----------------
CMSO is an ontology that aims to describe computational materials science samples (or structures),
including crystalline defects. Initially focusing on the description at the atomic scale.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 0.0.1
:Last Updated:
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `CMSO Homepage <https://github.com/OCDO/cmso/tree/main>`_
:Documentation: `CMSO Documentation <https://github.com/OCDO/cmso/tree/main>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 347
    - **Root Nodes**: 40
    - **Leaf Nodes**: 192
    - **Maximum Depth**: 2
    - **Edges**: 556

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 22
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import CMSO

    # Initialize and load ontology
    ontology = CMSO()
    ontology.load("path/to/cmso.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
