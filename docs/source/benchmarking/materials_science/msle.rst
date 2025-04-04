Material Science Lab Equipment Ontology (MSLE)
===============================================

Overview
-----------------
The current ontology describes Material Science Lab Equipment

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 1.1
:Last Updated: Sep 15, 2022
:Creator:
:License:
:Format: TTL
:Download: `MSLE Homepage <https://github.com/MehrdadJalali-AI/MSLE-Ontology>`_
:Documentation: `MSLE Documentation <https://github.com/MehrdadJalali-AI/MSLE-Ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 146
    - **Root Nodes**: 16
    - **Leaf Nodes**: 52
    - **Maximum Depth**: 9
    - **Edges**: 479

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 4
    - **Taxonomic Relations**: 83
    - **Non-taxonomic Relations**: 229
    - **Average Terms per Type**: 0.15

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import MSLE

    # Initialize and load ontology
    ontology = MSLE()
    ontology.load("path/to/msle.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
