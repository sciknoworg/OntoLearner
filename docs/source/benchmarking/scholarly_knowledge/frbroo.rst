FRBRoo: Functional Requirements for Bibliographic Records
========================================================

Overview
-----------------
The FRBRoo ("FRBR-object oriented") initiative is a joint effort of the CIDOC Conceptual Reference Model
and Functional Requirements for Bibliographic Records international working groups to establish
a formal ontology intended to capture and represent the underlying semantics of bibliographic information
and to facilitate the integration, mediation, and interchange of bibliographic and museum information.

:Domain: Scholarly Knowledge
:Category: Bibliographic Records
:Current Version: 2.4
:Last Updated: November 2015
:Producer:
:License: Creative Commons 4.0
:Format: OWL, RDF
:Download: `FRBRoo Homepage <https://ontome.net/namespace/6#summary>`_
:Documentation: `FRBRoo Documentation <https://vocab.org/frbr/core>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 491
    - **Root Nodes**: 0
    - **Leaf Nodes**: 344
    - **Maximum Depth**: 0
    - **Edges**: 886

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 83
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import FRBRoo

   # Initialize and load ontology
   frbroo = FRBRoo()
   frbroo.load("path/to/ontology.owl")
   # Extract datasets
   data = frbroo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
