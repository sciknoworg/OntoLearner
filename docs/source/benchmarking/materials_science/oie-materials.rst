Open Innovation Environment (OIE) domain ontologies, Materials module (OIEMaterials)
====================================================================================

Overview
-----------------
The materials module populates the physicalistic perspective with materials subclasses categorised
according to modern applied physical sciences.

:Domain: Materials Science and Engineering
:Category: Materials
:Current Version:
:Last Updated:
:Creator: Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro"
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: TTL
:Download: `OIE Homepage <https://github.com/emmo-repo/OIE-Ontologies/>`_
:Documentation: `OIE Documentation <https://github.com/emmo-repo/OIE-Ontologies/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 278
    - **Root Nodes**: 13
    - **Leaf Nodes**: 115
    - **Maximum Depth**: 4
    - **Edges**: 561

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 165
    - **Non-taxonomic Relations**: 3
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import OIEMaterials

    # Initialize and load ontology
    ontology = OIEMaterials()
    ontology.load("path/to/oie-materials.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
