Virtual Materials Marketplace (VIMMP) Ontologies
================================================

Overview
-----------------
The Virtual Materials Marketplace (VIMMP) project is developing an open platform for providing
and accessing services related to materials modelling. Within VIMMP, a system of marketplace-level ontologies
is developed to characterize services, models, and interactions between users; the European Materials
and Modelling Ontology (EMMO, recently renamed while keeping the original acronym) is employed
as a top-level ontology. The ontologies are used to annotate data that are stored in the ZONTAL Space component
of VIMMP and to support the ingest and retrieval of data and metadata at the VIMMP marketplace front-end.

:Domain: Materials Science and Engineering
:Category: Materials Modelling
:Current Version:
:Last Updated: 2021-01-02
:Creator: Ilian T. Todorov (ORCID 0000-0001-7275-1784),
          Martin Thomas Horsch (ORCID 0000-0002-9464-6739),
          Michael A. Seaton (ORCID 0000-0002-4708-573X),
          Silvia Chiacchiera (ORCID 0000-0003-0422-7870)
:License: GNU Lesser General Public License (LGPL) version 3
:Format: OWL, RDF/XML
:Download: `VIMMP Homepage <https://matportal.org/ontologies/VIMMP_ONTOLOGIES>`_
:Documentation: `VIMMP Documentation <https://matportal.org/ontologies/VIMMP_ONTOLOGIES>`_

Base Metrics
---------------
    - Classes: 1,082
    - Individuals: 897
    - Properties: 771

Graph Metrics
------------------
    - **Total Nodes**: 6149
    - **Root Nodes**: 841
    - **Leaf Nodes**: 1948
    - **Maximum Depth**: 16
    - **Edges**: 15298

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 1939
    - **Taxonomic Relations**: 4077
    - **Non-taxonomic Relations**: 404
    - **Average Terms per Type**: 34.02

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import VIMMP

   # Initialize and load ontology
   ontology = VIMMP()
   ontology.load("path/to/vimmp.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
