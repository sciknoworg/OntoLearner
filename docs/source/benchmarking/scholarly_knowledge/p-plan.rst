Ontology for Provenance and Plans (P-Plan)
===========================================

Overview
-----------------
The Ontology for Provenance and Plans (P-Plan) is an extension of the PROV-O ontology [PROV-O]
created to represent the plans that guided the execution of scientific processes. P-Plan describes
how the plans are composed and their correspondence to provenance records that describe the execution itself.

:Domain: Scholarly Knowledge
:Category: Scholarly Knowledge
:Current Version: 1.3
:Last Updated: 2014-03-12
:Creator: http://www.isi.edu/~gil/
:License: `Creative Commons 4.0 <https://creativecommons.org/licenses/by/4.0/>`_
:Format: OWL
:Download: `P-Plan Homepage <https://vocab.linkeddata.es/p-plan/index.html>`_
:Documentation: `P-Plan Documentation <https://vocab.linkeddata.es/p-plan/index.html>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 52
    - **Root Nodes**: 10
    - **Leaf Nodes**: 24
    - **Maximum Depth**: 1
    - **Edges**: 100

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 16
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import P-Plan

    # Initialize and load ontology
    ontology = P-Plan()
    ontology.load("path/to/p-plan.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
