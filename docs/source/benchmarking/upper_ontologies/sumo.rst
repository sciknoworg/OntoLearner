Suggested Upper Merged Ontology (SUMO)
======================================

Overview
-----------------
The Suggested Upper Merged Ontology (SUMO) and its domain ontologies form the largest formal public ontology
in existence today. They are being used for research and applications in search, linguistics and reasoning.
SUMO is the only formal ontology that has been mapped to all of the WordNet lexicon.

:Domain: Upper Ontology
:Category: Upper Ontology
:Current Version: 1.0
:Last Updated: 2025-02-17
:Producer:
:License: Creative Commons 4.0
:Format: OWL
:Download: `SUMO Homepage <https://www.ontologyportal.org/>`_
:Documentation: `SUMO Documentation <https://www.ontologyportal.org/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Nodes**: 288016
    - **Root Nodes**: 77015
    - **Leaf Nodes**: 197102
    - **Maximum Depth**: 27
    - **Edges**: 496645

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 80282
    - **Taxonomic Relations**: 7178
    - **Non-taxonomic Relations**: 311
    - **Average Terms per Type**: 1867.02

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import SUMO

   # Initialize and load ontology
   sumo = SUMO()
   sumo.load("path/to/sumo.owl")
   # Extract datasets
   data = sumo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
