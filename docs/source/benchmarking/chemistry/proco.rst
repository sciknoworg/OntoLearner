PROcess Chemistry Ontology (PROCO)
================

Overview
-----------------
PROCO (PROcess Chemistry Ontology) is a formal ontology that aims to standardly
represent entities and relations among entities in the domain of process chemistry.

:Domain: Chemistry
:Category: Chemicals, Processes
:Current Version: 04-14-2022
:Last Updated: 04-14-2022
:Producer: Anna Dun, Wes A. Schafer, Yongqun &quot;Oliver&quot; He (YH), Zachary Dance
:License: Creative Commons 4.0
:Format: OWL
:Download: `PROCO Homepage <https://github.com/proco-ontology/PROCO>`_
:Documentation: `PROCO Documentation <https://github.com/proco-ontology/PROCO>`_

Base Metrics
---------------
    - Classes: 922
    - Individuals: 17
    - Properties: 149

Graph Metrics:
------------------
    - **Total Nodes**: 6258
    - **Root Nodes**: 89
    - **Leaf Nodes**: 4646
    - **Maximum Depth**: 18
    - **Edges**: 11796

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 14
    - **Taxonomic Relations**: 2975
    - **Non-taxonomic Relations**: 17
    - **Average Terms per Type**: 0.9

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import PROCO

    # Initialize and load ontology
    ontology = PROCO()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
