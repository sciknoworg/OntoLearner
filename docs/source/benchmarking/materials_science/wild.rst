Workflows in Linked Data (WiLD)
===============================

Overview
-----------------
Ontology to describe Workflows in Linked Data

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version:
:Last Updated: 2020-06-10
:Creator: Tobias Käfer
:License: DBpedia License
:Format: TTL
:Download: `WiLD Homepage <https://databus.dbpedia.org/ontologies/purl.org/wild--vocab/2020.06.10-210552>`_
:Documentation: `WiLD Documentation <https://databus.dbpedia.org/ontologies/purl.org/wild--vocab/2020.06.10-210552>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 50
    - **Root Nodes**: 21
    - **Leaf Nodes**: 9
    - **Maximum Depth**: 2
    - **Edges**: 91

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 4
    - **Taxonomic Relations**: 9
    - **Non-taxonomic Relations**: 4
    - **Average Terms per Type**: 0.24

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import WiLD

    # Initialize and load ontology
    ontology = WiLD()
    ontology.load("path/to/wild.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
