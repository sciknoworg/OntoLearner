Basic Forml Ontology
====================

Overview
-----------------
The Basic Formal Ontology (BFO) is a small, upper-level ontology that describes
the basic types of entities in the world and how they relate to each other.

:Domain: Basic
:Category: Upper-Level Ontology
:Current Version: 2.0
:Last Updated: 2020
:Producer: University at Buffalo
:License: Creative Commons 4.0
:Format: OWL, TTL
:Download: `BFO Homepage <https://github.com/BFO-ontology/BFO-2020/>`_
:Documentation: `BFO Documentation <https://basic-formal-ontology.org/>`_

Base Metrics
---------------
    - Classes: 35
    - Individuals: 0
    - Properties: 22
    - Annotation Assertions: 0


Graph Metrics:
------------------
    - **Total Nodes**: 538
    - **Root Nodes**: 16
    - **Leaf Nodes**: 276
    - **Maximum Depth**:
    - **Edges**: 1002

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 162
    - **Non-taxonomic Relations**: 18
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BFO

   # Initialize and load ontology
   bfo = BFO()
   bfo.load("path/to/ontology.owl")
   # Extract datasets
   data = bfo.extract()
   # Access specific relations
   term_types = data.term_typings
