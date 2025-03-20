The Elementary Multiperspective Material Ontology (EMMO)
=======================================================

Overview
-----------------
The Elementary Multiperspective Material Ontology (EMMO) is the result of a multidisciplinary effort within the EMMC,
aimed at the development of a standard representational ontology framework based on current materials modelling
and characterization knowledge. Instead of starting from general upper level concepts, as done by other ontologies,
the EMMO development started from the very bottom level, using the actual picture of the physical world coming
from applied sciences, and in particular from physics and material sciences.

:Domain: Materials Science
:Category: Materials Modelling
:Current Version: 1.0.0-rc3
:Last Updated: 2024-03
:Producer: European Materials Modelling Council (EMMC)
:License: Creative Commons 4.0
:Format: OWL, RDF/XML, TTL, JSON-LD
:Download: `EMMO Homepage <https://emmo-repo.github.io/>`_
:Documentation: `EMMO Documentation <https://emmo-repo.github.io/>`_


Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 13613
    - **Root Nodes**: 281
    - **Leaf Nodes**: 7742
    - **Maximum Depth**:
    - **Edges**: 30349

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 2
    - **Taxonomic Relations**: 27873
    - **Non-taxonomic Relations**: 77
    - **Average Terms per Type**: 0.20

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import EMMO

   # Initialize and load ontology
   emmo = EMMO()
   emmo.load("path/to/ontology.owl")
   # Extract datasets
   data = emmo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
