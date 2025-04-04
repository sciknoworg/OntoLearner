Laser Powder Bed Fusion Ontology (LPBFO)
========================================

Overview
-----------------
The LPBF Ontology can be used to describe the additive manufacturing of a component via
Laser Powder Bed Fusion (LPBF) / Selective Laser Melting (SLM). The ontology builds on BFO2.0
and BWMD_mid and has been developed to be used in conjunction with the digital workflows provided
by Fraunhofer IWM. If possible, the terminology within this ontology was used as provided by ISO/ASTM 52900:2015.
Recently, classes relevant for Life Cycle Analysis (LCA) were added that enable sustainability assessment.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: v1.1.9
:Last Updated: 2022-09-20
:Producer: Fraunhofer IWM
:License: `CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/legalcode>`_
:Format: OWL, RDF/XML, Turtle
:Download: `LPBFO Homepage <https://matportal.org/ontologies/LPBFO>`_
:Documentation: `LPBFO Documentation <https://matportal.org/ontologies/LPBFO>`_

Base Metrics
---------------
    - Classes: 509
    - Individuals: 0
    - Properties: 40

Graph Metrics
------------------
    - **Total Nodes**: 1835
    - **Root Nodes**: 129
    - **Leaf Nodes**: 1056
    - **Maximum Depth**: 90
    - **Edges**: 3548

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 507
    - **Non-taxonomic Relations**: 22
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import LPBFO

    # Initialize and load ontology
    ontology = LPBFO()
    ontology.load("path/to/ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
