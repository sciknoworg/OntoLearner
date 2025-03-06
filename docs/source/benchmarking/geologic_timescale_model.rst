Geologic Timescale model (GTS)
==============================

Overview
-----------------
This is an RDF/OWL representation of the GeoSciML Geologic Timescale model, which has been adapted
from the model described in Cox, S.J.D, & Richard, S.M. (2005) A formal model for the geologic timescale and GSSP,
compatible with geospatial information transfer standards, Geosphere, Geological Society of America.

:Domain: Geology
:Category: Geography
:Current Version: 1.0
:Last Updated: 2020-05-31
:Producer: Simon J D Cox  (simon.cox@csiro.au) of CSIRO
:License: Creative Commons 1.0
:Format: OWL, TTL
:Download: `GeoSciML Homepage <https://raw.githack.com/CGI-IUGS/timescale-ont/master/html/gts.html>`_
:Documentation: `GeoSciML Documentation <https://raw.githack.com/CGI-IUGS/timescale-ont/master/html/gts.html>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 311
    - **Root Nodes**: 0
    - **Leaf Nodes**: 92
    - **Maximum Depth**: 0
    - **Edges**: 743

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 7
    - **Taxonomic Relations**: 549
    - **Non-taxonomic Relations**: 2
    - **Average Terms per Type**: 0.47

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import GTS

   # Initialize and load ontology
   gts = GTS()
   gts.load("path/to/ontology.owl")
   # Extract datasets
   data = gts.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
