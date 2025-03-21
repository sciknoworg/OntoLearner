AGROVOC Multilingual Thesaurus
==============================

Overview
-----------------
AGROVOC is a relevant Linked Open Data set about agriculture available for public use and facilitates
access and visibility of data across domains and languages. It offers a structured collection of agricultural concepts,
terms, definitions and relationships which are used to unambiguously identify resources, allowing standardized
indexing processes and making searches more efficient.

:Domain: Agriculture
:Category: Scholarly Knowledge
:Current Version: 2024-04
:Last Updated: August 12, 2024
:Producer: Food and Agriculture Organization of the United Nations
:License: Creative Commons 4.0
:Format: RDF, SKOS
:Download: `AGROVOC Homepage <https://agroportal.lirmm.fr/ontologies/AGROVOC>`_
:Documentation: `AGROVOC Documentation <https://agroportal.lirmm.fr/ontologies/AGROVOC>`_

Base Metrics
---------------
    - Classes: 34
    - Individuals: 1281468
    - Properties: 209

Graph Metrics:
------------------
    - **Total Nodes**: 2279766
    - **Root Nodes**: 59
    - **Leaf Nodes**: 981249
    - **Maximum Depth**: 12
    - **Edges**: 10,140,352

Dataset Statistics
--------------------
Generated Benchmarks:
    - **Term Types**: 1234769
    - **Taxonomic Relations**: 13
    - **Non-taxonomic Relations**: 7
    - **Average Terms per Type**: 47491

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import AGROVOC

   # Initialize and load ontology
   agrovoc = AGROVOC()
   agrovoc.load("path/to/ontology.rdf")
   # Extract datasets
   data = agrovoc.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
