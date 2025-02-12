Material Information
====================

Overview
-----------------
The Material Information ontology is divided into smaller ontologies (partitions).
The partitions are Environment, Geometry, Material Information, Manufacturing Process, Property,
Substance, Unit Dimension, Structure, Equation and Physical Constant.

:Domain: Material Science and Engineering
:Category: Information Science
:Current Version:
:Last Updated:
:Producer: Toshihiro Ashino
:License:
:Format: OWL, RDF/XML
:Download: `Material Information Homepage <https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MaterialInformation.owl>`_
:Documentation: `Material Information Documentation <https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MaterialInformation.owl>`_

Base Metrics
---------------
    - Classes: 545
    - Individuals: 411
    - Properties: 98

Schema Metrics
---------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics:
------------------
    - **Total Nodes**: 1155
    - **Root Nodes**: 596
    - **Leaf Nodes**: 48
    - **Maximum Depth**:
    - **Edges**: 2343

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 410
    - **Taxonomic Relations**: 611
    - **Non-taxonomic Relations**: 32
    - **Average Terms per Type**: 6.72

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MaterialInformation

   # Initialize and load ontology
   material_information = MaterialInformation()
   material_information.load("path/to/ontology.owl")
   # Extract datasets
   data = material_information.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
