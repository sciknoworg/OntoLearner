Materials Mechanics Ontology (MMO)
==================================

Overview
-----------------
The materials mechanics ontology is an application-level ontology that was created
for supporting named entity recognition tasks for materials fatigue domain. The ontology covers
some fairly general MSE concepts that could prospectively be merged into PMDco or other upper materials ontologies
such as descriptions of crystallographic defects and microstructural entities.
Furthermore, concepts related to the materials fatigue subdomain are also heavily incorporated.

:Domain: Materials Science & Engineering
:Category: Scholarly Knowledge
:Current Version: 1.0.1
:Last Updated: 2024-01-30
:Producer: Akhil Thomas, Ali Riza Durmaz
:License: Creative Commons 4.0
:Format: OWL, TTL
:Download: `MMO Homepage <https://iwm-micro-mechanics-public.pages.fraunhofer.de/ontologies/materials-mechanics-ontology/index-en.html>`_
:Documentation: `MMO Documentation <https://iwm-micro-mechanics-public.pages.fraunhofer.de/ontologies/materials-mechanics-ontology/index-en.html>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 1043
    - **Root Nodes**: 11
    - **Leaf Nodes**: 509
    - **Maximum Depth**:
    - **Edges**: 2402

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 876
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MMO

   # Initialize and load ontology
   mmo = MMO()
   mmo.load("path/to/ontology.owl")
   # Extract datasets
   data = mmo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
