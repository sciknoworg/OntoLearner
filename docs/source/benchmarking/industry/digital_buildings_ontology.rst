Digital Buildings Ontology
===========================

Overview
-----------------
The Digital Buildings ontology (DBO) is used by Google to represent structured information
about buildings and building-installed equipment.

:Domain: Industry
:Category: Building Information
:Current Version: 0.0.1
:Last Updated: 02/23/2023
:Producer: Google
:License: Apache 2.0
:Format: OWL, CSV, RDF/XML
:Download: `DBO Homepage <https://github.com/google/digitalbuildings?tab=readme-ov-file>`_
:Documentation: `DBO Documentation <https://github.com/google/digitalbuildings?tab=readme-ov-file>`_

Base Metrics
---------------
    - Classes: 1,334
    - Individuals: 35
    - Properties: 7

Graph Metrics:
------------------
    - **Total Nodes**: 13152
    - **Root Nodes**: 1
    - **Leaf Nodes**: 686
    - **Maximum Depth**: 6
    - **Edges**: 32,491

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 35
    - **Taxonomic Relations**: 37,016
    - **Non-taxonomic Relations**: 12
    - **Average Terms per Type**: 1.09

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import DBO

   # Initialize and load ontology
   dbo = DBO()
   dbo.load("path/to/ontology.owl")
   # Extract datasets
   data = dbo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
