Planar Defects Ontology (PLDO)
===============================

Overview
-----------------
PLDO is an ontology designed to describe planar defects in crystalline materials,
such as grain boundaries and stacking faults, with a focus on their atomic-scale structure and properties.

:Domain: Materials Science and Engineering
:Category: Materials Defects
:Current Version: 1.0.0
:Last Updated:
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `PLDO Homepage <https://github.com/OCDO/pldo>`_
:Documentation: `PLDO Documentation <https://github.com/OCDO/pldo>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 215
    - **Root Nodes**: 38
    - **Leaf Nodes**: 121
    - **Maximum Depth**: 2
    - **Edges**: 320

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 38
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import PLDO

    # Initialize and load ontology
    ontology = PLDO()
    ontology.load("path/to/pldo.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
