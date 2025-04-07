Open Innovation Environment (OIE) domain ontologies, Software module (OIESoftware)
====================================================================================

Overview
-----------------
EMMO-compliant, domain-level OIE ontology tackling the area of software products.

:Domain: Materials Science and Engineering
:Category: Materials
:Current Version: 0.1
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
    - **Total Nodes**: 205
    - **Root Nodes**: 17
    - **Leaf Nodes**: 49
    - **Maximum Depth**: 5
    - **Edges**: 489

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 188
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import OIESoftware

   # Initialize and load ontology
   ontology = OIESoftware()
   ontology.load("path/to/oie-software.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
