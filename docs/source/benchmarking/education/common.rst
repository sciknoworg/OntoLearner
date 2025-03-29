Ontology for the representation of commons elements in the Trias ontology
===========================================================================

Overview
-----------------
OSCCA is a computer course architectural ontology system for associating computer learners to select and explore
a set of appropriate courses and curriculums. An ontology is used for defining relationships between items
in order to assist the user to find their interesting knowledge points

:Domain: Education
:Category: Computer Science
:Current Version: 0.1.0
:Last Updated:
:Producer: Jhon Toledo, Miguel Angel García, Oscar Corcho
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: RDF/XML
:Download: `Common Ontology Homepage <https://w3id.org/mobility/trias/common/0.1.0>`_
:Documentation: `Common Ontology Documentation <https://w3id.org/mobility/trias/common/0.1.0>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 67
    - **Root Nodes**: 8
    - **Leaf Nodes**: 30
    - **Maximum Depth**: 1
    - **Edges**: 131

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 26
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import Common

    # Initialize and load ontology
    ontology = Common()
    ontology.load("data/ontologies/new/common.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
