Life Ontology (LifO)
==============================

Overview
-----------------
LifO is a formal ontology that represents the life processes of organisms and related entities and relations.
LifO is a general purpose ontology that covers the common features associated with different types of organisms
such as unicellular prokaryotes (e.g., E. coli) and multicellular organisms (e.g., humans).

:Domain: Biology, Life Sciences
:Category: General Purpose
:Current Version: 1.0.17
:Last Updated: March 11, 2018
:Producer: Yongqun &quot;Oliver&quot; He (YH)
:License: Creative Commons 4.0
:Format: OWL
:Download: `LifO Homepage <https://bioportal.bioontology.org/ontologies/LIFO>`_

Base Metrics
---------------
    - Classes: 215
    - Properties: 98
    - Annotations: 0

Graph Metrics:
------------------
    - **Total Nodes**: 416
    - **Root Nodes**: 230
    - **Leaf Nodes**: 38
    - **Maximum Depth**: 9
    - **Edges**: 1046
    - **Average Depth**: 3.00

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 9
    - **Taxonomic Relations**: 321
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.69

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology.computer import LIFO

   # Initialize and load ontology
   life = LIFO()
   life.load("path/to/ontology.owl")
   # Extract datasets
   data = life.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
