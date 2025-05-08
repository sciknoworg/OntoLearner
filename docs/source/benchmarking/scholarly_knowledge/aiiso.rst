Academic Institution Internal Structure Ontology (AIISO)
========================================================================================================================

Overview
--------
The Academic Institution Internal Structure Ontology (AIISO) provides classes and properties
to describe the internal organizational structure of an academic institution. AIISO is designed to work
in partnership with Participation (http://purl.org/vocab/participation/schema),
FOAF (http://xmlns.com/foaf/0.1/) and aiiso-roles (http://purl.org/vocab/aiiso-roles/schema)
to describe the roles that people play within an institution.

:Domain: Scholarly Knowledge
:Category: Academic Institution
:Current Version: 1.0
:Last Updated: 2008-05-14
:Creator: Open University
:License: Creative Commons 4.0
:Format: RDF
:Download: `Academic Institution Internal Structure Ontology (AIISO) Homepage <https://vocab.org/aiiso/>`_

Graph Metrics
-------------
    - **Total Nodes**: 119
    - **Total Edges**: 247
    - **Root Nodes**: 8
    - **Leaf Nodes**: 54

Knowledge coverage
------------------
    - Classes: 22
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 2
    - **Minimum Depth**: 0
    - **Average Depth**: 0.89
    - **Depth Variance**: 0.47

Breadth metrics
------------------
    - **Maximum Breadth**: 14
    - **Minimum Breadth**: 5
    - **Average Breadth**: 9.00
    - **Breadth Variance**: 14.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 13
    - **Non-taxonomic Relations**: 3
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import AIISO

    # Initialize and load ontology
    ontology = AIISO()
    ontology.load("path/to/ontology.RDF")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
