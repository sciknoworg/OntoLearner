Gene Ontology (GO)
==================

Overview
-----------------
The Gene Ontology (GO) Provides structured controlled vocabularies for the annotation of gene products
with respect to their molecular function, cellular component, and biological role.
The Gene Ontology consists of three Vocabularies.

:Domain: Molecular Biology
:Category: Genomic and Proteomic
:Current Version:
:Last Updated: 2024-11-03
:Producer:
:License: Creative Commons 4.0
:Format: OWL, OBO, JSON
:Download: `GO Homepage <https://geneontology.org/docs/download-ontology/>`_
:Documentation: `GO Documentation <http://geneontology.org>`_

Base Metrics
---------------
    - Classes: 51,567
    - Individuals: 0
    - Properties: 9
    - Annotation Assertions: 0

Schema Metrics
---------------
    - Attribute Richness: 0
    - Inheritance Richness: 0
    - Relationship Richness: 0

Graph Metrics:
------------------
    - **Total Nodes**: 48,020
    - **Root Nodes**: 32,712
    - **Leaf Nodes**: 49
    - **Maximum Depth**: 16
    - **Edges**: 115,518

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 156430
    - **Non-taxonomic Relations**: 30
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import GO

   # Initialize and load ontology
   go = GO()
   go.load("path/to/ontology.owl")
   # Extract datasets
   data = go.extract()
   # Access specific relations
   term_types = data.term_typings
