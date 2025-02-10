Metadata4Ing
=============

Overview
-----------------
An ontology for describing the generation of research data within a scientific activity.

:Domain: Engineering
:Category: Scholarly Knowledge
:Current Version: 1.3.0
:Last Updated: 2024-09-20
:Producer: Metadata4Ing Workgroup
:License: Creative Commons 4.0
:Format: OWL, TTL
:Download: `Metadata4Ing Homepage <https://nfdi4ing.pages.rwth-aachen.de/metadata4ing/metadata4ing/>`_
:Documentation: `Metadata4Ing Documentation <https://nfdi4ing.pages.rwth-aachen.de/metadata4ing/metadata4ing/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Schema Metrics
---------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics:
------------------
    - **Total Nodes**: 976
    - **Root Nodes**: 109
    - **Leaf Nodes**: 701
    - **Maximum Depth**:
    - **Edges**: 1431

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 21
    - **Taxonomic Relations**: 122
    - **Non-taxonomic Relations**: 6
    - **Average Terms per Type**: 5.25

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import Metadata4Ing

   # Initialize and load ontology
   m4i = Metadata4Ing()
   m4i.load("path/to/ontology.owl")
   # Extract datasets
   data = m4i.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.non_type_taxonomies
