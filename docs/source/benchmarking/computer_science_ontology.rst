Computer Science Ontology (CSO)
==============================

Overview
-----------------
The Computer Science Ontology (CSO) is a large-scale ontology of research areas in computer science.
It provides a comprehensive vocabulary of research topics in computing, organized in a hierarchical structure.

:Domain: Computer Science
:Category: Research Areas
:Current Version: 3.4
:Last Updated:
:Producer: Knowledge Media Institute, Open University
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `CSO Homepage <https://cso.kmi.open.ac.uk/home>`_
:Documentation: `CSO Documentation <https://cso.kmi.open.ac.uk/about>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:
    - Annotation Assertions:
    - DL Expressivity:

Schema Metrics
---------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics:
------------------
    - **Total Nodes**: 38901
    - **Root Nodes**: 82
    - **Leaf Nodes**: 24203
    - **Maximum Depth**: 11
    - **Edges**: 93,289

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 44204
    - **Non-taxonomic Relations**: 49085
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology.computer import ComputerOntology

   # Initialize and load ontology
   cso = ComputerOntology()
   cso.load("path/to/ontology.owl")
   # Extract datasets
   data = cso.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
