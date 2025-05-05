Microscopy Ontology (MO)
========================================================================================================================

Overview
--------
The Microscopy Ontology (MO) extends the ontological framework of the PMDco. The MO facilitates semantic integration
and the interoperable connection of diverse data sources from the fields of microscopy and microanalysis. Consequently,
the MO paves the way for new, adaptable data applications and analyses across various experiments and studies

:Domain: Biology and Life Sciences
:Category: Microscopy
:Current Version: 2.0
:Last Updated: None
:Creator: https://orcid.org/0000-0002-3717-7104,https://orcid.org/0000-0002-7094-5371
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Microscopy Ontology (MO) Homepage <https://github.com/materialdigital/microscopy-ontology?tab=readme-ov-file>`_

Graph Metrics
-------------
    - **Total Nodes**: 4853
    - **Total Edges**: 9727
    - **Root Nodes**: 97
    - **Leaf Nodes**: 2884

Knowledge coverage
------------------
    - Classes: 1066
    - Individuals: 1
    - Properties: 70

Hierarchical metrics
--------------------
    - **Maximum Depth**: 23
    - **Minimum Depth**: 0
    - **Average Depth**: 4.20
    - **Depth Variance**: 13.95

Breadth metrics
------------------
    - **Maximum Breadth**: 178
    - **Minimum Breadth**: 1
    - **Average Breadth**: 41.33
    - **Breadth Variance**: 2660.81

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 953
    - **Non-taxonomic Relations**: 20
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MO

    # Initialize and load ontology
    ontology = MO()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
