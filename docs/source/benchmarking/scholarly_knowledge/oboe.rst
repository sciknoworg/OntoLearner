Extensible Observation Ontology (OBOE)
==========================

Overview
--------
The Extensible Observation Ontology (OBOE) is a formal ontology for capturing the semantics
of scientific observation and measurement. The ontology supports researchers to add detailed semantic annotations
to scientific data, thereby clarifying the inherent meaning of scientific observations.

:Domain: Scholarly Knowledge
:Category: Scientific Observation
:Current Version: 1.2
:Last Updated: None
:Creator: The Regents of the University of California
:License: Creative Commons 3.0
:Format: OWL
:Download: `Extensible Observation Ontology (OBOE) Homepage <https://terminology.tib.eu/ts/ontologies/OBOE>`_

Graph Metrics
-------------
    - **Total Nodes**: 1868
    - **Total Edges**: 5017
    - **Root Nodes**: 169
    - **Leaf Nodes**: 156

Knowledge coverage
------------------
    - Classes: 478
    - Individuals: 0
    - Properties: 30

Hierarchical metrics
--------------------
    - **Maximum Depth**: 11
    - **Minimum Depth**: 0
    - **Average Depth**: 2.96
    - **Depth Variance**: 4.93

Breadth metrics
------------------
    - **Maximum Breadth**: 480
    - **Minimum Breadth**: 6
    - **Average Breadth**: 153.33
    - **Breadth Variance**: 18183.39

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 3244
    - **Non-taxonomic Relations**: 62
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OBOE

    # Initialize and load ontology
    ontology = OBOE()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
