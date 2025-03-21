Document Components Ontology (DoCO)
===================================

Overview
-----------------
DoCO, the Document Components Ontology, is an OWL 2 DL ontology that provides a general-purpose structured vocabulary
of document elements. DoCO has been designed as a general unifying ontological framework for describing different aspects
related to the content of scientific and other scholarly texts. Its primary goal has been to improve the interoperability
and shareability of academic documents (and related services) when multiple formats are actually used for their storage.

:Domain: Scholarly Communication
:Category: Education
:Current Version: 1.3
:Last Updated: 2015-07-03
:Producer: David Shotton and Silvio Peroni
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `DoCO Homepage <http://www.sparontologies.net/ontologies/doco>`_
:Documentation: `DoCO Documentation <https://sparontologies.github.io/doco/current/doco.html>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 442
    - **Root Nodes**: 12
    - **Leaf Nodes**: 73
    - **Maximum Depth**: 27
    - **Edges**: 922

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 156
    - **Non-taxonomic Relations**: 13
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import DoCO

   # Initialize and load ontology
   doco = DoCO()
   doco.load("path/to/ontology.rdf")
   # Extract datasets
   data = doco.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
