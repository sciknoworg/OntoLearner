Allotrope Foundation Ontology (AFO)
=========================================

Overview
-----------------
The AFO is an ontology suite that provides a standard vocabulary and semantic model
for the representation of laboratory analytical processes. The AFO suite is aligned at the upper layer
to the Basic Formal Ontology (BFO). The core domains modeled include, Equipment, Material, Process, and Results.
This artifact contains all triples of Allotrope Foundation Merged Without QUDT Ontology Suite (REC/2023/12)
together with triples inferred with HermiT.

:Domain: Chemistry
:Category: Laboratory Analytical Processes
:Current Version: 2024-06
:Last Updated: 2024-06-28
:Producer: Allotrope Foundation
:License: CC BY 4.0
:Format: TTL
:Download: `AFO Homepage <https://terminology.tib.eu/ts/ontologies/AFO>`_
:Documentation: `AFO Documentation <https://terminology.tib.eu/ts/ontologies/AFO>`_

Base Metrics
---------------
    - Classes: 3273
    - Individuals: 430
    - Properties: 48

Graph Metrics:
------------------
    - **Total Nodes**: 15547
    - **Root Nodes**: 142
    - **Leaf Nodes**: 8003
    - **Maximum Depth**: 32
    - **Edges**: 36699

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 38
    - **Taxonomic Relations**: 9889
    - **Non-taxonomic Relations**: 208
    - **Average Terms per Type**: 1.41

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import AFO

   # Initialize and load ontology
   ontology = AFO()
   ontology.load("path/to/ontology.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
