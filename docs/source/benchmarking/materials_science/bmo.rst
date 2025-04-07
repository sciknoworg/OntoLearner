Building Material Ontology (BMO)
================================

Overview
-----------------
Building Material Ontology defines the main concepts of building material,
types, layers, and properties.

:Domain: Materials Science & Engineering
:Category: Materials
:Current Version: 0.1
:Last Updated: 2019-12-10
:Producer: Janakiram Karlapudi (janakiram.karlapudi@tu-dresden.de), Prathap Valluru (prathap.valluru@tu-dresden.de)
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL, OWL, RDF/XML
:Download: `BMO Homepage <https://matportal.org/ontologies/BUILDMAT>`_
:Documentation: `BMO Documentation <{https://matportal.org/ontologies/BUILDMAT>`_

Base Metrics
---------------
    - Classes: 26
    - Individuals: 12
    - Properties: 63

Graph Metrics
------------------
    - **Total Nodes**: 203
    - **Root Nodes**: 83
    - **Leaf Nodes**: 68
    - **Maximum Depth**: 7
    - **Edges**: 420

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 12
    - **Taxonomic Relations**: 20
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.67

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BMO

   # Initialize and load ontology
   ontology = BMO()
   ontology.load("path/to/bmo.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
