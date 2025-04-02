Domain ontology for atomistic and electronic modelling (Atomistic)
==================================================================

Overview
-----------------
An EMMO-based domain ontology for atomistic and electronic modelling.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.0.2
:Last Updated:
:Producer: Francesca L. Bleken, Jesper Friis
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: Turtle
:Download: `Atomistic Homepage <https://github.com/emmo-repo/domain-atomistic>`_
:Documentation: `Atomistic Documentation <https://github.com/emmo-repo/domain-atomistic>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 93
    - **Root Nodes**: 11
    - **Leaf Nodes**: 70
    - **Maximum Depth**: 7
    - **Edges**: 107

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
    from ontolearner.ontology import Atomistic

    # Initialize and load ontology
    ontology = Atomistic()
    ontology.load("path/to/atomistic.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
