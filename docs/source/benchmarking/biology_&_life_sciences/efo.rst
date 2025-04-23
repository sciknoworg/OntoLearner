Experimental Factor Ontology (EFO)
==========================

Overview
--------
The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables
available in EBI databases, and for projects such as the GWAS catalog. It combines parts of several biological ontologies,
such as UBERON anatomy, ChEBI chemical compounds, and Cell Ontology. The scope of EFO is to support the annotation,
analysis and visualization of data handled by many groups at the EBI and as the core ontology for Open Targets.
EFO is developed by the EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT).

:Domain: Biology & Life Sciences
:Category: Biology
:Current Version: 3.75.0
:Last Updated: 2025-02-17
:Creator: None
:License: Apache 2.0
:Format: OWL, TTL, CSV, NT
:Download: `Experimental Factor Ontology (EFO) Homepage <https://www.ebi.ac.uk/efo>`_

Graph Metrics
-------------
    - **Total Nodes**: 948012
    - **Total Edges**: 2874304
    - **Root Nodes**: 308011
    - **Leaf Nodes**: 443836

Knowledge coverage
------------------
    - Classes: 88311
    - Individuals: 0
    - Properties: 87

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 1.24
    - **Depth Variance**: 2.14

Breadth metrics
------------------
    - **Maximum Breadth**: 308011
    - **Minimum Breadth**: 5
    - **Average Breadth**: 62043.14
    - **Breadth Variance**: 11287110481.98

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 280860
    - **Non-taxonomic Relations**: 15975
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import EFO

    # Initialize and load ontology
    ontology = EFO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
