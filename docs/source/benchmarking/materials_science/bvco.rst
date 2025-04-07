Battery Value Chain Ontology (BVCO)
===================================

Overview
-----------------
Battery Value Chain Ontology (BVCO) aims to model processes along the Battery value chain. Processes are
holistic perspective elements that transform inputs/educts (matter, energy, information)
into output/products (matter, energy, information) with the help of tools (devices, algorithms).
They can be decomposed into sub-processes and have predecessor and successor processes.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.4.3
:Last Updated:
:Producer: Lukas Gold, Simon Stier
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: Turtle
:Download: `BVCO Homepage <https://github.com/Battery-Value-Chain-Ontology/ontology>`_
:Documentation: `BVCO Documentation <https://github.com/Battery-Value-Chain-Ontology/ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics
------------------
    - **Total Nodes**: 804
    - **Root Nodes**: 85
    - **Leaf Nodes**: 283
    - **Maximum Depth**: 30
    - **Edges**: 1719

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1396
    - **Non-taxonomic Relations**: 5
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BVCO

   # Initialize and load ontology
   ontology = BVCO()
   ontology.load("path/to/bvco.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
