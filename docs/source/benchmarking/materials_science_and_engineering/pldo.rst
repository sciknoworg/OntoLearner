Planar Defects Ontology (PLDO)
========================================================================================================================

Overview
--------
PLDO is an ontology designed to describe planar defects in crystalline materials,
such as grain boundaries and stacking faults, with a focus on their atomic-scale structure and properties.

:Domain: Materials Science and Engineering
:Category: Materials Defects
:Current Version: 1.0.0
:Last Updated: None
:Creator: https://orcid.org/0000-0001-7564-7990
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL
:Download: `Planar Defects Ontology (PLDO) Homepage <https://github.com/OCDO/pldo>`_

Graph Metrics
-------------
    - **Total Nodes**: 215
    - **Total Edges**: 320
    - **Root Nodes**: 38
    - **Leaf Nodes**: 121

Knowledge coverage
------------------
    - Classes: 27
    - Individuals: 0
    - Properties: 15

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.57
    - **Depth Variance**: 0.40

Breadth metrics
------------------
    - **Maximum Breadth**: 38
    - **Minimum Breadth**: 6
    - **Average Breadth**: 25.00
    - **Breadth Variance**: 188.67

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 38
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PLDO

    # Initialize and load ontology
    ontology = PLDO()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
