The BRENDA Tissue Ontology (BTO)
================================

Overview
-----------------
A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.

:Domain: Chemistry
:Category: Chemistry
:Current Version: 2021-10-26
:Last Updated: 2021-10-26
:Producer: N/A
:License: Creative Commons 4.0
:Format: owl
:Download:`BRENDA Tissue Ontology <https://terminology.tib.eu/ts/ontologies/BTO>`_
:Documentation: `BRENDA Tissue Ontology Documentation <https://terminology.tib.eu/ts/ontologies/BTO>`_

Base Metrics
---------------
    - Classes: 6569
    - Properties: 37
    - Individuals: 0

Schema Metrics
---------------
    - Attribute Richness: 0
    - Inheritance Richness: 0
    - Relationship Richness: 0

Graph Metrics:
------------------
    - **Nodes**: 37130
    - **Root Nodes**: 5619
    - **Leaf Nodes**: 21886
    - **Maximum Depth**: 24
    - **Edges**: 86188

Dataset Statistics
------------------
Generated Benchmarks:
    * **Term Types**: 0
    * **Taxonomic Relations**: 10241
    * **Non-taxonomic Relations**: 3
    * **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.bto import BTOOntology

    # Initialize and load ontology
    bto = BTOOntology()
    # Load ontology from file
    bto.load("path/to/bto.owl")
    # Extract datasets
    data = bto.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
