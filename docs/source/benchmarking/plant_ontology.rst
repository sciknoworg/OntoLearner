Plant Ontology (PO)
==================

Overview
-----------------
The Plant Ontology (PO) is a structured vocabulary and database resource that links plant anatomy,
morphology and growth and development to plant genomics data.

Basic Information
-----------------
:Domain: Life Sciences, Biology
:Current Version:
:Last Updated Date:
:Producer:
:License: Creative Commons 4.0
:Format: owl, ttl, csv, nt
:Download:`Plant Ontology <https://github.com/Planteome/plant-ontology>`_
:Documentation:

Ontology Statistics
------------------
Graph Metrics:
    - **Total Triples**:
    - **Nodes**:
    - **Edges**:

Hierarchical Structure:
    - **Maximum Depth**:
    - **Root Nodes**:
    - **Leaf Nodes**:

Dataset Statistics
------------------
Generated Benchmarks:
    * **Term Types**: 1,827
    * **Taxonomic Relations**:
    * **Non-taxonomic Relations**:
    * **Average Terms per Type**: 456.75

Relationship Types
----------------
Taxonomic Relations:

Non-taxonomic Relations:

Alignments
-----------------

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.plant import PlantOntology

    # Initialize and load ontology
    plant = PlantOntology()

    plant.load("path/to/plant-ontology.owl")

    # Extract datasets
    data = plant.extract()
