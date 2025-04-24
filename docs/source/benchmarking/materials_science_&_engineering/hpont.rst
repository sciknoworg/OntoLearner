The Heat Pump Ontology (HPOnt)
========================================================================================================================

Overview
--------
The Heat Pump Ontology (HPOnt) aims to formalize and represent all the relevant information of Heat Pumps.
The HPOnt has been developed as part of the REACT project which has received funding
from the European Union’s Horizon 2020 research and innovation programme under grant agreement no. 824395.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.2
:Last Updated: None
:Creator: REACT project team
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `The Heat Pump Ontology (HPOnt) Homepage <https://react2020.github.io/REACT-ONTOLOGY/HPOnt/index-en.html/>`_

Graph Metrics
-------------
    - **Total Nodes**: 84
    - **Total Edges**: 143
    - **Root Nodes**: 16
    - **Leaf Nodes**: 43

Knowledge coverage
------------------
    - Classes: 4
    - Individuals: 6
    - Properties: 12

Hierarchical metrics
--------------------
    - **Maximum Depth**: 4
    - **Minimum Depth**: 0
    - **Average Depth**: 1.13
    - **Depth Variance**: 1.98

Breadth metrics
------------------
    - **Maximum Breadth**: 16
    - **Minimum Breadth**: 2
    - **Average Breadth**: 6.00
    - **Breadth Variance**: 27.20

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 5
    - **Taxonomic Relations**: 4
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 2.50

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import HPOnt

    # Initialize and load ontology
    ontology = HPOnt()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
