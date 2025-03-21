Hydra Core Vocabulary
=====================

Overview
-----------------
Hydra is a lightweight vocabulary to create hypermedia-driven Web APIs. By specifying a number of concepts
commonly used in Web APIs it enables the creation of generic API clients.

:Domain: Web Development
:Category: Web Development
:Current Version:
:Last Updated: 13 July 2021
:Producer: Hydra W3C Community Group
:License: Creative Commons 4.0
:Format: JSON-LD, RDF, TTL
:Download: `Hydra Homepage <https://www.hydra-cg.com/spec/latest/core/#references>`_
:Documentation: `Hydra Documentation <https://www.hydra-cg.com/spec/latest/core/#references>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 154
    - **Root Nodes**: 0
    - **Leaf Nodes**: 86
    - **Maximum Depth**: 0
    - **Edges**: 452

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 14
    - **Taxonomic Relations**: 15
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 1.56

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import Hydra

   # Initialize and load ontology
   hydra = Hydra()
   hydra.load("path/to/ontology.jsonld")
   # Extract datasets
   data = hydra.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
