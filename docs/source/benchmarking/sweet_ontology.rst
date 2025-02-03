Semantic Web for Earth and Environment Technology Ontology (SWEET)
================================================================

Overview
-----------------
The Semantic Web for Earth and Environment Technology Ontology (SWEET) is an investigation in improving discovery
and use of Earth science data, through software understanding of the semantics of web resources.
SWEET is a collection of ontologies conceptualizing a knowledge space for Earth system science,
represented using the web ontology language (OWL). It includes both orthogonal concepts (space, time,
Earth realms, physical quantities, etc.) and integrative science knowledge concepts (phenomena, events, etc.).

:Domain: Earth Science, Environmental Science
:Category: Earth System Science, Geoscience
:Current Version: 3.6.0
:Last Updated: July 14, 2022
:Producer: NASA, JPL, Caltech
:License: Creative Commons 4.0
:Format: OWL
:Download: `SWEET Homepage <https://bioportal.bioontology.org/ontologies/SWEET>`_

Base Metrics
---------------
    - Classes: 10,239
    - Individuals: 2,148
    - Properties: 359
    - Annotation Assertions: 0
    - DL Expressivity:

Graph Metrics:
------------------
    - **Total Nodes**: 12,468
    - **Root Nodes**: 10,212
    - **Leaf Nodes**: 13
    - **Maximum Depth**: 14
    - **Edges**: 27,954

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 2,221
    - **Taxonomic Relations**: 16,070
    - **Non-taxonomic Relations**: 515
    - **Average Terms per Type**: 79.32

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology.sweet import SweetOntology

    # Initialize and load ontology
    sweet = SweetOntology()
    sweet.load("path/to/sweet-ontology.owl")
    # Extract datasets
    data = sweet.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.taxonomic_relations
    non_taxonomic_relations = data.non_taxonomic_relations
