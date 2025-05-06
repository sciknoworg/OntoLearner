Human Disease Ontology (DOID)
========================================================================================================================

Overview
--------
The Disease Ontology has been developed as a standardized ontology for human disease
with the purpose of providing the biomedical community with consistent,
reusable and sustainable descriptions of human disease terms,
phenotype characteristics and related medical vocabulary disease concepts.

:Domain: Medicine
:Category: Human Diseases
:Current Version: None
:Last Updated: 2024-12-18
:Creator: The Open Biological and Biomedical Ontology Foundry
:License: Creative Commons 1.0
:Format: OWL
:Download: `Human Disease Ontology (DOID) Homepage <http://purl.obolibrary.org/obo/doid/releases/2024-12-18/doid.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 136876
    - **Total Edges**: 288142
    - **Root Nodes**: 14035
    - **Leaf Nodes**: 95185

Knowledge coverage
------------------
    - Classes: 15343
    - Individuals: 0
    - Properties: 2

Hierarchical metrics
--------------------
    - **Maximum Depth**: 26
    - **Minimum Depth**: 0
    - **Average Depth**: 1.59
    - **Depth Variance**: 1.07

Breadth metrics
------------------
    - **Maximum Breadth**: 61852
    - **Minimum Breadth**: 1
    - **Average Breadth**: 4291.67
    - **Breadth Variance**: 172233228.89

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 41569
    - **Non-taxonomic Relations**: 25
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import DOID

    # Initialize and load ontology
    ontology = DOID()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
