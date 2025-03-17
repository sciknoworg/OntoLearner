Upper Mapping and Binding Exchange Layer (UMBEL) Vocabulary
==========================================================

Overview
-----------------
UMBEL is the Upper Mapping and Binding Exchange Layer, designed to help content interoperate on the Web.
UMBEL provides two valuable functions: First, it is a broad, general reference structure of 34,000 concepts,
which provides a scaffolding to link and interoperate other datasets and domain vocabularies.
Second, it is a base vocabulary for the construction of other concept-based domain ontologies,
also designed for interoperation.

:Domain: Web Development
:Category: General Knowledge
:Current Version: 1.50
:Last Updated: May 10, 2016
:Producer:
:License:
:Format: n3
:Download: `UMBEL Homepage <https://github.com/structureddynamics/UMBEL/tree/master/Ontology>`_
:Documentation: `UMBEL Documentation <https://github.com/structureddynamics/UMBEL/tree/master/Ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 1185
    - **Root Nodes**: 64
    - **Leaf Nodes**: 302
    - **Maximum Depth**: 55
    - **Edges**: 2868

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 10
    - **Taxonomic Relations**: 64
    - **Non-taxonomic Relations**: 33
    - **Average Terms per Type**: 1.25

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import UMBEL

   # Initialize and load ontology
   umbel = UMBEL()
   umbel.load("path/to/ontology.n3")
   # Extract datasets
   data = umbel.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
