EUropean Research Information Ontology (EURIO)
=============================================
EURIO (EUropean Research Information Ontology) conceptualises, formally encodes and makes available in an open,
structured and machine-readable format data about resarch projects funded by the EU's
framework programmes for research and innovation.

:Domain: Scholarly Knowledge
:Category: Scholarly Knowledge
:Current Version: 2.4
:Last Updated: 2023-10-19
:Producer: Publications Office of the European Commission
:License: Creative Commons 4.0
:Format: RDF, TTL
:Download: `EURIO Homepage <https://op.europa.eu/de/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurio>`_
:Documentation: `EURIO Documentation <https://op.europa.eu/de/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurio>`_

Base Metrics
------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0
    - Annotation Assertions: 0

Schema Metrics
--------------
    - Attribute Richness: 0
    - Inheritance Richness: 0
    - Relationship Richness: 0

Graph Metrics:
--------------
    - **Total Nodes**: 502
    - **Root Nodes**: 18
    - **Leaf Nodes**: 204
    - **Edges**: 1193

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 700
    - **Non-taxonomic Relations**: 4
    - **Average Terms per Type**: 0

Usage Example
-------------
.. code-block:: python

   from ontolearner.ontology import EURIO

   # Initialize and load ontology
   eurio = EURIO()
   eurio.load("path/to/ontology.rdf")
   # Extract datasets
   data = eurio.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
