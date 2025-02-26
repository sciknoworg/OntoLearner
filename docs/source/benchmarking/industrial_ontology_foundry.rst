Industrial Ontology Foundry (IOF)
=================================

Overview
-----------------
The IOF Core Ontology contains notions found to be common across multiple manufacturing domains.
This file is an RDF implementation of these notions. The ontology utilizes the Basic Formal Ontology or BFO
as a top-level ontology but also borrows terms from various domain-independent or mid-level ontologies.
The purpose of the ontology is to serve as a foundation for ensuring consistency
and interoperability across various domain-specific reference ontologies the IOF publishes.

:Domain: Industrial Manufacturing
:Category: Scholarly Knowledge
:Current Version: 1.0
:Last Updated: 2020
:Producer: IOF Core Working Group
:License: MIT
:Format: RDF, OWL, TTL, CSV, NT
:Download: `IOF Homepage <https://oagi.org/pages/Released-Ontologies>`_
:Documentation: `IOF Documentation <https://ontocommons.eu/initiatives/industry-ontology-foundry>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Schema Metrics
---------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics:
------------------
    - **Total Nodes**: 1442
    - **Root Nodes**: 13
    - **Leaf Nodes**: 716
    - **Maximum Depth**: 6
    - **Edges**: 2686

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 298
    - **Non-taxonomic Relations**: 29
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import IOF

   # Initialize and load ontology
   iof = IOF()
   iof.load("path/to/ontology.owl")
   # Extract datasets
   data = iof.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
