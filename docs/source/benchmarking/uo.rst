Unit Ontology (UO) - An ontology of units of measurements
=========================================================

Overview
-----------------
Metrical units for use in conjunction with PATO

:Domain: Material Science and Engineering
:Category: Material Science and Engineering
:Current Version:
:Last Updated: 2023-05-25
:Producer: KAUST
:License: Creative Commons 3.0
:Format: owl
:Download:`UO Ontology <https://bioportal.bioontology.org/ontologies/UO>`_
:Documentation: `UO Documentation <https://bioportal.bioontology.org/ontologies/UO>`_

Base Metrics
---------------
    - Classes: 572
    - Properties: 4
    - Individuals: 275

Graph Metrics:
------------------
    - **Nodes**: 2284
    - **Root Nodes**: 6
    - **Leaf Nodes**: 754
    - **Maximum Depth**: 4
    - **Edges**: 5354

Dataset Statistics
------------------
Generated Benchmarks:
    * **Term Types**: 0
    * **Taxonomic Relations**: 880
    * **Non-taxonomic Relations**: 356
    * **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.uo import UoOntology

    # Initialize and load ontology
    uo = UoOntology()
    # Load ontology from file
    uo.load("path/to/uo-ontology.owl")
    # Extract datasets
    data = uo.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
