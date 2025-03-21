Copyright Ontology
==================

Overview
-----------------
The Copyright Ontology tries to formalise the copyright domain as a way to facilitate
automated (or computer-supported) copyright management through the whole content value chain,
as it is shaped by copyright law. Therefore, it does not focus just on the last step,
end-users permissions to consume content, like many rights languages and ontologies do.

:Domain: Copyright
:Category: Legal Knowledge
:Current Version:
:Last Updated: 2019-09
:Producer: Rhizomik
:License: Creative Commons 4.0
:Format: RDF
:Download: `Copyright Ontology Homepage <https://rhizomik.net/ontologies/copyrightonto/>`_
:Documentation: `Copyright Ontology Documentation <https://rhizomik.net/ontologies/copyrightonto/>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 218
    - **Root Nodes**: 6
    - **Leaf Nodes**: 75
    - **Maximum Depth**: 8
    - **Edges**: 470

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 7
    - **Taxonomic Relations**: 403
    - **Non-taxonomic Relations**: 7
    - **Average Terms per Type**: 2.33

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import CopyrightOnto

    # Initialize and load ontology
    copyright_onto = CopyrightOnto()
    copyright_onto.load("path/to/ontology.ttl")
    # Extract datasets
    data = copyright_onto.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
