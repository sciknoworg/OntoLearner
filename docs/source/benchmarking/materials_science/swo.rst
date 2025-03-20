The Software Ontology (SWO)
============================

Overview
-----------------
The Software Ontology (SWO) is a resource for describing software tools, their types, tasks, versions,
provenance and associated data. It contains detailed information on licensing and formats
as well as software applications themselves, mainly (but not limited) to the bioinformatics community.

:Domain: General
:Category: General
:Current Version: 1.0
:Last Updated: 	2023-03-05
:Producer: Allyson Lister, Andy Brown, Duncan Hull, Helen Parkinson, James Malone, Jon Ison, Nandini Badarinarayan, Robert Stevens
:License: Creative Commons 4.0
:Format: OWL
:Download: `SWO Homepage <https://terminology.tib.eu/ts/ontologies/SWO>`_
:Documentation: `SWO Documentation <https://terminology.tib.eu/ts/ontologies/SWO>`_

Base Metrics
---------------
    - Classes: 1971
    - Properties: 240
    - Individuals: 446

Graph Metrics:
------------------
    - **Nodes**: 12367
    - **Root Nodes**: 176
    - **Leaf Nodes**: 8223
    - **Maximum Depth**: 17
    - **Edges**: 36215

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 9748
    - **Non-taxonomic Relations**: 1314
    - **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.swo import SWO

    # Initialize and load ontology
    swo = SWO()
    # Load ontology from file
    swo.load("path/to/ontology.owl")
    # Extract datasets
    data = swo.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
