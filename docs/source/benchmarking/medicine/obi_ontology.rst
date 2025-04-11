Ontology for Biomedical Investigations (OBI)
============================================

Overview
-----------------
The Ontology for Biomedical Investigations (OBI) helps you communicate clearly about scientific investigations
by defining more than 2500 terms for assays, devices, objectives, and more.

:Domain: Medicine
:Category: Healthcare
:Current Version:
:Last Updated: 2025-01-09
:Producer:
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `OBI Homepage <https://github.com/obi-ontology/obi/tree/master>`_
:Documentation: `OBI Documentation <https://github.com/obi-ontology/obi/tree/master>`_

Base Metrics
------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
-------------
    - **Total Nodes**: 40613
    - **Root Nodes**: 177
    - **Leaf Nodes**: 10917
    - **Maximum Depth**: 28
    - **Edges**: 104537

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 288
    - **Taxonomic Relations**: 22953
    - **Non-taxonomic Relations**: 1121
    - **Average Terms per Type**: 6.70

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import OBI

   # Initialize and load ontology
   obi = OBI()
   obi.load("path/to/ontology.owl")
   # Extract datasets
   data = obi.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
