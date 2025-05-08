Matolab Tensile Test Ontology (MOL_TENSILE)
========================================================================================================================

Overview
--------
An ontology for describing the tensile test process, made in the Materials Open Lab Project.

:Domain: Materials Science and Engineering
:Category: Materials Testings
:Current Version: 0.4
:Last Updated: 04/16/2021
:Creator: Markus Schilling, markus.schilling@bam.de; Philipp von Hartrott, philipp.von.hartrott@iwm.fraunhofer.de
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: RDF
:Download: `Matolab Tensile Test Ontology (MOL_TENSILE) Homepage <https://matportal.org/ontologies/MOL_TENSILE>`_

Graph Metrics
-------------
    - **Total Nodes**: 1970
    - **Total Edges**: 3602
    - **Root Nodes**: 132
    - **Leaf Nodes**: 1245

Knowledge coverage
------------------
    - Classes: 371
    - Individuals: 20
    - Properties: 95

Hierarchical metrics
--------------------
    - **Maximum Depth**: 90
    - **Minimum Depth**: 0
    - **Average Depth**: 16.30
    - **Depth Variance**: 665.10

Breadth metrics
------------------
    - **Maximum Breadth**: 285
    - **Minimum Breadth**: 2
    - **Average Breadth**: 11.49
    - **Breadth Variance**: 1763.74

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 20
    - **Taxonomic Relations**: 370
    - **Non-taxonomic Relations**: 20
    - **Average Terms per Type**: 6.67

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MOLTENSILE

    # Initialize and load ontology
    ontology = MOLTENSILE()
    ontology.load("path/to/ontology.RDF")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
