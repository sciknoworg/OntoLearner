NFDI MatWerk Ontology (MatWerk)
==============================================================================

Overview
--------
NFDI-MatWerk aims to establish a digital infrastructure for Materials Science and Engineering (MSE),
fostering improved data sharing and collaboration. This repository provides comprehensive documentation
for NFDI MatWerk Ontology (MWO) v3.0, a foundational framework designed to structure research data
and enhance interoperability within the MSE community. To ensure compliance with top-level ontology standards,
MWO v3.0 is aligned with the Basic Formal Ontology (BFO) and incorporates the modular approach
of the NFDIcore mid-level ontology, enriching metadata through standardized classes and properties.
The MWO addresses key aspects of MSE research data, including the NFDI-MatWerk community structure,
covering task areas, infrastructure use cases, projects, researchers, and organizations.
It also describes essential NFDI resources, such as software, workflows, ontologies, publications,
datasets, metadata schemas, instruments, facilities, and educational materials. Additionally,
MWO represents NFDI-MatWerk services, academic events, courses, and international collaborations.
As the foundation for the MSE Knowledge Graph, MWO facilitates efficient data integration and retrieval,
promoting collaboration and knowledge representation across MSE domains. This digital transformation
enhances data discoverability, reusability, and accelerates scientific exchange, innovation,
and discoveries by optimizing research data management and accessibility.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 3.0.0
:Last Updated: 2024-01-30
:Creator: Hossein Beygi Nasrabadi, Jörg Waitelonis, Ebrahim Norouzi, Kostiantyn Hubaiev, Harald Sack
:License: Creative Commons 4.0
:Format: OWL, TTL
:Download: `NFDI MatWerk Ontology (MatWerk) Homepage <https://github.com/ISE-FIZKarlsruhe/mwo?tab=readme-ov-file>`_

Graph Metrics
-------------
    - **Total Nodes**: 2554
    - **Total Edges**: 4870
    - **Root Nodes**: 86
    - **Leaf Nodes**: 1384

Knowledge coverage
------------------
    - Classes: 449
    - Individuals: 29
    - Properties: 129

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 2.83
    - **Depth Variance**: 5.95

Breadth metrics
------------------
    - **Maximum Breadth**: 148
    - **Minimum Breadth**: 1
    - **Average Breadth**: 40.00
    - **Breadth Variance**: 1814.14

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 29
    - **Taxonomic Relations**: 562
    - **Non-taxonomic Relations**: 12
    - **Average Terms per Type**: 4.14

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MatWerk

    # Initialize and load ontology
    ontology = MatWerk()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
