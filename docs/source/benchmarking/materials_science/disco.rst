Dislocation Ontology (DISCO)
=================================

Overview
-----------------
DISO is an ontology that defines the linear defect, in particular dislocation concepts
and relations between them in crystalline materials.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 1.0
:Last Updated: 21.03.202
:Producer: Ahmad Zainul Ihsan
:License: Creative Commons Attribution 3.0 International (CC BY 3.0)
:Format: OWL/XML, RDF/XML, Turtle
:Download: `DISCO Homepage <https://github.com/Materials-Data-Science-and-Informatics/dislocation-ontology>`_
:Documentation: `DISCO Documentation <{https://github.com/Materials-Data-Science-and-Informatics/dislocation-ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 324
    - **Root Nodes**: 9
    - **Leaf Nodes**: 91
    - **Maximum Depth**: 1
    - **Edges**: 739

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 202
    - **Non-taxonomic Relations**: 6
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import DISCO

   # Initialize and load ontology
   ontology = DISCO()
   ontology.load("path/to/disco.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
