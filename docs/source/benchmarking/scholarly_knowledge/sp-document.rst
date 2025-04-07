SMART Protocols Ontology: Document Module (SP-Document)
========================================================

Overview
-----------------
SMART Protocols Ontology: Document Module is an ontology designed
to represent metadata used to report an experimental protocol.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 4.0
:Last Updated: 2013-07-01
:Creator: http://oxgiraldo.wordpress.com
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL/XML
:Download: `SP-Document Homepage <https://github.com/SMARTProtocols/SMART-Protocols>`_
:Documentation: `SP-Document Documentation <https://github.com/SMARTProtocols/SMART-Protocols>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 1489
    - **Root Nodes**: 18
    - **Leaf Nodes**: 908
    - **Maximum Depth**: 18
    - **Edges**: 3044

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 45
    - **Taxonomic Relations**: 1194
    - **Non-taxonomic Relations**: 74
    - **Average Terms per Type**: 1.88

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import SPDocument

    # Initialize and load ontology
    ontology = SPDocument()
    ontology.load("path/to/sp-document.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
