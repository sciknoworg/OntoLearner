SMART Protocols Ontology: Workflow Module (SP-Workflow)
========================================================

Overview
-----------------
SP-Workflow module represents: i) the executable  elements of a protocol; ii) the experimental actions
and material entities that participates in instructions (sample/specimen, organisms, reagents,
instruments);  and iii) the order of execution of the instructions.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 4.0
:Last Updated: 2013-07-01
:Creator: http://oxgiraldo.wordpress.com
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL/XML
:Download: `SP-Workflow Homepage <https://github.com/SMARTProtocols/SMART-Protocols>`_
:Documentation: `SP-Workflow Documentation <https://github.com/SMARTProtocols/SMART-Protocols>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 1446
    - **Root Nodes**: 4
    - **Leaf Nodes**: 834
    - **Maximum Depth**: 14
    - **Edges**: 3017

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 5
    - **Taxonomic Relations**: 1079
    - **Non-taxonomic Relations**: 24
    - **Average Terms per Type**: 0.24

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import SPWorkflow

    # Initialize and load ontology
    ontology = SPWorkflow()
    ontology.load("path/to/sp-workflow.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
