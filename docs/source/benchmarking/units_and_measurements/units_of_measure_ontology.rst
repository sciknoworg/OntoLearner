Ontology of units of Measure (OM)
===================================

Overview
-----------------
The Ontology of units of Measure (OM) 2.0 models concepts and relations important to scientific research.
It has a strong focus on units, quantities, measurements, and dimensions.
It includes, for instance, common units such as the SI units metre and kilogram,
but also units from other systems of units such as the mile or nautical mile. For many application areas
it includes more specific units and quantities, such as the unit of the Hubble constant or the quantity vaselife.
The following application areas are supported by OM: Geometry; Mechanics; Thermodynamics; Electromagnetism;
Fluid mechanics; Chemical physics; Photometry; Radiometry and Radiobiology; Nuclear physics;
Astronomy and Astrophysics; Cosmology; Earth science; Meteorology; Material science; Microbiology;
Economics; Information technology and Typography.

:Domain: Units and Measurements
:Category: Units and Measurements
:Current Version: 2.0.57
:Last Updated: June 28, 2024
:Producer: Hajo Rijgersberg, Don Willems, Jan Top
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `OM Homepage <https://bioportal.bioontology.org/ontologies/OM>`_
:Documentation: `OM Documentation <https://bioportal.bioontology.org/ontologies/OM>`_

Base Metrics
---------------
    - Classes: 814
    - Individuals: 2,251
    - Properties: 34

Graph Metrics
--------------
    - **Total Nodes**: 9,352
    - **Root Nodes**: 27
    - **Leaf Nodes**: 4,836
    - **Maximum Depth**: 4
    - **Edges**: 27,500

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 1,953
    - **Taxonomic Relations**: 2,016
    - **Non-taxonomic Relations**: 230
    - **Average Terms per Type**: 55.80

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import OM

   # Initialize and load ontology
   om = OM()
   om.load("path/to/ontology.owl")
   # Extract datasets
   data = om.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
