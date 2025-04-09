Molecular Process Ontology (MOP)
================================

Overview
-----------------
MOP is the molecular process ontology. It contains the molecular processes that underlie
the name reaction ontology RXNO, for example cyclization, methylation and demethylation.

:Domain: chemistry
:Category: Chemistry, Molecular Biology
:Current Version: 2022-05-11
:Last Updated: 2022-05-11
:Producer: {{ producer }}
:License: Creative Commons 4.0
:Format: OWL
:Download: `MOP Homepage <https://terminology.tib.eu/ts/ontologies/MOP>`_
:Documentation: `MOP Documentation <https://github.com/rsc-ontologies/rxno>`_

Base Metrics
---------------
    - Classes: 3686
    - Individuals: 0
    - Properties: 38

Graph Metrics:
------------------
    - **Total Nodes**: 15794
    - **Root Nodes**: 3693
    - **Leaf Nodes**: 8182
    - **Maximum Depth**: 14
    - **Edges**: 41157

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 4171
    - **Non-taxonomic Relations**: 78
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MOP

   # Initialize and load ontology
   ontology = MOP()
   ontology.load("path/to/ontology.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
