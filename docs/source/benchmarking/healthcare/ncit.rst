NCI Thesaurus (NCIt)
====================

Overview
-----------------
NCI Thesaurus (NCIt) is a reference terminology that includes broad coverage of the cancer domain,
including cancer related diseases, findings and abnormalities. The NCIt OBO Edition aims to increase integration
of the NCIt with OBO Library ontologies. NCIt OBO Edition releases should be considered experimental.

:Domain: Life Sciences, Biology
:Category: Cancer, Oncology
:Current Version: 24.04e
:Last Updated: 2023-10-19
:Producer:
:License: Creative Commons 4.0
:Format: owl
:Download: `NCI Thesaurus <https://terminology.tib.eu/ts/ontologies/NCIT>`_
:Documentation: `NCI Thesaurus Documentation <https://terminology.tib.eu/ts/ontologies/NCIT>`_

Base Metrics
---------------
    - Classes: 191101
    - Individuals: 0
    - Properties: 248

Graph Metrics:
------------------
    - **Nodes**:
    - **Root Nodes**:
    - **Leaf Nodes**:
    - **Maximum Depth**:
    - **Edges**:

Dataset Statistics
-------------------
Generated Benchmarks:
    * **Term Types**:
    * **Taxonomic Relations**:
    * **Non-taxonomic Relations**:
    * **Average Terms per Type**:

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.ncit import NCITOntology

    # Initialize and load ontology
    ncit = NCITOntology()
    # Load ontology from file
    ncit.load("path/to/ncit.owl")
    # Extract datasets
    data = ncit.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
