Crystallographic Defect Core Ontology (CDCO)
=============================================

Overview
-----------------
CDCO defines the common terminology shared across all types of crystallographic defects,
providing a unified framework for data integration in materials science.

:Domain: Material Science and Engineering
:Category: Materials Science Ontology
:Current Version: 1.0.0
:Last Updated:
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `CDCO Homepage <https://github.com/OCDO/cdco>`_
:Documentation: `CDCO Documentation <https://github.com/OCDO/cdco>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 85
    - **Root Nodes**: 8
    - **Leaf Nodes**: 53
    - **Maximum Depth**: 1
    - **Edges**: 123

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 4
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import CDCO

   # Initialize and load ontology
   ontology = CDCO()
   ontology.load("path/to/cdco.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
