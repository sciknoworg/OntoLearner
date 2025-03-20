Ontology for Biomedical Investigations (OBI)
============================================

Overview
-----------------
The PRotein Ontology (PRO) formally defines taxon-specific and taxon-neutral protein-related entities
in three major areas: proteins related by evolution; proteins produced from a given gene;
and protein-containing complexes.

:Domain: Biomedical Science
:Category: Healthcare
:Current Version:
:Last Updated:
:Producer:
:License: Creative Commons 4.0
:Format:
:Download:
:Documentation:

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
---------------
    - **Total Nodes**:
    - **Root Nodes**:
    - **Leaf Nodes**:
    - **Maximum Depth**:
    - **Edges**:

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**:
    - **Taxonomic Relations**:
    - **Non-taxonomic Relations**:
    - **Average Terms per Type**:

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import PRoteinOntology

   # Initialize and load ontology
   pro = PRoteinOntology()
   pro.load("path/to/ontology.owl")
   # Extract datasets
   data = pro.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
