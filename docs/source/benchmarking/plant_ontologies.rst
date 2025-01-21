Plant Ontology (PO)
==================

Overview
-----------------
The Plant Ontology (PO) is a structured vocabulary and database resource that links plant anatomy,
morphology and growth and development to plant genomics data.

Ontology Statistics
------------------
Current statistics from PO:

* **Term Types**: 1,827
* **Taxonomic Relations**: Pending
* **Non-taxonomic Relations**: Pending
* **Average Terms per Type**: 456.75

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.plant import PlantOntology

    # Initialize and load ontology
    plant = PlantOntology()

    plant.load("path/to/plant-ontology.owl")

    # Extract datasets
    data = plant.extract()
