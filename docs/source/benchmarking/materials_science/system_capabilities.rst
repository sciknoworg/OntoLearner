System capabilities, operating ranges, and survival ranges ontology (SystemCapabilities)
=========================================================================================

Overview
-----------------
This ontology describes system capabilities, operating ranges, and survival ranges.

:Domain: Materials Science & Engineering
:Category: Materials Science, Engineering, Systems
:Current Version:
:Last Updated: 2017-05-14
:Producer: W3C/OGC Spatial Data on the Web Working Group
:License: W3C Software and Document License
:Format: OWL
:Download: `SystemCapabilities Homepage <https://terminology.tib.eu/ts/ontologies/SSNSYSTEM>`_
:Documentation: `SystemCapabilities Documentation <https://terminology.tib.eu/ts/ontologies/SSNSYSTEM>`_

Base Metrics
---------------
    - Classes: 65
    - Individuals: 1
    - Properties: 82

Graph Metrics:
------------------
    - **Total Nodes**: 137
    - **Root Nodes**: 14
    - **Leaf Nodes**: 47
    - **Maximum Depth**: 2
    - **Edges**: 268

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 2
    - **Taxonomic Relations**: 148
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.4

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import SystemCapabilities

   # Initialize and load ontology
   ontology = SystemCapabilities()
   ontology.load("path/to/ontology.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
