Mass Spectrometry Ontology (MS)
===============================

Overview
-----------------
A structured controlled vocabulary for the annotation of experiments concerned with proteomics mass spectrometry.

:Domain: Chemistry
:Category: Mass Spectrometry, Proteomics
:Current Version:
:Last Updated: 12:02:2025
:Producer: Andreas Bertsch
:License: Creative Commons 4.0
:Format: OWL
:Download: `Mass Spectrometry Homepage <https://terminology.tib.eu/ts/ontologies/MS>`_
:Documentation: `Mass Spectrometry Documentation <https://terminology.tib.eu/ts/ontologies/MS>`_

Base Metrics
---------------
    - Classes: 3636
    - Individuals: 0
    - Properties: 42

Graph Metrics:
------------------
    - **Total Nodes**: 17851
    - **Root Nodes**: 3786
    - **Leaf Nodes**: 7959
    - **Maximum Depth**: 15
    - **Edges**: 51814

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 16046
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MassSpectrometry

   # Initialize and load ontology
   ontology = MassSpectrometry()
   ontology.load("path/to/ontology.owl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
