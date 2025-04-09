Physico-chemical methods and properties (FIX)
=============================================

Overview
-----------------
An ontology of physico-chemical methods and properties.

:Domain: Chemistry
:Category: Chemicals, Properties
:Current Version: 2020-04-13
:Last Updated: 2020-04-13
:Producer: N/A
:License: N/A
:Format: OWL
:Download: `FIX Homepage <https://terminology.tib.eu/ts/ontologies/FIX>`_
:Documentation: `FIX Documentation <hhttps://terminology.tib.eu/ts/ontologies/FIX>`_

Base Metrics
---------------
    - Classes: 1163
    - Individuals: 0
    - Properties: 15

Graph Metrics:
------------------
    - **Total Nodes**: 3402
    - **Root Nodes**: 22
    - **Leaf Nodes**: 2147
    - **Maximum Depth**: 14
    - **Edges**: 7621

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2978
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import FIX

   # Initialize and load ontology
   ontology = FIX()
   ontology.load("path/to/ontology.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
