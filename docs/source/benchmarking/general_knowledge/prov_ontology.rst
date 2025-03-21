The PROV Ontology
=================

Overview
-----------------
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
:Producer:
:License: W3C Software License
:Format: OWL
:Download: `PROV Homepage <https://terminology.tib.eu/ts/ontologies/PROV>`_
:Documentation: `PROV Documentation <https://terminology.tib.eu/ts/ontologies/PROV>`_

Base Metrics
---------------
    - Classes: 31
    - Individuals: 72
    - Properties: 1

Graph Metrics:
------------------
    - **Nodes**: 417
    - **Root Nodes**: 26
    - **Leaf Nodes**: 248
    - **Maximum Depth**: 7
    - **Edges**: 1100

Dataset Statistics
------------------
Generated Benchmarks:
    * **Term Types**: 0
    * **Taxonomic Relations**: 41
    * **Non-taxonomic Relations**: 4
    * **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.prov import PROV

    # Initialize and load ontology
    prov = PROV()
    # Load ontology from file
    prov.load("path/to/ontology.owl")
    # Extract datasets
    data = prov.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
