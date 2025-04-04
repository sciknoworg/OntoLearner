Material Properties Ontology (MAT)
==================================

Overview
-----------------
The Material Properties Ontology aims to provide the vocabulary to describe the building components,
materials, and their corresponding properties, relevant within the construction industry. More specifically,
the building elements and properties covered in this ontology support applications
focused on the design of building renovation projects.

:Domain: Materials Science and Engineering
:Category: Materials Properties
:Current Version: 0.0.8
:Last Updated:
:Creator: María Poveda-Villalón, Serge Chávez-Feria
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: RDF/XML, TTL, N-Triples
:Download: `MAT Homepage <https://bimerr.iot.linkeddata.es/def/material-properties/>`_
:Documentation: `MAT Documentation <https://bimerr.iot.linkeddata.es/def/material-properties/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 263
    - **Root Nodes**: 7
    - **Leaf Nodes**: 52
    - **Maximum Depth**: {12
    - **Edges**: 691

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 323
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import MAT

    # Initialize and load ontology
    ontology = MAT()
    ontology.load("path/to/mat.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
