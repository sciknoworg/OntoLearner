Crystallography Ontology (EMMOCrystallography)
===============================================

Overview
-----------------
A crystallography domain ontology based on EMMO and the CIF core dictionary. It is implemented as a formal language.

:Domain: Materials Science and Engineering
:Category: Crystallography
:Current Version: 0.0.1
:Last Updated:
:Producer:
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: Turtle
:Download: `Crystallography Homepage <https://github.com/emmo-repo/domain-crystallography>`_
:Documentation: `Crystallography Documentation <https://github.com/emmo-repo/domain-crystallography>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 337
    - **Root Nodes**: 29
    - **Leaf Nodes**: 166
    - **Maximum Depth**: 14
    - **Edges**: 586

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 331
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import EMMOCrystallography

    # Initialize and load ontology
    ontology = EMMOCrystallography()
    ontology.load("path/to/crystallography.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
