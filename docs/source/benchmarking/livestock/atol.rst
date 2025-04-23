Animal Trait Ontology for Livestock (ATOL)
==========================

Overview
--------
ATOL (Animal Trait Ontology for Livestock) is an ontology of characteristics defining phenotypes of livestock
in their environment (EOL). ATOL aims to:
- provide a reference ontology of phenotypic traits of farm animals for the international scientific and educational
- communities, farmers, etc.;
- deliver this reference ontology in a language which can be used by computers in order to support database management,
semantic analysis and modeling;
- represent traits as generic as possible for livestock vertebrates;
- make the ATOL ontology as operational as possible and closely related to measurement techniques;
- structure the ontology in relation to animal production.

:Domain: Livestock
:Category: Animal Science
:Current Version: 6.0
:Last Updated: May 11, 2020
:Creator: INRAE, France
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `Animal Trait Ontology for Livestock (ATOL) Homepage <https://bioportal.bioontology.org/ontologies/ATOL>`_

Graph Metrics
-------------
    - **Total Nodes**: 8220
    - **Total Edges**: 52090
    - **Root Nodes**: 12
    - **Leaf Nodes**: 5868

Knowledge coverage
------------------
    - Classes: 2352
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 7
    - **Minimum Depth**: 0
    - **Average Depth**: 2.30
    - **Depth Variance**: 2.58

Breadth metrics
------------------
    - **Maximum Breadth**: 38
    - **Minimum Breadth**: 2
    - **Average Breadth**: 16.12
    - **Breadth Variance**: 137.86

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2628
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import ATOL

    # Initialize and load ontology
    ontology = ATOL()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
