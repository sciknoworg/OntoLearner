Molecules And Materials Basic Ontology (MAMBO)
========================================================================================================================

Overview
--------
MAMBO (Molecules And Materials Basic Ontology) is a domain ontology for molecular materials.
Its main targets are: Allowing the retrieval of structured information regarding molecular materials
and related applications (i.e. devices based on molecular materials) Supporting the development of new,
complex workflows for modelling systems based on molecular materials (computational modelling
and data-driven techniques) Integrating data generated via computational simulations and empirical experiments.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: None
:Last Updated: None
:Creator: None
:License: General Public License v3.0 (GPL-3.0)
:Format: OWL, TTL
:Download: `Molecules And Materials Basic Ontology (MAMBO) Homepage <https://github.com/daimoners/MAMBO>`_

Graph Metrics
-------------
    - **Total Nodes**: 166
    - **Total Edges**: 624
    - **Root Nodes**: 1
    - **Leaf Nodes**: 7

Knowledge coverage
------------------
    - Classes: 57
    - Individuals: 0
    - Properties: 104

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.50
    - **Depth Variance**: 0.25

Breadth metrics
------------------
    - **Maximum Breadth**: 1
    - **Minimum Breadth**: 1
    - **Average Breadth**: 1.00
    - **Breadth Variance**: 0.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 39
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MAMBO

    # Initialize and load ontology
    ontology = MAMBO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
