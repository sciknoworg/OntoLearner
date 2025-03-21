The DBpedia Ontology
====================

Overview
-----------------
The DBpedia ontology is generated from the manually created specifications in the DBpedia Mappings Wiki.
Each release of this ontology corresponds to a new release of the DBpedia dataset, which contains
instance data extracted from various language versions of Wikipedia. The DBpedia ontology has evolved
into a crowd-sourced effort, resulting in a shallow cross-domain ontology.

:Domain: General Knowledge
:Category: Knowledge Graph
:Current Version:
:Last Updated: 2008-11-17
:Producer: DBpedia Maintainers and Contributors
:License: Creative Commons 3.0
:Format: OWL
:Download: `DBpedia Homepage <https://wiki.dbpedia.org/>`_
:Documentation: `DBpedia Documentation <https://wiki.dbpedia.org/documentation>`_

Base Metrics
---------------
    - Classes:
    - Properties:
    - Annotation Assertions:

Graph Metrics:
------------------
    - **Total Nodes**: 4,051
    - **Root Nodes**: 3,489
    - **Leaf Nodes**: 100
    - **Maximum Depth**: 10
    - **Edges**: 13,762
    - **Average Depth**: 6.79

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 759
    - **Non-taxonomic Relations**: 825
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology.dbpedia import DBpediaOntology

   # Initialize and load ontology
   dbpedia = DBpedia()
   dbpedia.load("path/to/ontology.owl")
   # Extract datasets
   data = dbpedia.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
