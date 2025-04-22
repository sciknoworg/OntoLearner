Software Ontology (SWO)
==========================

Overview
--------
The Software Ontology (SWO) is a resource for describing software tools, their types, tasks, versions,
provenance and associated data. It contains detailed information on licensing and formats
as well as software applications themselves, mainly (but not limited) to the bioinformatics community.

:Domain: Scholarly Knowledge
:Category: Software
:Current Version: 1.0
:Last Updated: 2013-07-01
:Creator: Allyson Lister, Andy Brown, Duncan Hull, Helen Parkinson, James Malone, Jon Ison, Nandini Badarinarayan, Robert Stevens
:License: Creative Commons 4.0
:Format: OWL
:Download: `Software Ontology (SWO) Homepage <https://terminology.tib.eu/ts/ontologies/SWO>`_

Graph Metrics
-------------
    - **Total Nodes**: 11581
    - **Total Edges**: 33570
    - **Root Nodes**: 177
    - **Leaf Nodes**: 3150

Knowledge coverage
------------------
    - Classes: 2746
    - Individuals: 443
    - Properties: 165

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 3.07
    - **Depth Variance**: 5.30

Breadth metrics
------------------
    - **Maximum Breadth**: 392
    - **Minimum Breadth**: 1
    - **Average Breadth**: 132.93
    - **Breadth Variance**: 17222.21

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 444
    - **Taxonomic Relations**: 20936
    - **Non-taxonomic Relations**: 699
    - **Average Terms per Type**: 10.33

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SWO

    # Initialize and load ontology
    ontology = SWO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
