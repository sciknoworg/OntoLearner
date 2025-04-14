Tribological Artificial Intelligence (TribAIn) Ontology
========================================================

Overview
-----------------
The tribAIn1 ontology aims to formalize knowledge gained from tribological experiments for reuse,
comparison and documentation. Therefore, the tribAin ontology provides concepts for the specification
of methodological background knowledge of experimental design, the documentation of the experimental setup
and the representation of different kinds of results (e.g. measurements series, analysis,
interpretation in natural-language). Using the EXPO2 (ontology of scientific experiments) as basis,
gives tribAIn a generic background about scientific experimental design, methodology and results representation.

:Domain: Scholarly Knowledge
:Category: Scholarly Knowledge
:Current Version:
:Last Updated:
:Creator: Patricia Kügler
:License: `Creative Commons 4.0 <https://creativecommons.org/licenses/by/4.0/>`_
:Format: TTL
:Download: `TribAIn Homepage <https://github.com/snow0815/tribAIn>`_
:Documentation: `TribAIn Documentation <https://github.com/snow0815/tribAIn>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 771
    - **Root Nodes**: 163
    - **Leaf Nodes**: 279
    - **Maximum Depth**: 21
    - **Edges**: 1723

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 21
    - **Taxonomic Relations**: 488
    - **Non-taxonomic Relations**: 24
    - **Average Terms per Type**: 0.70

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import TribAIn

    # Initialize and load ontology
    ontology = TribAIn()
    ontology.load("path/to/tribain.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
