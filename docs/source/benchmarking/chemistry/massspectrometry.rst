Mass Spectrometry Ontology (MassSpectrometry)
========================================================================================================================

Overview
--------
A structured controlled vocabulary for the annotation of experiments concerned with proteomics mass spectrometry.

:Domain: Chemistry
:Category: Mass Spectrometry, Proteomics
:Current Version: None
:Last Updated: 12:02:2025
:Creator: Andreas Bertsch
:License: Creative Commons 4.0
:Format: OWL
:Download: `Mass Spectrometry Ontology (MassSpectrometry) Homepage <https://terminology.tib.eu/ts/ontologies/MS>`_

Graph Metrics
-------------
    - **Total Nodes**: 17851
    - **Total Edges**: 51814
    - **Root Nodes**: 3786
    - **Leaf Nodes**: 7959

Knowledge coverage
------------------
    - Classes: 3636
    - Individuals: 0
    - Properties: 12

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 1.16
    - **Depth Variance**: 0.58

Breadth metrics
------------------
    - **Maximum Breadth**: 7345
    - **Minimum Breadth**: 2
    - **Average Breadth**: 2534.57
    - **Breadth Variance**: 9465403.67

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 7016
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MassSpectrometry

    # Initialize and load ontology
    ontology = MassSpectrometry()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
