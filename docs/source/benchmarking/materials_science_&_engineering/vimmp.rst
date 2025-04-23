Virtual Materials Marketplace (VIMMP) Ontologies
==========================

Overview
--------
The Virtual Materials Marketplace (VIMMP) project is developing an open platform for providing
and accessing services related to materials modelling. Within VIMMP, a system of marketplace-level ontologies
is developed to characterize services, models, and interactions between users; the European Materials
and Modelling Ontology (EMMO, recently renamed while keeping the original acronym) is employed
as a top-level ontology. The ontologies are used to annotate data that are stored in the ZONTAL Space component
of VIMMP and to support the ingest and retrieval of data and metadata at the VIMMP marketplace front-end.

:Domain: Materials Science & Engineering
:Category: Materials Modeling
:Current Version: None
:Last Updated: 2021-01-02
:Creator: Ilian T. Todorov, Martin Thomas Horsch, Michael A. Seaton, Silvia Chiacchiera
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `Virtual Materials Marketplace (VIMMP) Ontologies Homepage <https://matportal.org/ontologies/VIMMP_ONTOLOGIES>`_

Graph Metrics
-------------
    - **Total Nodes**: 6149
    - **Total Edges**: 15298
    - **Root Nodes**: 841
    - **Leaf Nodes**: 1948

Knowledge coverage
------------------
    - Classes: 1234
    - Individuals: 911
    - Properties: 771

Hierarchical metrics
--------------------
    - **Maximum Depth**: 20
    - **Minimum Depth**: 0
    - **Average Depth**: 3.17
    - **Depth Variance**: 12.15

Breadth metrics
------------------
    - **Maximum Breadth**: 1383
    - **Minimum Breadth**: 3
    - **Average Breadth**: 263.38
    - **Breadth Variance**: 147256.81

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 1939
    - **Taxonomic Relations**: 4077
    - **Non-taxonomic Relations**: 404
    - **Average Terms per Type**: 34.02

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import VIMMP

    # Initialize and load ontology
    ontology = VIMMP()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
