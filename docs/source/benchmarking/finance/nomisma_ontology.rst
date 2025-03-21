Nomisma Ontology
================

Overview
-----------------
Nomisma Ontology is a collaborative project to provide stable digital representations of numismatic concepts according
to the principles of Linked Open Data. These take the form of http URIs that provide access to the information
about a concept in various formats. The project is a collaborative effort of the American Numismatic Society
and the Institute for the Study of the Ancient World at New York University.

:Domain: Numismatics
:Category: Financial
:Current Version:
:Last Updated: 2025-01-22
:Producer: American Numismatic Society, Institute for the Study of the Ancient World
:License: Creative Commons 4.0
:Format: RDF, TTL
:Download: `Nomisma Homepage <https://www.dainst.org/forschung/projekte/noslug/2098>`_
:Documentation: `Nomisma Documentation <https://www.dainst.org/forschung/projekte/noslug/2098>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 245
    - **Root Nodes**: 22
    - **Leaf Nodes**: 113
    - **Maximum Depth**: 3
    - **Edges**: 431

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 13
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import Nomisma

   # Initialize and load ontology
   nomisma = Nomisma()
   nomisma.load("path/to/ontology.ttl")
   # Extract datasets
   data = nomisma.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
