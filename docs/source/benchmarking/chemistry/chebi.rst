Chemical Entities of Biological Interest (ChEBI)
========================================================================================================================

Overview
--------
Chemical Entities of Biological Interest (ChEBI) is a dictionary of molecular entities
focused on ‘small’ chemical compounds. The term ‘molecular entity’ refers to any constitutionally
or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer, etc.,
identifiable as a separately distinguishable entity. The molecular entities in question
are either products of nature or synthetic products used to intervene in the processes of living organisms.
ChEBI incorporates an ontological classification, whereby the relationships between molecular entities
or classes of entities and their parents and/or children are specified.

:Domain: Chemistry
:Category: Chemical Entities
:Current Version: 239
:Last Updated: 01/01/2025
:Creator: None
:License: Creative Commons 4.0
:Format: OWL, OBO, JSON
:Download: `Chemical Entities of Biological Interest (ChEBI) Homepage <https://www.ebi.ac.uk/chebi/>`_

Graph Metrics
-------------
    - **Total Nodes**: 2433610
    - **Total Edges**: 6913389
    - **Root Nodes**: 609907
    - **Leaf Nodes**: 1528418

Knowledge coverage
------------------
    - Classes: 220816
    - Individuals: 0
    - Properties: 10

Hierarchical metrics
--------------------
    - **Maximum Depth**: 6
    - **Minimum Depth**: 0
    - **Average Depth**: 1.14
    - **Depth Variance**: 0.69

Breadth metrics
------------------
    - **Maximum Breadth**: 908127
    - **Minimum Breadth**: 26
    - **Average Breadth**: 310545.00
    - **Breadth Variance**: 135103408992.57

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 1200620
    - **Non-taxonomic Relations**: 18607
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import ChEBI

    # Initialize and load ontology
    ontology = ChEBI()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
