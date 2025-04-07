Point Defects Ontology (PODO)
=============================

Overview
-----------------
PODO focuses on the description of point defects in crystalline materials.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 1.0.0
:Last Updated:
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWl
:Download: `PODO Homepage <https://github.com/OCDO/podo>`_
:Documentation: `PODO Documentation <https://github.com/OCDO/podo>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 153
    - **Root Nodes**: 38
    - **Leaf Nodes**: 84
    - **Maximum Depth**: 2
    - **Edges**: 192

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 12
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import PODO

   # Initialize and load ontology
   ontology = PODO()
   ontology.load("path/to/podo.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
