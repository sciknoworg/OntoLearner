The Heat Pump Ontology (HPOnt)
==============================

Overview
-----------------
The Heat Pump Ontology (HPOnt) aims to formalize and represent all the relevant information of Heat Pumps.
The HPOnt has been developed as part of the REACT project which has received funding
from the European Union’s Horizon 2020 research and innovation programme under grant agreement no. 824395.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 0.2
:Last Updated:
:Producer: REACT Project
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `HPOnt Homepage <https://react2020.github.io/REACT-ONTOLOGY/HPOnt/index-en.html/>`_
:Documentation: `HPOnt Documentation <https://react2020.github.io/REACT-ONTOLOGY/HPOnt/index-en.html>`_

Base Metrics
------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
-------------
    - **Total Nodes**: 84
    - **Root Nodes**: 16
    - **Leaf Nodes**: 43
    - **Maximum Depth**: 5
    - **Edges**: 143

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 5
    - **Taxonomic Relations**: 4
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.23


Usage Example
^^^^^^^^^^^^^
.. code-block:: python

    from ontolearner.ontology import HPOnt

    # Initialize and load ontology
    hpo = HPOnt()
    hpo.load("path/to/ontology.owl")
    # Extract datasets
    data = hpo.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
