Characterisation Methodology Domain Ontology (CHAMEO)
========================================================================================================================

Overview
--------
An ontology for materials characterization which represents the evolution of the CHADA template
in an ontological form, allowing to generate FAIR documentation of Characterisation Experiments
and that has been used as a basis for the development of a number of technique-specific
or application-specific ontologies in the materials characterisation domain. CHAMEO
has been used as a foundation for the definition of the new CHADA template during the CWA.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 1.0.0
:Last Updated: 2024-04-12
:Creator: https://orcid.org/0000-0002-4181-2852, https://orcid.org/0000-0002-5174-8508, https://orcid.org/0000-0002-9668-6961
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `Characterisation Methodology Domain Ontology (CHAMEO) Homepage <https://github.com/emmo-repo/domain-characterisation-methodology>`_

Graph Metrics
-------------
    - **Total Nodes**: 802
    - **Total Edges**: 1526
    - **Root Nodes**: 29
    - **Leaf Nodes**: 459

Knowledge coverage
------------------
    - Classes: 203
    - Individuals: 0
    - Properties: 52

Hierarchical metrics
--------------------
    - **Maximum Depth**: 12
    - **Minimum Depth**: 0
    - **Average Depth**: 4.25
    - **Depth Variance**: 8.29

Breadth metrics
------------------
    - **Maximum Breadth**: 45
    - **Minimum Breadth**: 2
    - **Average Breadth**: 19.92
    - **Breadth Variance**: 154.69

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 397
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import CHAMEO

    # Initialize and load ontology
    ontology = CHAMEO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
