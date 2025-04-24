National Research Data Infrastructure Ontology (NFDIcore)
========================================================================================================================

Overview
--------
The National Research Data Infrastructure (NFDI) initiative has led to the formation of various consortia,
each focused on developing a research data infrastructure tailored to its specific domain.
To ensure interoperability across these consortia, the NFDIcore ontology has been developed
as a mid-level ontology for representing metadata related to NFDI resources, including individuals,
organizations, projects, data portals, and more.

:Domain: Scholarly Knowledge
:Category: Research Data Infrastructure
:Current Version: 3.0.0
:Last Updated: 2025-02-07
:Creator: Jörg Waitelonis, Oleksandra Bruns, Tabea Tietz, Etienne Posthumus, Hossein Beygi Nasrabadi, Harald Sack
:License: Creative Commons 1.0
:Format: RDF/XML, TTL, JSON-LD
:Download: `National Research Data Infrastructure Ontology (NFDIcore) Homepage <https://ise-fizkarlsruhe.github.io/nfdicore/>`_

Graph Metrics
-------------
    - **Total Nodes**: 1849
    - **Total Edges**: 3525
    - **Root Nodes**: 84
    - **Leaf Nodes**: 1029

Knowledge coverage
------------------
    - Classes: 302
    - Individuals: 0
    - Properties: 102

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 2.85
    - **Depth Variance**: 5.97

Breadth metrics
------------------
    - **Maximum Breadth**: 145
    - **Minimum Breadth**: 1
    - **Average Breadth**: 39.29
    - **Breadth Variance**: 1732.49

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 391
    - **Non-taxonomic Relations**: 10
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import NFDIcore

    # Initialize and load ontology
    ontology = NFDIcore()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
