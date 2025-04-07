Microscopy Ontology (MO)
=========================

Overview
-----------------
The Microscopy Ontology (MO) extends the ontological framework of the PMDco. The MO facilitates semantic integration
and the interoperable connection of diverse data sources from the fields of microscopy and microanalysis. Consequently,
the MO paves the way for new, adaptable data applications and analyses across various experiments and studies

:Domain: Biology
:Category: Microscopy
:Current Version: 2.0
:Last Updated:
:Producer: https://orcid.org/0000-0002-3717-7104,https://orcid.org/0000-0002-7094-5371
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: Turtle
:Download: `Microscopy Ontology Homepage <https://github.com/materialdigital/microscopy-ontology?tab=readme-ov-file>`_
:Documentation: `Microscopy Ontology Documentation <hhttps://github.com/materialdigital/microscopy-ontology?tab=readme-ov-file>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 4853
    - **Root Nodes**: 97
    - **Leaf Nodes**: 2884
    - **Maximum Depth**: 24
    - **Edges**: 9727

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 1181
    - **Non-taxonomic Relations**: 114
    - **Average Terms per Type**: 0.06

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import Microscopy

    # Initialize and load ontology
    ontology = Microscopy()
    ontology.load("path/to/pmd_mo.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
