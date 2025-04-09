Materials Vocabulary (MatVoc)
==============================

Overview
-----------------
The official ontology produced in the context of the STREAM project.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 1.0.0
:Last Updated: 2022-12-12
:Producer: Tatyana Sheveleva, Javad Chamanara
:License: MIT License
:Format: RDF/XML,TTL
:Download: `MatVoc Homepage <https://stream-project.github.io/#overv>`_
:Documentation: `MatVoc Documentation <https://stream-project.github.io/#overv>`_

Base Metrics
---------------
    - Classes: 31
    - Individuals: 0
    - Properties: 12

Graph Metrics
------------------
    - **Total Nodes**: 94
    - **Root Nodes**: 16
    - **Leaf Nodes**: 44
    - **Maximum Depth**: 2
    - **Edges**: 161

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 6
    - **Non-taxonomic Relations**: 7
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MatVoc

   # Initialize and load ontology
   ontology = MatVoc()
   ontology.load("path/to/matvoc.rdf")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
