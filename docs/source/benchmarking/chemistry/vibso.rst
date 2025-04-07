The Vibration Spectroscopy Ontology (VIBSO)
===========================================

Overview
-----------------
The Vibration Spectroscopy Ontology defines technical terms with which research data produced
in vibrational spectroscopy experiments can be semantically enriched, made machine readable and FAIR.

:Domain: Chemistry
:Category: Spectroscopy
:Current Version: 2024-09-23
:Last Updated: 2024-09-23
:Producer: VIBSO Workgroup
:License: Creative Commons Attribution 4.0
:Format: OWL
:Download: `VIBSO Homepage <https://terminology.tib.eu/ts/ontologies/vibso>`_
:Documentation: `VIBSO Documentation <https://terminology.tib.eu/ts/ontologies/vibso>`_

Base Metrics
---------------
    - Classes: 478
    - Individuals: 118
    - Properties: 175

Graph Metrics:
------------------
    - **Total Nodes**: 4007
    - **Root Nodes**: 328
    - **Leaf Nodes**: 2547
    - **Maximum Depth**: 22
    - **Edges**: 8009

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 40
    - **Taxonomic Relations**: 856
    - **Non-taxonomic Relations**: 125
    - **Average Terms per Type**: 1.48

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import VIBSO

   # Initialize and load ontology
   ontology = VIBSO()
   ontology.load("path/to/ontology.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
