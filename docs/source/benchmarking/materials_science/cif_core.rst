Crystallographic Information Framework (CIF) Core Dictionary (CIFCore)
======================================================================

Overview
-----------------
(1) to explain the historical development of CIF dictionaries to define in a machine-actionable manner the contents
of data files covering various aspects of crystallography and related structural sciences; (2) to demonstrate
some of the more complex types of information that can be handled with this approach.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.1.0
:Last Updated: May 24, 2023
:Producer: {{ producer }}
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: Turtle
:Download: `CIFCore Homepage <https://github.com/emmo-repo/CIF-ontology?tab=readme-ov-file>`_
:Documentation: `CIFCore Documentation <https://www.iucr.org/resources/cif/dictionaries/cif_core>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 4494
    - **Root Nodes**: 1
    - **Leaf Nodes**: 3310
    - **Maximum Depth**: 1
    - **Edges**: 15377

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 27150
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import CIFCore

   # Initialize and load ontology
   ontology = CIFCore()
   ontology.load("path/to/ontology.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
