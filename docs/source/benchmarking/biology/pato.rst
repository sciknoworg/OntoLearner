The Phenotype And Trait Ontology (PATO)
=======================================

Overview
-----------------
An ontology of phenotypic qualities (properties, attributes or characteristics).

:Domain: Biology & Life Sciences
:Category: Biology
:Current Version: 1.2
:Last Updated: 2025-02-01
:Producer:
:License: Creative Commons 4.0
:Format: OWL
:Download: `PATO Ontology <https://terminology.tib.eu/ts/ontologies/PATO>`_
:Documentation: `PATO Documentation <https://terminology.tib.eu/ts/ontologies/PATO>`_

Base Metrics
---------------
    - Classes: 8602
    - Properties: 352
    - Individuals: 0

Graph Metrics:
------------------
    - **Nodes**: 98691
    - **Root Nodes**: 16564
    - **Leaf Nodes**: 45644
    - **Maximum Depth**: 6
    - **Edges**: 259386

Dataset Statistics
------------------
Generated Benchmarks:
    * **Term Types**: 0
    * **Taxonomic Relations**: 62605
    * **Non-taxonomic Relations**: 5456
    * **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.pato import PatoOntology

    # Initialize and load ontology
    pato = PatoOntology()
    # Load ontology from file
    pato.load("path/to/pato-ontology.owl")
    # Extract datasets
    data = pato.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
