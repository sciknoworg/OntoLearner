Open Provenance Model for Workflows (OPMW)
==========================================

Overview
-----------------
The Open Provenance Model for Workflows (OPMW) is an ontology for describing workflow traces
and their templates based on the Open Provenance Model. It has been designed as a profile for OPM,
extending and reusing OPM's core ontologies OPMV (OPM-Vocabulary) and OPMO (OPM-Ontology).

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 3.1
:Last Updated: 2014-12-22
:Creator: http://delicias.dia.fi.upm.es/members/DGarijo/#me, http://www.isi.edu/~gil/
:License: Creative Commons Attribution 2.0 Generic (CC BY 2.0)
:Format: OWL, RDF/XML
:Download: `OPMW Homepage <https://www.opmw.org/model/OPMW_20141222/>`_
:Documentation: `OPMW Documentation <https://www.opmw.org/model/OPMW_20141222/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 539
    - **Root Nodes**: 33
    - **Leaf Nodes**: 306
    - **Maximum Depth**: 7
    - **Edges**: 1387

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 79
    - **Non-taxonomic Relations**: 4
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import OPMW

    # Initialize and load ontology
    ontology = OPMW()
    ontology.load("path/to/opmw.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
