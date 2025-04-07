EMMO-based ontology for microstructures (MicroStructures)
=========================================================

Overview
-----------------
This is intended to be a domain ontology for metallic microstructures, covering aspects like: composition,
particles, both stable (primary) and metastable (precipitates), grains, subgrains,
grain boundaries & particle free zones (PFZs), texture, dislocations. The aim is to support
both microstructure modelling as well as characterisation.

:Domain: Materials Science & Engineering
:Category: Microstructure
:Current Version:
:Last Updated:
:Producer:
:License:
:Format: OWL/XML
:Download: `MicroStructures Homepage <https://github.com/jesper-friis/emmo-microstructure>`_
:Documentation: `MicroStructures Documentation <https://github.com/jesper-friis/emmo-microstructure>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 115
    - **Root Nodes**: 1
    - **Leaf Nodes**: 37
    - **Maximum Depth**: 1
    - **Edges**: 287

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 364
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import MicroStructures

    # Initialize and load ontology
    ontology = MicroStructures()
    ontology.load("path/to/ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
