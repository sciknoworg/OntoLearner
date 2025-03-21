The Description of a Project (DOAP) vocabulary
==============================================

Overview
-----------------
The Description of a Project (DOAP) vocabulary, described using W3C RDF Schema and the Web Ontology Language
to describe software projects, and in particular open source projects.

:Domain: Industry
:Category: Software
:Current Version:
:Last Updated: 2020-04-03
:Producer: Edd Wilder-James
:License: Apache License 2.0
:Format: RDF
:Download: `DOAP Homepage <https://github.com/ewilderj/doap/blob/master/schema/doap.rdf>`_
:Documentation: `DOAP Documentation <https://github.com/ewilderj/doap/wiki>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 496
    - **Root Nodes**: 1
    - **Leaf Nodes**: 435
    - **Maximum Depth**: 1
    - **Edges**: 634

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 14
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import DOAP

   # Initialize and load ontology
   doap = DOAP()
   doap.load("path/to/ontology.rdf")
   # Extract datasets
   data = doap.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
