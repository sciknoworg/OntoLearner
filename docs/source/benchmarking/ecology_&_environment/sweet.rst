Semantic Web for Earth and Environment Technology Ontology (SWEET)
========================================================================================================================

Overview
--------
The Semantic Web for Earth and Environment Technology Ontology (SWEET) is an investigation in improving discovery
and use of Earth science data, through software understanding of the semantics of web resources.
SWEET is a collection of ontologies conceptualizing a knowledge space for Earth system science,
represented using the web ontology language (OWL). It includes both orthogonal concepts (space, time,
Earth realms, physical quantities, etc.) and integrative science knowledge concepts (phenomena, events, etc.).

:Domain: Ecology & Environment
:Category: Earth Science, Geoscience
:Current Version: 3.6.0
:Last Updated: July 14, 2022
:Creator: NASA, JPL, Caltech
:License: Creative Commons 4.0
:Format: OWL
:Download: `Semantic Web for Earth and Environment Technology Ontology (SWEET) Homepage <https://bioportal.bioontology.org/ontologies/SWEET>`_

Graph Metrics
-------------
    - **Total Nodes**: 26249
    - **Total Edges**: 64544
    - **Root Nodes**: 244
    - **Leaf Nodes**: 11866

Knowledge coverage
------------------
    - Classes: 10240
    - Individuals: 2351
    - Properties: 358

Hierarchical metrics
--------------------
    - **Maximum Depth**: 15
    - **Minimum Depth**: 0
    - **Average Depth**: 3.62
    - **Depth Variance**: 9.36

Breadth metrics
------------------
    - **Maximum Breadth**: 303
    - **Minimum Breadth**: 2
    - **Average Breadth**: 102.81
    - **Breadth Variance**: 8823.90

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 2439
    - **Taxonomic Relations**: 18839
    - **Non-taxonomic Relations**: 515
    - **Average Terms per Type**: 11.67

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SWEET

    # Initialize and load ontology
    ontology = SWEET()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
