Citation Typing Ontology (CiTO)
==============================

Overview
-----------------
The Citation Typing Ontology (CiTO) is an ontology that enables characterization of the nature or type of citations,
both factually and rhetorically.

:Domain: Scholarly Communication
:Category: Scholarly Knowledge
:Current Version: 2.8.1
:Last Updated: 2018-02-16
:Producer: Silvio Peroni, David Shotton
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `CiTO Homepage <https://github.com/SPAROntologies/cito/tree/master/docs/current>`_
:Documentation: `CiTO Documentation <https://sparontologies.github.io/cito/current/cito.html>`_

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
    - **Total Nodes**: 312
    - **Root Nodes**: 11
    - **Leaf Nodes**: 182
    - **Maximum Depth**: 1
    - **Edges**: 574

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 11
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import CiTO

   # Initialize and load ontology
   cito = CiTO()
   cito.load("path/to/ontology.owl")
   # Extract datasets
   data = cito.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
