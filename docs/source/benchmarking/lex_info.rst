LexInfo
========

Overview
-----------------
LexInfo allows us to associate linguistic information to elements in an ontology with respect
to any level of linguistic description and expressivity. LexInfo has been implemented as an OWL ontology
and is available together with an API.

:Domain: Linguistics
:Category: Scholarly Knowledge
:Current Version: 3.0
:Last Updated:
:Producer:
:License: Apache 2.0
:Format: RDF
:Download: `LexInfo Homepage <https://lexinfo.net/index.html>`_
:Documentation: `LexInfo Documentation <https://lexinfo.net/index.html>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 3351
    - **Root Nodes**: 1
    - **Leaf Nodes**: 2308
    - **Maximum Depth**: 1
    - **Edges**: 5435

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 288
    - **Taxonomic Relations**: 282
    - **Non-taxonomic Relations**: 75
    - **Average Terms per Type**: 11.52

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import LexInfo

   # Initialize and load ontology
   lexinfo = LexInfo()
   lexinfo.load("path/to/ontology.owl")
   # Extract datasets
   data = lexinfo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
