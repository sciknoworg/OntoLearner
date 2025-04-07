Mechanical Testing Ontology (MechanicalTesting)
===============================================

Overview
-----------------
A domain ontology for mechanical testing based on EMMO.

:Domain: Materials Science & Engineering
:Category: Mechanical Testing
:Current Version: 1.0.0
:Last Updated:
:Producer: Fraunhofer IWM
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL/XML
:Download: `MechanicalTesting Homepage <https://github.com/emmo-repo/domain-mechanical-testing>`_
:Documentation: `MechanicalTesting Documentation <https://github.com/emmo-repo/domain-mechanical-testing>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 1365
    - **Root Nodes**: 174
    - **Leaf Nodes**: 713
    - **Maximum Depth**: 20
    - **Edges**: 2569

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2745
    - **Non-taxonomic Relations**: 14
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MechanicalTesting

   # Initialize and load ontology
   ontology = MechanicalTesting()
   ontology.load("path/to/ontology.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
