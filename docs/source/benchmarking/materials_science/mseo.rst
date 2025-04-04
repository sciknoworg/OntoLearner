Materials Science and Engineering Ontology (MSEO)
==================================================

Overview
-----------------
MSEO utilizes the IOF Ontology stack giving materials scientists and engineers the ability
to represent their experiments and resulting data. The goal is to create machine and human readable sematic data
which can be easily digested by other science domains. It is a product of the joint venture Materials Open Lab Project
between the Bundesanstalt für Materialforschung und -prüfung (BAM) and the Fraunhofer Group MATERIALS
and uses the BWMD ontology created by Fraunhofer IWM as a starting point.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version:
:Last Updated:
:Creator: Thomas Hanke, Fraunhofer IWM
:License: MIT License
:Format: TTL, OWL
:Download: `MSEO Homepage <https://github.com/Mat-O-Lab/MSEO>`_
:Documentation: `MSEO Documentation <https://github.com/Mat-O-Lab/MSEO>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 543
    - **Root Nodes**: 12
    - **Leaf Nodes**: 396
    - **Maximum Depth**: 4
    - **Edges**: 782

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 124
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import MSEO

    # Initialize and load ontology
    ontology = MSEO()
    ontology.load("path/to/mseo.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
