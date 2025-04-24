Biological Pathways Exchange (BioPAX)
========================================================================================================================

Overview
--------
BioPAX is a standard language that aims to enable integration, exchange, visualization and analysis
of biological pathway data. Specifically, BioPAX supports data exchange between pathway data
groups and thus reduces the complexity of interchange between data formats by providing an
accepted standard format for pathway data.

:Domain: Biology & Life Sciences
:Category: Bioinformatics
:Current Version: 1.0
:Last Updated: 16 April 2015
:Creator: None
:License: None
:Format: OWL
:Download: `Biological Pathways Exchange (BioPAX) Homepage <http://www.biopax.org/>`_

Graph Metrics
-------------
    - **Total Nodes**: 555
    - **Total Edges**: 1611
    - **Root Nodes**: 68
    - **Leaf Nodes**: 200

Knowledge coverage
------------------
    - Classes: 92
    - Individuals: 0
    - Properties: 96

Hierarchical metrics
--------------------
    - **Maximum Depth**: 15
    - **Minimum Depth**: 0
    - **Average Depth**: 2.70
    - **Depth Variance**: 6.33

Breadth metrics
------------------
    - **Maximum Breadth**: 138
    - **Minimum Breadth**: 1
    - **Average Breadth**: 34.50
    - **Breadth Variance**: 1919.38

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 292
    - **Non-taxonomic Relations**: 446
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BioPAX

    # Initialize and load ontology
    ontology = BioPAX()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
