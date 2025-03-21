The Phenotype And Trait Ontology (PATO)
=======================================

Overview
-----------------
An ontology of phenotypic qualities (properties, attributes or characteristics).

:Domain: Biology
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
    - **Nodes**:
    - **Root Nodes**:
    - **Leaf Nodes**:
    - **Maximum Depth**:
    - **Edges**:

Dataset Statistics
------------------
Generated Benchmarks:
    * **Term Types**:
    * **Taxonomic Relations**:
    * **Non-taxonomic Relations**:
    * **Average Terms per Type**:

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
