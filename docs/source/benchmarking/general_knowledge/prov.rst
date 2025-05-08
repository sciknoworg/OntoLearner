PROV Ontology (PROV-O)
========================================================================================================================

Overview
--------
The PROV Ontology (PROV-O) expresses the PROV Data Model [PROV-DM] using the OWL2 Web Ontology Language (OWL2) [OWL2-OVERVIEW].
It provides a set of classes, properties, and restrictions that can be used to represent
and interchange provenance information generated in different systems and under different contexts.
It can also be specialized to create new classes and properties to model provenance information
for different applications and domains. The PROV Document Overview describes the overall state of PROV,
and should be read before other PROV documents.

:Domain: General Knowledge
:Category: General
:Current Version: 2013-04-30
:Last Updated: 2013-04-30
:Creator: None
:License: W3C Software License
:Format: OWL
:Download: `PROV Ontology (PROV-O) Homepage <https://terminology.tib.eu/ts/ontologies/PROV>`_

Graph Metrics
-------------
    - **Total Nodes**: 417
    - **Total Edges**: 1100
    - **Root Nodes**: 26
    - **Leaf Nodes**: 248

Knowledge coverage
------------------
    - Classes: 39
    - Individuals: 0
    - Properties: 50

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 2.21
    - **Depth Variance**: 1.98

Breadth metrics
------------------
    - **Maximum Breadth**: 59
    - **Minimum Breadth**: 5
    - **Average Breadth**: 30.29
    - **Breadth Variance**: 409.63

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 39
    - **Non-taxonomic Relations**: 4
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PROV

    # Initialize and load ontology
    ontology = PROV()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
