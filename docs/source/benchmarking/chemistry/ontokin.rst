Ontology for Chemical Kinetic Reaction Mechanisms
=================================================

Overview
-----------------
OntoKin is an ontology developed for representing chemical kinetic reaction mechanisms.

:Domain: Chemistry
:Category: Chemistry
:Current Version: 1.0
:Last Updated: 08 February 2022
:Producer: IEEE
:License: Creative Commons 4.0
:Format: OWL
:Download: `OntoKin Homepage <https://www.ontologyportal.org/>`_
:Documentation: `OntoKin Documentation <https://www.ontologyportal.org/>`_

Base Metrics
---------------
    - Classes: 58
    - Properties: 136
    - Individuals: 0

Graph Metrics:
------------------
    - **Nodes**: 407
    - **Root Nodes**: 122
    - **Leaf Nodes**: 103
    - **Maximum Depth**: 15
    - **Edges**: 1011

Dataset Statistics
------------------
Generated Benchmarks:
    * **Term Types**: 0
    * **Taxonomic Relations**: 138
    * **Non-taxonomic Relations**: 1
    * **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.ontokin import OntoKin

    # Initialize and load ontology
    ontokin = OntoKin()
    # Load ontology from file
    ontokin.load("path/to/ontology.owl")
    # Extract datasets
    data = ontokin.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
