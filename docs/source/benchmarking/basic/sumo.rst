Suggested Upper Merged Ontology (SUMO)
======================================

Overview
-----------------
The Suggested Upper Merged Ontology (SUMO) and its domain ontologies form the largest formal public ontology
in existence today. They are being used for research and applications in search, linguistics and reasoning.
SUMO is the only formal ontology that has been mapped to all of the WordNet lexicon.

:Domain: General
:Category: General
:Current Version: 1.0
:Last Updated: 2025-02-17
:Producer:
:License: Creative Commons 4.0
:Format: KIF, OWL
:Download: `SUMO Homepage <https://www.ontologyportal.org/>`_
:Documentation: `SUMO Documentation <https://www.ontologyportal.org/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Nodes**:
    - **Root Nodes**:
    - **Leaf Nodes**:
    - **Maximum Depth**:
    - **Edges**:

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**:
    - **Taxonomic Relations**:
    - **Non-taxonomic Relations**:
    - **Average Terms per Type**:

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import SUMO

   # Initialize and load ontology
   sumo = SUMO()
   sumo.load("path/to/ontology.owl")
   # Extract datasets
   data = sumo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
