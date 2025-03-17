The ontology of data analysis and management (EDAM)
===================================================

Overview
-----------------
EDAM is a domain ontology of data analysis and data management in bio- and other sciences, and science-based applications.
It comprises concepts related to analysis, modelling, optimisation, and data life cycle. Targetting usability by diverse users,
the structure of EDAM is relatively simple, divided into 4 main sections: Topic, Operation, Data (incl. Identifier), and Format.

:Domain: General
:Category: General
:Current Version: 1.25-20240924T0027Z-unstable(1.26)
:Last Updated: 24.09.2024
:Producer: Federico Bianchini, Hervé Ménager, Jon Ison, Matúš Kalaš
:License: Creative Commons 4.0
:Format: owl
:Download:`EDAM Ontology <https://terminology.tib.eu/ts/ontologies/edam>`_
:Documentation: `EDAM Documentation <https://terminology.tib.eu/ts/ontologies/edam>`_

Base Metrics
---------------
    - Classes: 3511
    - Properties: 75
    - Individuals: 0

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
    * **Term Types**: 0
    * **Taxonomic Relations**: 9748
    * **Non-taxonomic Relations**: 1314
    * **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.edam import EdamOntology

    # Initialize and load ontology
    edam = EdamOntology()
    # Load ontology from file
    edam.load("path/to/edam-ontology.owl")
    # Extract datasets
    data = edam.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
