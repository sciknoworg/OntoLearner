Additive Manufacturing Ontology (AMOntology)
========================================================================================================================

Overview
--------
The AM ontology has been developed following two major milestones. The ontology developed within the first milestone
includes AMProcessOntology, ModelOntology and AMOntology files. AMProcessOntology contains the set of entities
used to capture knowledge about additive manufacturing processes. ModelOntology contains the set of entities
used to capture knowledge about modeling concepts that represent (possibly) multi-physics multi-scale processes.
AMOntology uses AMProcessOntology and ModelOntology files to describe entities that capture knowledge
about characteristics of computational models for AM processes.

:Domain: Materials Science & Engineering
:Category: Manufacturing
:Current Version: 1.0
:Last Updated: 2023-05-10
:Creator: Iassou Souroko, Ali Riza Durmaz
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Additive Manufacturing Ontology (AMOntology) Homepage <https://github.com/iassouroko/AMontology>`_

Graph Metrics
-------------
    - **Total Nodes**: 900
    - **Total Edges**: 2299
    - **Root Nodes**: 71
    - **Leaf Nodes**: 99

Knowledge coverage
------------------
    - Classes: 328
    - Individuals: 56
    - Properties: 21

Hierarchical metrics
--------------------
    - **Maximum Depth**: 15
    - **Minimum Depth**: 0
    - **Average Depth**: 4.66
    - **Depth Variance**: 11.25

Breadth metrics
------------------
    - **Maximum Breadth**: 116
    - **Minimum Breadth**: 1
    - **Average Breadth**: 55.50
    - **Breadth Variance**: 1339.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 59
    - **Taxonomic Relations**: 1603
    - **Non-taxonomic Relations**: 5
    - **Average Terms per Type**: 1.26

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import AMOntology

    # Initialize and load ontology
    ontology = AMOntology()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
