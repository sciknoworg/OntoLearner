The OBO Relations Ontology (RO)
============================

Overview
-----------------
The Relations Ontology (RO) is a collection of OWL relations (ObjectProperties) intended for use
across a wide variety of biological ontologies.

:Domain: Biology
:Category: Relations
:Current Version: 2024-04-24
:Last Updated: 2024-04-24
:Producer:
:License: CC0
:Format: OWL
:Download: `RO Homepage <http://purl.obolibrary.org/obo/ro.owl>`_
:Documentation: `RO Documentation <https://oborel.github.io/obo-relations/>`_

Base Metrics
---------------
    - Classes: 57
    - Individuals: 35
    - Properties: 807
    - Annotation Assertions: 0

Schema Metrics
---------------
    - Attribute Richness: 0
    - Inheritance Richness: 0
    - Relationship Richness: 0

Graph Metrics:
------------------
    - **Total Nodes**: 937
    - **Root Nodes**: 488
    - **Leaf Nodes**: 34
    - **Maximum Depth**: 0
    - **Edges**: 3085

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 2
    - **Taxonomic Relations**: 64
    - **Non-taxonomic Relations**: 10
    - **Average Terms per Type**: 0.15

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import RO

   # Initialize and load ontology
   ro = RO()
   ro.load("path/to/ontology.owl")
   # Extract datasets
   data = ro.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
