The Platform MaterialDigital core ontology (PMDco)
==================================================

Overview
-----------------
The PMD Core Ontology (PMDco) is a comprehensive framework for representing knowledge that encompasses
fundamental concepts from the domains of materials science and engineering (MSE). The PMDco
has been designed as a mid-level ontology to establish a connection between specific MSE application ontologies
and the domain neutral concepts found in established top-level ontologies. The primary goal of the PMDco
is to promote interoperability between diverse domains.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 3.0.0-alpha1
:Last Updated: 2025-03-20
:Creator: Jannis Grundmann
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL/XML
:Download: `PMDco Homepage <https://github.com/materialdigital/core-ontology?tab=readme-ov-file>`_
:Documentation: `PMDco Documentation <https://materialdigital.github.io/core-ontology/index-en.html#>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 4207
    - **Root Nodes**: 85
    - **Leaf Nodes**: 2365
    - **Maximum Depth**: 22
    - **Edges**: 8103

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1126
    - **Non-taxonomic Relations**: 115
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import PMDco

   # Initialize and load ontology
   ontology = PMDco()
   ontology.load("path/to/pmdco.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
