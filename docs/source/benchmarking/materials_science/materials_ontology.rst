Material Ontology
==================

Overview
-----------------
The Material Ontology (MatOnto) is based on the upper level ontology, the BFO.

:Domain: Material Science and Engineering
:Category: Scholarly Knowledge
:Current Version:
:Last Updated:
:Producer:
:License:
:Format: OWL, TTL
:Download: `MATONTO Homepage <https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MatOnto.owl>`_
:Documentation: `MATONTO Documentation <https://github.com/EngyNasr/MSE-Benchmark/tree/main>`_

Base Metrics
-------------------
    - Classes: 847
    - Individuals: 131
    - Properties: 96

Graph Metrics:
------------------
    - **Total Nodes**: 4753
    - **Root Nodes**: 33
    - **Leaf Nodes**: 1063
    - **Maximum Depth**:
    - **Edges**: 11287

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 122
    - **Taxonomic Relations**: 2228
    - **Non-taxonomic Relations**: 434
    - **Average Terms per Type**: 5.08

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MatOnto

   # Initialize and load ontology
   matonto = MatOnto()
   matonto.load("path/to/ontology.owl")
   # Extract datasets
   data = matonto.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
