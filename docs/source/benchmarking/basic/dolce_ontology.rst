Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE)
=====================================================================

Overview
-----------------
The Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE) is a foundational ontology
that provides a conceptual framework for the formalization of domain ontologies.

:Domain: Linguistics, Cognitive Science
:Category: Foundational Ontology
:Current Version:
:Last Updated:
:Producer: Laboratory for Applied Ontology, ISTC-CNR
:License: Creative Commons 4.0
:Format: OWL, RDF/XML, TTL
:Download: `DOLCE Homepage <https://www.loa.istc.cnr.it/index.php/dolce/>`_
:Documentation: `DOLCE Documentation <https://www.loa.istc.cnr.it/index.php/dolce/>`_

Base Metrics
---------------
    - Classes: 79
    - Individuals: 0
    - Properties: 123

Graph Metrics:
------------------
    - **Total Nodes**: 252
    - **Root Nodes**: 10
    - **Leaf Nodes**: 86
    - **Maximum Depth**:
    - **Edges**: 689

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 231
    - **Non-taxonomic Relations**: 24
    - **Average Terms per Type**: 0.00

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import DOLCE

   # Initialize and load ontology
   dolce = DOLCE()
   dolce.load("path/to/ontology.owl")
   # Extract datasets
   data = dolce.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
