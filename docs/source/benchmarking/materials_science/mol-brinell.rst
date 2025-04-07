MatoLab Brinell Test Ontology (MOLBRINELL)
============================================

Overview
-----------------
An ontology for describing the Brinell hardness testing process, made in the Materials Open Lab Project.

:Domain: Materials Science and Engineering
:Category: Materials Testing
:Current Version: 0.1
:Last Updated: 05/05/2022
:Creator: Birgit Skrotzki, Hossein Beygi Nasrabadi, Philipp von Hartrott, Vinicius Carrillo Beber, Yue Chen
:License:
:Format: TTL, RDF/XML, OWL
:Download: `MOLBRINELL Homepage <https://matportal.org/ontologies/MOL_BRINELL>`_
:Documentation: `MOLBRINELL Documentation <https://matportal.org/ontologies/MOL_BRINELL>`_

Base Metrics
---------------
    - Classes: 37
    - Individuals: 3,277
    - Properties: 21

Graph Metrics
------------------
    - **Total Nodes**: 3648
    - **Root Nodes**: 29
    - **Leaf Nodes**: 308
    - **Maximum Depth**: 2
    - **Edges**: 16347

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 3053
    - **Taxonomic Relations**: 14
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 82.51

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MOLBRINELL

   # Initialize and load ontology
   ontology = MOLBRINELL()
   ontology.load("path/to/mol-brinell.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
