Nanomaterials Ontology (NanoMine)
==================================

Overview
-----------------
Polymer Nanocomposites based ontology which enable researchers to develop and test
broad-reaching hypotheses about how inter-relationships between different materials
processing methods and composition result in specific changes in material properties.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version:
:Last Updated:
:Producer:
:License: APACHE 2.0
:Format: Turtle
:Download: `NanoMine Homepage <https://github.com/tetherless-world/nanomine-ontology>`_
:Documentation: `NanoMine Documentation <https://github.com/tetherless-world/nanomine-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 496
    - **Root Nodes**: 0
    - **Leaf Nodes**: 263
    - **Maximum Depth**: 0
    - **Edges**: 971

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 321
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import NanoMine

   # Initialize and load ontology
   ontology = NanoMine()
   ontology.load("path/to/nanomine.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
