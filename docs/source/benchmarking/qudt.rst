Quantities, Units, Dimensions and Data Types (QUDT)
=====================================================

Overview
-----------------
QUDT.org exists to make the QUDT Ontologies, derived models and vocabularies available to the public.
Originally, QUDT models were developed for the NASA Exploration Initiatives Ontology Models (NExIOM) project,
a Constellation Program initiative at the AMES Research Center (ARC).

:Domain: Physics
:Category: Materials Science and Engineering
:Current Version: 2.1
:Last Updated: March 1, 2022
:Producer: NASA Ames Research Center
:License: Creative Commons 4.0
:Format: TTL
:Download: `QUDT Homepage <https://qudt.org/>`_
:Documentation: `QUDT Documentation <https://qudt.org/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 772
    - **Root Nodes**: 0
    - **Leaf Nodes**: 233
    - **Maximum Depth**: 0
    - **Edges**: 2,288

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 27
    - **Taxonomic Relations**: 3,252
    - **Non-taxonomic Relations**: 12
    - **Average Terms per Type**: 0.96

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import QUDT

   # Initialize and load ontology
   qudt = QUDT()
   qudt.load("path/to/ontology.ttl")
   # Extract datasets
   data = qudt.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
