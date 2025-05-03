NanoParticle Ontology (NPO)
========================================================================================================================

Overview
--------
NanoParticle Ontology (NPO) is developed within the framework of the Basic Formal Ontology (BFO),
and implemented in the Ontology Web Language (OWL) using well-defined ontology design principles.
The NPO was developed to represent knowledge underlying the preparation, chemical composition,
and characterization of nanomaterials involved in cancer research. Public releases of the NPO
are available through BioPortal website, maintained by the National Center for Biomedical Ontology.
Mechanisms for editorial and governance processes are being developed for the maintenance,
review, and growth of the NPO.

:Domain: Biology & Life Sciences
:Category: Materials Science
:Current Version: 2013-05-31
:Last Updated: 2013-05-31
:Creator: Dennis G. Thomas
:License: BSD-3-Clause license
:Format: OWL
:Download: `NanoParticle Ontology (NPO) Homepage <https://github.com/sobolevnrm/npo?tab=readme-ov-file>`_

Graph Metrics
-------------
    - **Total Nodes**: 9976
    - **Total Edges**: 36031
    - **Root Nodes**: 11
    - **Leaf Nodes**: 4344

Knowledge coverage
------------------
    - Classes: 2464
    - Individuals: 0
    - Properties: 87

Hierarchical metrics
--------------------
    - **Maximum Depth**: 10
    - **Minimum Depth**: 0
    - **Average Depth**: 4.26
    - **Depth Variance**: 7.37

Breadth metrics
------------------
    - **Maximum Breadth**: 35
    - **Minimum Breadth**: 7
    - **Average Breadth**: 21.82
    - **Breadth Variance**: 106.88

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 6895
    - **Non-taxonomic Relations**: 12277
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import NPO

    # Initialize and load ontology
    ontology = NPO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
