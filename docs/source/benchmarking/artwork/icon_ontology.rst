ICON Ontology
==============================

Overview
-----------------
The ICON ontology deals with high granularity art interpretation. It was developed by conceptualizing
Panofsky&apos;s theory of levels of interpretation, therefore artworks can be described according
to Pre-iconographical, Iconographical and Iconological information.

:Domain: Art History, Cultural Heritage
:Category: Art Interpretation
:Current Version: 2.1.0
:Last Updated: April 26th, 2024
:Producer: Knowledge Media Institute
:License: Creative Commons 4.0
:Format: OWL
:Download: `ICON Ontology <https://w3id.org/icon/ontology/>`_
:Documentation: `ICON Repository <https://github.com/br0ast/ICON/tree/main/Development>`_

Base Metrics
---------------
    - Classes:
    - Object Properties:
    - Data Properties:
    - Annotation Assertions:

Graph Metrics:
-----------------
    - **Total Nodes**: 118
    - **Root Nodes**: 47
    - **Leaf Nodes**: 16
    - **Maximum Depth**: 3
    - **Edges**: 313
    - **Average Depth**: 1.5

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**:
    - **Taxonomic Relations**: 47
    - **Non-taxonomic Relations**: 3
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology.icon import IconOntology

   # Initialize and load ontology
   icon = IconOntology()
   icon.load("path/to/ontology.owl")
   # Extract datasets
   data = icon.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
