Open Innovation Environment (OIE) domain ontologies, Manufacturing module (OIEManufacturing)
=============================================================================================

Overview
-----------------
Describes manufacturing processes with engineered participants. The module also provides a root for engineered materials.

:Domain: Materials Science and Engineering
:Category: Materials
:Current Version:
:Last Updated:
:Creator: Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `OIE Homepage <https://github.com/emmo-repo/OIE-Ontologies/>`_
:Documentation: `OIE Documentation <https://github.com/emmo-repo/OIE-Ontologies/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 380
    - **Root Nodes**: 13
    - **Leaf Nodes**: 131
    - **Maximum Depth**: 5
    - **Edges**: 869

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 249
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import OIEManufacturing

   # Initialize and load ontology
   ontology = OIEManufacturing()
   ontology.load("path/to/oie-manufacturing.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
