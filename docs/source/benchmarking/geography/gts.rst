Geologic Timescale model (GTS)
========================================================================================================================

Overview
--------
This is an RDF/OWL representation of the GeoSciML Geologic Timescale model, which has been adapted
from the model described in Cox, S.J.D, & Richard, S.M. (2005) A formal model for the geologic timescale and GSSP,
compatible with geospatial information transfer standards, Geosphere, Geological Society of America.

:Domain: Geography
:Category: geospatial Information, Geology
:Current Version: 1.0
:Last Updated: 2020-05-31
:Creator: Simon J D Cox (simon.cox@csiro.au) of CSIRO
:License: Creative Commons 1.0
:Format: TTL
:Download: `Geologic Timescale model (GTS) Homepage <https://raw.githack.com/CGI-IUGS/timescale-ont/master/html/gts.html>`_

Graph Metrics
-------------
    - **Total Nodes**: 311
    - **Total Edges**: 743
    - **Root Nodes**: 0
    - **Leaf Nodes**: 92

Knowledge coverage
------------------
    - Classes: 40
    - Individuals: 7
    - Properties: 12

Hierarchical metrics
--------------------
    - **Maximum Depth**: 0
    - **Minimum Depth**: 0
    - **Average Depth**: 0.00
    - **Depth Variance**: 0.00

Breadth metrics
------------------
    - **Maximum Breadth**: 0
    - **Minimum Breadth**: 0
    - **Average Breadth**: 0.00
    - **Breadth Variance**: 0.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 7
    - **Taxonomic Relations**: 77
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 7.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import GTS

    # Initialize and load ontology
    ontology = GTS()
    ontology.load("path/to/ontology.TTL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
