GIST Ontology
================

Overview
-----------------
Gist is Semantic Arts' minimalist upper ontology for the enterprise.
It is designed to have the maximum coverage of typical business ontology concepts
with the fewest number of primitives and the least amount of ambiguity.

:Domain: Industry
:Category: Upper Ontology
:Current Version: 12.1.0
:Last Updated: 2024-Feb-27
:Producer: Semantic Arts
:License: Creative Commons 4.0
:Format: OWL
:Download: `GIST Homepage <https://semanticarts.com/gist>`_
:Documentation: `GIST Documentation <https://semanticarts.com/gist>`_

Base Metrics
---------------
    - Classes: 97
    - Individuals: 0
    - Properties: 121
    - Annotation Assertions: 0

Graph Metrics:
------------------
    - **Total Nodes**: 1352
    - **Root Nodes**: 77
    - **Leaf Nodes**: 633
    - **Maximum Depth**:
    - **Edges**: 2543

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 8
    - **Taxonomic Relations**: 78
    - **Non-taxonomic Relations**: 106
    - **Average Terms per Type**: 1.33

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import GIST

   # Initialize and load ontology
   gist = GIST()
   gist.load("path/to/ontology.owl")
   # Extract datasets
   data = gist.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
