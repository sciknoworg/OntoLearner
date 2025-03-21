The Chemical Methods Ontology (ChMO)
====================================

Overview
-----------------
The Chemical Methods Ontology contains more than 3000 classes and describes methods used to:
- collect data in chemical experiments, such as mass spectrometry and electron microscopy.
- prepare and separate material for further analysis, such as sample ionisation, chromatography, and electrophoresis
- synthesise materials, such as epitaxy and continuous vapour deposition It also describes the instruments used in these experiments, such as mass spectrometers and chromatography columns and their outputs.

:Domain: Chemistry
:Category: Chemistry
:Current Version:
:Last Updated: 2022-04-19
:Producer:
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `ChMO Homepage <https://github.com/rsc-ontologies/rsc-cmo>`_
:Documentation: `ChMO Documentation <https://github.com/rsc-ontologies/rsc-cmo>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 24075
    - **Root Nodes**: 3100
    - **Leaf Nodes**: 17250
    - **Maximum Depth**: 18
    - **Edges**: 44,651

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 4268
    - **Non-taxonomic Relations**: 216
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import ChMO

   # Initialize and load ontology
   chmo = ChMO()
   chmo.load("path/to/ontology.owl")
   # Extract datasets
   data = chmo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
