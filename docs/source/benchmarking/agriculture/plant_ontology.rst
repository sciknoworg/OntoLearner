Plant Ontology (PO)
===================

Overview
-----------------
The Plant Ontology (PO) is a structured vocabulary and database resource that links plant anatomy,
morphology and growth and development to plant genomics data.

:Domain: Biology, Life Sciences
:Category: Plant Anatomy, Morphology, Growth and Development
:Current Version:
:Last Updated:
:Producer:
:License: Creative Commons 4.0
:Format: owl, ttl, csv, nt
:Download:`Plant Ontology <https://github.com/Planteome/plant-ontology>`_
:Documentation: `Plant Ontology <https://github.com/Planteome/plant-ontology>`_

Base Metrics
---------------
    - Classes:
    - Properties:
    - Annotation Assertions:

Graph Metrics:
------------------
    - **Nodes**: 2191
    - **Root Nodes**: 1316
    - **Leaf Nodes**: 343
    - **Maximum Depth**: 11
    - **Edges**: 5242

Dataset Statistics
-------------------
Generated Benchmarks:
    * **Term Types**: 0
    * **Taxonomic Relations**: 2848
    * **Non-taxonomic Relations**: 36
    * **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.plant import PlantOntology

    # Initialize and load ontology
    plant = PlantOntology()
    # Load ontology from file
    plant.load("path/to/plant-ontology.owl")
    # Extract datasets
    data = plant.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
