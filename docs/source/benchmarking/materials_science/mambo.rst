Molecules And Materials Basic Ontology (MAMBO)
===============================================

Overview
---------
MAMBO (Molecules And Materials Basic Ontology) is a domain ontology for molecular materials.
Its main targets are: Allowing the retrieval of structured information regarding molecular materials
and related applications (i.e. devices based on molecular materials) Supporting the development of new,
complex workflows for modelling systems based on molecular materials (computational modelling
and data-driven techniques) Integrating data generated via computational simulations and empirical experiments.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version:
:Last Updated:
:Producer:
:License: General Public License v3.0 (GPL-3.0)
:Format: OWL/XML
:Download: `MAMBO Homepage <https://github.com/daimoners/MAMBO>`_
:Documentation: `MAMBO Documentation <https://github.com/daimoners/MAMBO>`_

Base Metrics
-------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
--------------
    - **Total Nodes**: 166
    - **Root Nodes**:1
    - **Leaf Nodes**: 7
    - **Maximum Depth**: 1
    - **Edges**: 624

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 39
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
--------------
.. code-block:: python

   from ontolearner.ontology import MAMBO

   # Initialize and load ontology
   ontology = MAMBO()
   ontology.load("path/to/mambo.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
