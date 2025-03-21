Animal Trait Ontology for Livestock
====================================

Overview
-----------------
ATOL (Animal Trait Ontology for Livestock) is an ontology of characteristics defining phenotypes of livestock
in their environment (EOL). ATOL aims to:
- provide a reference ontology of phenotypic traits of farm animals for the international scientific and educational
- communities, farmers, etc.;
- deliver this reference ontology in a language which can be used by computers in order to support database management,
semantic analysis and modeling;
- represent traits as generic as possible for livestock vertebrates;
- make the ATOL ontology as operational as possible and closely related to measurement techniques;
- structure the ontology in relation to animal production.

:Domain: Animal Science
:Category: Livestock
:Current Version: 6.0
:Last Updated: May 11, 2020
:Producer: INRAE, France
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `ATOL Homepage <https://bioportal.bioontology.org/ontologies/ATOL>`_
:Documentation: `ATOL Documentation <https://bioportal.bioontology.org/ontologies/ATOL>`_

Base Metrics
---------------
    - Classes: 2,352
    - Individuals: 0
    - Properties: 0

Graph Metrics
------------------
    - **Total Nodes**: 8,220
    - **Root Nodes**: 12
    - **Leaf Nodes**: 5,868
    - **Maximum Depth**: 12
    - **Edges**: 52,090

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2,628
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import ATOL

   # Initialize and load ontology
   atol = ATOL()
   atol.load("path/to/ontology.owl")
   # Extract datasets
   data = atol.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.non_type_taxonomies
