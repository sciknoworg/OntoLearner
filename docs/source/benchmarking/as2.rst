Activity Streams 2.0 Vocabulary
===============================

Overview
-----------------
Activity Streams 2.0 (AS2) is a social data format. Its types represent activities, content objects,
and actors like people or groups on the social web.

:Domain: Social Media
:Category: Social
:Current Version: 2.0
:Last Updated: 23 May 2017
:Producer:
:License: W3C Document License
:Format: OWL
:Download: `AS2 Homepage <https://github.com/w3c/activitystreams?tab=License-1-ov-file#readme>`_
:Documentation: `AS2 Documentation <https://github.com/w3c/activitystreams?tab=License-1-ov-file#readme>`_

Base Metrics
---------------
    - Classes: 10
    - Individuals: 0
    - Properties: 0


Schema Metrics
---------------
    - Attribute Richness: 0
    - Inheritance Richness: 0
    - Relationship Richness: 0

Graph Metrics:
------------------
    - **Total Nodes**: 426
    - **Root Nodes**: 0
    - **Leaf Nodes**: 120
    - **Maximum Depth**: 0
    - **Edges**: 945

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 59
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import AS2

   # Initialize and load ontology
   as2 = AS2()
   as2.load("path/to/ontology.owl")
   # Extract datasets
   data = as2.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
