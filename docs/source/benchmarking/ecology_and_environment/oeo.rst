The Open Energy Ontology (OEO)
==============================

Overview
-----------------
The Open Energy Ontology (OEO) is a domain ontology of the energy system analysis context. It is developed as part of the Open Energy Family. The OEO is published on GitHub under an open source license. The language used is the Manchester OWL Syntax, which was chosen because it is user-friendly for editing and viewing differences of edited files. The OEO is constantly being extended. The first version of the OEO has been released on June 11th 2020. A Steering Committee (OEO-SC) was created to accompany the development, increase awareness of the ontology and include it in current projects.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 2.7.0
:Last Updated: 03/2025
:Creator:
:License: Creative Commons Attribution 1.0 Generic (CC BY 1.0)
:Format: OWL/XML
:Download: `OEO Homepage <https://github.com/OpenEnergyPlatform/ontology?tab=readme-ov-file>`_
:Documentation: `OEO Documentation <https://github.com/OpenEnergyPlatform/ontology?tab=readme-ov-file>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 11699
    - **Root Nodes**: 2365
    - **Leaf Nodes**: 4476
    - **Maximum Depth**: 36
    - **Edges**: 32779

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 214
    - **Taxonomic Relations**: 6517
    - **Non-taxonomic Relations**: 254
    - **Average Terms per Type**: 5.22

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import OEO

   # Initialize and load ontology
   ontology = OEO()
   ontology.load("path/to/oeo-full.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
