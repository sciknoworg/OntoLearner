Automotive Ontology (AUTO)
==========================

Overview
-----------------
The AUTOMOTIVE ONTOLOGY (AUTO) defines the shared conceptual structures
in the automotive industry. It is an OWL ontology. It is built upon the auto schema.org
extension created by the W3C Automotive Ontology Community Group. AUTO's development process
follows the best practices established by the EDMC FIBO Community.

:Domain: Industry
:Category: Automotive
:Current Version:
:Last Updated: 2021-03-01
:Producer: EDM Council
:License: MIT
:Format: RDF
:Download: `Automotive Ontology (AUTO) Homepage <https://github.com/edmcouncil/auto/tree/master>`_
:Documentation: `Automotive Ontology (AUTO) Documentation <https://github.com/edmcouncil/auto/tree/master>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics
------------------
    - **Total Nodes**: 6344
    - **Root Nodes**: 417
    - **Leaf Nodes**: 2589
    - **Maximum Depth**: 37
    - **Edges**: 17693

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 58
    - **Taxonomic Relations**: 13448
    - **Non-taxonomic Relations**: 49
    - **Average Terms per Type**: 2.32

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import AUTO

   # Initialize and load ontology
   ontology = {{ class_name }}()
   ontology.load("path/to/auto.rdf")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
