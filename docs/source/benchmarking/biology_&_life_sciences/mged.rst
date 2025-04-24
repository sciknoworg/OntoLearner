MGED Ontology (MGED)
========================================================================================================================

Overview
--------
An ontology for microarray experiments in support of MAGE v.1. Concepts, definitions, terms,
and resources for standardized description of a microarray experiment in support of MAGE v.1.
The MGED ontology is divided into the MGED Core ontology which is intended to be stable and
in synch with MAGE v.1; and the MGED Extended ontology which adds further associations
and classes not found in MAGE v.1

:Domain: Biology & Life Sciences
:Category: Domain Ontology
:Current Version: 1.3.1.1
:Last Updated: Feb. 9, 2007
:Creator: Chris Stoeckert, Helen Parkinson, Trish Whetzel, Paul Spellman, Catherine A. Ball, Joseph White, John Matese, Liju Fan, Gilberto Fragoso, Mervi Heiskanen, Susanna Sansone, Helen Causton, Laurence Game, Chris Taylor
:License: Creative Commons 4.0
:Format: OWL
:Download: `MGED Ontology (MGED) Homepage <https://mged.sourceforge.net/ontologies/MGEDontology.php/>`_

Graph Metrics
-------------
    - **Total Nodes**: 3427
    - **Total Edges**: 5101
    - **Root Nodes**: 730
    - **Leaf Nodes**: 2171

Knowledge coverage
------------------
    - Classes: 233
    - Individuals: 681
    - Properties: 121

Hierarchical metrics
--------------------
    - **Maximum Depth**: 11
    - **Minimum Depth**: 0
    - **Average Depth**: 1.38
    - **Depth Variance**: 2.09

Breadth metrics
------------------
    - **Maximum Breadth**: 1771
    - **Minimum Breadth**: 1
    - **Average Breadth**: 282.92
    - **Breadth Variance**: 244751.41

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 744
    - **Taxonomic Relations**: 1536
    - **Non-taxonomic Relations**: 6
    - **Average Terms per Type**: 7.83

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MGED

    # Initialize and load ontology
    ontology = MGED()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
