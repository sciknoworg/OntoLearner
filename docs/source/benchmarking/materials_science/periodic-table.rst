Periodic Table of the Elements Ontology (PeriodicTable)
=======================================================

Overview
-----------------
PeriodicTable.owl is a representation of the Periodic Table of the Elements in the OWL Web Ontology Language.
It provides reference data to support Semantic Web applications in chemistry and related disciplines.

:Domain: Materials Science and Engineering
:Category: Chemistry
:Current Version: 1.10
:Last Updated: 2004/02/05
:Creator: Michael Cook
:License:
:Format: OWL
:Download: `PeriodicTable} Homepage <https://www.daml.org/2003/01/periodictable/>`_
:Documentation: `PeriodicTable Documentation <https://www.daml.org/2003/01/periodictable/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 730
    - **Root Nodes**: 2
    - **Leaf Nodes**: 521
    - **Maximum Depth**: 1
    - **Edges**: 1845

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 156
    - **Taxonomic Relations**: 302
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 7.09

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import PeriodicTable

   # Initialize and load ontology
   ontology = PeriodicTable()
   ontology.load("path/to/periodic-table.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
