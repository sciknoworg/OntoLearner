Reactions Ontology (RXNO)
=========================

Overview
-----------------
RXNO is the name reaction ontology. It contains more than 500 classes representing organic reactions
such as the Diels–Alder cyclization.

:Domain: Chemistry
:Category: Chemistry
:Current Version:
:Last Updated: 2021-12-16
:Producer:
:License: Creative Commons 4.0
:Format: OWL
:Download: `RXNO Homepage <https://github.com/rsc-ontologies/rxno>`_
:Documentation: `RXNO Documentation <https://github.com/rsc-ontologies/rxno>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 5676
    - **Root Nodes**: 845
    - **Leaf Nodes**: 2924
    - **Maximum Depth**: 16
    - **Edges**: 14,841

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 3757
    - **Non-taxonomic Relations**: 87
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import RXNO

   # Initialize and load ontology
   rxno = RXNO()
   rxno.load("path/to/ontology.owl")
   # Extract datasets
   data = rxno.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
