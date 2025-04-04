Metadata for Engineering (M4I)
==============================

Overview
-----------------
Metadata4Ing is an ontology for describing engineering results and their corresponding workflow.
The ontology is maintained by the Metadata4Ing working group, a subgroup of the Special Interest Group (SIG)
Metadata & Ontologies within NFDI4Ing.

:Domain: Material Science and Engineering
:Category: Materials Science
:Current Version: 1.3.1
:Last Updated: 2025-03-10
:Creator: Metadata4Ing Workgroup
:License: Creative Commons 4.0
:Format: OWL, TTL
:Download: `M4I Homepage <https://git.rwth-aachen.de/nfdi4ing/metadata4ing/metadata4ing>`_
:Documentation: `M4I Documentation <https://git.rwth-aachen.de/nfdi4ing/metadata4ing/metadata4ing>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 1032
    - **Root Nodes**: 109
    - **Leaf Nodes**: 731
    - **Maximum Depth**: 12
    - **Edges**: 1517

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 47
    - **Taxonomic Relations**: 122
    - **Non-taxonomic Relations**: 6
    - **Average Terms per Type**: 2.76

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import M4I

    # Initialize and load ontology
    ontology = M4I()
    ontology.load("path/to/metadata4ing.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
