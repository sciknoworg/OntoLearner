Chemical Entities of Biological Interest Ontology (ChEBI)
=========================================================

Overview
-----------------
A structured classification of chemical compounds of biological relevance.

:Domain: Chemistry
:Category: Chemical Entities
:Current Version: 239
:Last Updated: 01/01/2025
:Producer:
:License: Creative Commons 4.0
:Format: OWL, OBO, JSON
:Download: `ChEBI Homepage <https://www.ebi.ac.uk/chebi/>`_
:Documentation: `ChEBI Documentation <https://www.ebi.ac.uk/chebi>`_

Base Metrics
---------------
    - Classes: 220,816
    - Individuals: 0
    - Properties: 10
    - Annotation Assertions: 0

Schema Metrics
---------------
    - Attribute Richness: 0
    - Inheritance Richness: 0
    - Relationship Richness: 0

Graph Metrics:
------------------
    - **Total Nodes**: 202549
    - **Root Nodes**: 188890
    - **Leaf Nodes**: 456
    - **Maximum Depth**: 23
    - **Edges**: 685993

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 739976
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import ChEBI

   # Initialize and load ontology
   chebi = ChEBI()
   chebi.load("path/to/ontology.owl")
   # Extract datasets
   data = chebi.extract()
   # Access specific relations
   term_types = data.term_typings
