Atomistic Simulation Methods Ontology (ASMO)
===================

Overview
-----------------
ASMO is an ontology that aims to define the concepts needed to describe commonly
used atomic scale simulation methods, i.e. density functional theory, molecular dynamics,
Monte Carlo methods, etc. ASMO uses the Provenance Ontology (PROV-O) to describe the simulation process.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 1.0.0
:Last Updated:
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `ASMO Homepage <https://github.com/OCDO/asmo?tab=readme-ov-file#atomistic-simulation-methods-ontology-asmo>`_
:Documentation: `ASMO Documentation <https://github.com/OCDO/asmo?tab=readme-ov-file#atomistic-simulation-methods-ontology-asmo>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 588
    - **Root Nodes**: 23
    - **Leaf Nodes**: 360
    - **Maximum Depth**: 6
    - **Edges**: 1058

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 30
    - **Taxonomic Relations**: 99
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0.94

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import ASMO

    # Initialize and load ontology
    ontology = ASMO()
    ontology.load("path/to/asmo.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
