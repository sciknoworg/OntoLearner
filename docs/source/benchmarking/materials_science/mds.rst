Materials Data Science Ontology (MDS)
=====================================

Overview
-----------------
Materials Data Science(MDS) is an ontology encompassing multiple domains relevant to materials science,
chemical synthesis and characterizations, photovoltaics and geospatial datasets. The terms used for classes,
subclasses and instances are mapped to PMDCo and BFO Ontologies.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 0.3.0.0
:Last Updated: 03/24/2024
:Producer: SDLE Research Center
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL/XML
:Download: `MDS Homepage <https://matportal.org/ontologies/MDS>`_
:Documentation: `MDS Documentation <https://matportal.org/ontologies/MDS>`_

Base Metrics
---------------
    - Classes: 256
    - Individuals: 0
    - Properties: 12

Graph Metrics
------------------
    - **Total Nodes**: 657
    - **Root Nodes**: 63
    - **Leaf Nodes**: 303
    - **Maximum Depth**: 3
    - **Edges**: 1457

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 351
    - **Non-taxonomic Relations**: 128
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import MDS

    # Initialize and load ontology
    ontology = MDS()
    ontology.load("path/to/mds.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
