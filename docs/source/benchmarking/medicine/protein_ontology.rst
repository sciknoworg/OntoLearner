Ontology for Biomedical Investigations (OBI)
============================================

Overview
-----------------
The PRotein Ontology (PRO) formally defines taxon-specific and taxon-neutral protein-related entities
in three major areas: proteins related by evolution; proteins produced from a given gene;
and protein-containing complexes.

:Domain: Medicine
:Category: Healthcare
:Current Version: 1.2
:Last Updated: 08:08:2024
:Producer:
:License: `Creative Commons 4.0 <https://creativecommons.org/licenses/by/4.0/>`_
:Format: RDF
:Download: `PRO Homepage <http://purl.obolibrary.org/obo/pr.owl>`_
:Documentation: `PRO Documentation <https://proconsortium.org/protein-ontology/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
---------------
    - **Total Nodes**: 4214485
    - **Root Nodes**: 1158591
    - **Leaf Nodes**: 1642782
    - **Maximum Depth**: 1
    - **Edges**: 13562571

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2783894
    - **Non-taxonomic Relations**: 127293
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import PRoteinOntology

   # Initialize and load ontology
   pro = PRoteinOntology()
   pro.load("path/to/pro.rdf")
   # Extract datasets
   data = pro.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
