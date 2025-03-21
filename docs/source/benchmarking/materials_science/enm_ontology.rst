Environmental Noise Measurement Ontology (ENM)
=============================================

Overview
-----------------
The eNanoMapper project (https://www.enanomapper.net/), NanoCommons project (https://www.nanocommons.eu/)
and ACEnano project (http://acenano-project.eu/) are creating a pan-European computational infrastructure
for toxicological data management for ENMs, based on semantic web standards and ontologies.
This ontology is an application ontology targeting the full domain of nanomaterial safety assessment.
It re-uses several other ontologies including the NPO, CHEMINF, ChEBI, and ENVO.

:Domain: Nanomaterials
:Category: Material Science and Engineering
:Current Version: 10.0
:Last Updated: 2025-02-17
:Producer: eNanoMapper Consortium
:License: Creative Commons 3.0
:Format: OWL
:Download: `ENM Homepage <https://terminology.tib.eu/ts/ontologies/ENM>`_
:Documentation: `ENM Documentation <https://terminology.tib.eu/ts/ontologies/ENM>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics
------------------
    - **Total Nodes**: 102719
    - **Root Nodes**: 11156
    - **Leaf Nodes**: 64025
    - **Maximum Depth**: 131
    - **Edges**: 226566

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 9
    - **Taxonomic Relations**: 37103
    - **Non-taxonomic Relations**: 426
    - **Average Terms per Type**: 0.39

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import ENM

   # Initialize and load ontology
   enm = ENM()
   fso.load("path/to/ontology.owl")
   # Extract datasets
   data = enm.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
