The Conference Ontology
========================

Overview
-----------------
The conference-ontology is a new self-contained ontology for modeling knowledge about conferences.
The conference-ontology adopts the best ontology design practices (e.g., Ontology Design Patterns,
ontology reuse and interlinking) and guarantees interoperability with SWC ontology
and all other pertinent vocabularies.

:Domain: Events
:Category: Conferences
:Current Version:
:Last Updated: 2016/04/30
:Producer: Aldo Gangemi et al.
:License: Creative Commons 3.0
:Format: OWL
:Download: `Conference Ontology <http://www.scholarlydata.org/ontology/conference-ontology.owl>`_
:Documentation: `Conference Ontology Documentation <http://www.scholarlydata.org/ontology/doc/>`_

Base Metrics
---------------
    - Classes:
    - Object Properties:
    - Data Properties:
    - Annotation Assertions:
    - DL Expressivity:

Graph Metrics:
------------------
    - **Total Nodes**: 133
    - **Root Nodes**: 82
    - **Leaf Nodes**: 11
    - **Maximum Depth**: 3
    - **Edges**: 290
    - **Average Depth**: 2.00

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 32
    - **Taxonomic Relations**: 49
    - **Non-taxonomic Relations**: 3
    - **Average Terms per Type**: 2

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology.conference import ConferenceOntology

   # Initialize and load ontology
   conference = ConferenceOntology()
   conference.load("path/to/ontology.owl")
   data = conference.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
