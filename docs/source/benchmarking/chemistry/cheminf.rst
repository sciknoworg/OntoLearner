Chemical information ontology (CHEMINF)
========================================

Overview
-----------------
The chemical information ontology (cheminf) describes information entities about chemical entities.
It provides qualitative and quantitative attributes to richly describe chemicals.
Includes terms for the descriptors commonly used in cheminformatics software applications
and the algorithms which generate them.

:Domain: Chemistry
:Category: Chemistry
:Current Version: 2.1.0
:Last Updated:
:Producer: Egon Willighagen, Nina Jeliazkova, Ola Spjuth, Valery Tkachenko
:License: Creative Commons 1.0
:Format: OWL
:Download:`CHEMINF Ontology <https://terminology.tib.eu/ts/ontologies/CHEMINF>`_
:Documentation: `CHEMINF Documentation <https://terminology.tib.eu/ts/ontologies/CHEMINF>`_

Base Metrics
---------------
    - Classes: 928
    - Individuals: 20
    - Properties: 277

Graph Metrics:
------------------
    - **Nodes**: 1467
    - **Root Nodes**: 213
    - **Leaf Nodes**: 435
    - **Maximum Depth**: 16
    - **Edges**: 2837

Dataset Statistics
-------------------
Generated Benchmarks:
    * **Term Types**: 0
    * **Taxonomic Relations**: 594
    * **Non-taxonomic Relations**: 10
    * **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.cheminf import CheminfOntology

    # Initialize and load ontology
    cheminf = CheminfOntology()
    # Load ontology from file
    cheminf.load("path/to/cheminf-ontology.owl")
    # Extract datasets
    data = cheminf.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
