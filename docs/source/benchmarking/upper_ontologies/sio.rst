Semanticscience Integrated Ontology (SIO)
=========================================

Overview
-----------------
The semanticscience integrated ontology (SIO) provides a simple, integrated upper level ontology (types, relations)
for consistent knowledge representation across physical, processual and informational entities.
This project provides foundational support for the Bio2RDF (http://bio2rdf.org) and SADI (http://sadiframework.org) projects.

:Domain: Upper Ontology
:Category: Basic
:Current Version: 1.59
:Last Updated: 03/25/2024
:Producer: M. Dumontier
:License: Creative Commons 4.0
:Format: OWL, RDF, CSV
:Download: `SIO Homepage <https://bioportal.bioontology.org/ontologies/SIO>`_
:Documentation: `SIO Documentation <https://bioportal.bioontology.org/ontologies/SIO>`_

Base Metrics
---------------
    - Classes: 1,584
    - Individuals: 0
    - Properties: 212

Graph Metrics:
------------------
    - **Total Nodes**: 7,811
    - **Root Nodes**: 18
    - **Leaf Nodes**: 4,921
    - **Maximum Depth**: 23
    - **Edges**: 15,701

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 3,006
    - **Non-taxonomic Relations**: 115
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import SIO

   # Initialize and load ontology
   sio = SIO()
   sio.load("path/to/ontology.owl")
   # Extract datasets
   data = sio.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
