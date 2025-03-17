DataCite Ontology (DataCite)
============================

Overview
-----------------
The DataCite Ontology (DataCite) is an ontology that enables the metadata properties
of the DataCite Metadata Schema Specification (i.e., a list of metadata properties
for the accurate and consistent identification of a resource for citation
and retrieval purposes) to be described in RDF.

:Domain: Metadata
:Category: Scholarly Knowledge
:Current Version: 3.1
:Last Updated: 15/09/2022
:Producer: David Shotton, Silvio Peroni
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `DataCite Homepage <https://schema.datacite.org/>`_
:Documentation: `DataCite Documentation <https://schema.datacite.org/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 260
    - **Root Nodes**: 14
    - **Leaf Nodes**: 120
    - **Maximum Depth**: 8
    - **Edges**: 519

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 71
    - **Taxonomic Relations**: 55
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 3.55

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import DataCite

   # Initialize and load ontology
   datacite = DataCite()
   datacite.load("path/to/ontology.owl")
   # Extract datasets
   data = datacite.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
