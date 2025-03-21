PRotein Ontology (PRO)
======================

Overview
-----------------
The PRotein Ontology (PRO) formally defines taxon-specific and taxon-neutral protein-related entities
in three major areas: proteins related by evolution; proteins produced from a given gene;
and protein-containing complexes

:Domain: Biology
:Category: Healthcare
:Current Version: 70.0
:Last Updated: 08:08:2024
:Producer:
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `PRO Homepage <https://obofoundry.org/ontology/pr.html>`_
:Documentation: `PRO Documentation <https://obofoundry.org/ontology/pr.html>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 0
    - **Root Nodes**: 0
    - **Leaf Nodes**: 0
    - **Maximum Depth**: 0
    - **Edges**: 0

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 0
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import PRO

   # Initialize and load ontology
   pro = PRO()
   pro.load("path/to/ontology.owl")
   # Extract datasets
   data = pro.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
