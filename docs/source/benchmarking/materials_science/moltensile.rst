Matolab Tensile Test Ontology (MOL_TENSILE)
=============================================

Overview
-----------------
An ontology for describing the tensile test process, made in the Materials Open Lab Project.

:Domain: Materials Science and Engineering
:Category: Materials Testings
:Current Version: 0.4
:Last Updated: 	04/16/2021
:Creator: Markus Schilling, markus.schilling@bam.de; Philipp von Hartrott, philipp.von.hartrott@iwm.fraunhofer.de
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:Format: OWL, RDF/XML
:Download: `MOL_TENSILE Homepage <https://matportal.org/ontologies/MOL_TENSILE>`_
:Documentation: `MOL_TENSILE Documentation <https://matportal.org/ontologies/MOL_TENSILE>`_

Base Metrics
---------------
    - Classes: 372
    - Individuals: 20
    - Properties: 97

Graph Metrics
------------------
    - **Total Nodes**: 1970
    - **Root Nodes**: 132
    - **Leaf Nodes**: 1245
    - **Maximum Depth**: 90
    - **Edges**: 3602

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 20
    - **Taxonomic Relations**: 370
    - **Non-taxonomic Relations**: 20
    - **Average Terms per Type**: 1.43

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import MOLTENSILE

   # Initialize and load ontology
   ontology = MOLTENSILE()
   ontology.load("path/to/moltensile.rdf")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
