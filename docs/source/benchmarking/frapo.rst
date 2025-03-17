Funding, Research Administration and Projects Ontology (FRAPO)
==============================================================

Overview
-----------------
The Funding, Research Administration and Projects Ontology (FRAPO) is an ontology
for describing the administrative information of research projects, e.g., grant applications,
funding bodies, project partners, etc.

:Domain: Administration
:Category: Administration
:Current Version:
:Last Updated:
:Producer: David Shotton
:License: Creative Commons 4.0
:Format: OWL, TTL, NT
:Download: `FRAPO Homepage <http://www.sparontologies.net/ontologies/frapo>`_
:Documentation: `FRAPO Documentation <http://www.sparontologies.net/ontologies/frapo>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 539
    - **Root Nodes**: 18
    - **Leaf Nodes**: 274
    - **Maximum Depth**: 3
    - **Edges**: 1076

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 25
    - **Taxonomic Relations**: 82
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 1.67

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import FRAPO

   # Initialize and load ontology
   frapo = FRAPO()
   frapo.load("path/to/ontology.owl")
   # Extract datasets
   data = frapo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
