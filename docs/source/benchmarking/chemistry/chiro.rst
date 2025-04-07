CHEBI Integrated Role Ontology (CHIRO)
=========================================

Overview
-----------------
CHEBI provides a distinct role hierarchy. Chemicals in the structural hierarchy are connected
via a 'has role' relation. CHIRO provides links from these roles to useful other classes in other ontologies.
This will allow direct connection between chemical structures (small molecules, drugs) and what they do.
This could be formalized using 'capable of', in the same way Uberon and the Cell Ontology link structures to processes.

:Domain: Chemistry
:Category: Chemicals, Roles
:Current Version: 2015-11-23
:Last Updated: 2015-11-23
:Producer: N/A
:License: Creative Commons 1.0
:Format: OWL
:Download: `CHIRO Homepage <https://terminology.tib.eu/ts/ontologies/chiro>`_
:Documentation: `CHIRO Documentation <https://terminology.tib.eu/ts/ontologies/chiro>`_

Base Metrics
---------------
    - Classes: 13279
    - Individuals: 0
    - Properties: 59

Graph Metrics:
------------------
    - **Total Nodes**: 81778
    - **Root Nodes**: 14636
    - **Leaf Nodes**: 50439
    - **Maximum Depth**: 18
    - **Edges**: 197071

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 27299
    - **Non-taxonomic Relations**: 647
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import Chiro

   # Initialize and load ontology
   ontology = Chiro()
   ontology.load("path/to/ontology.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
