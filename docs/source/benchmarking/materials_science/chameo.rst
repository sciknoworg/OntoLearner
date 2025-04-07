Characterisation Methodology Domain Ontology (CHAMEO)
========================================================

Overview
-----------------
An ontology for materials characterization which represents the evolution of the CHADA template
in an ontological form, allowing to generate FAIR documentation of Characterisation Experiments
and that has been used as a basis for the development of a number of technique-specific
or application-specific ontologies in the materials characterisation domain. CHAMEO
has been used as a foundation for the definition of the new CHADA template during the CWA.

:Domain: Materials Science and Engineering
:Category: Characterisation
:Current Version: 1.0.0
:Last Updated: 2024-04-12
:Producer: https://orcid.org/0000-0002-4181-2852, https://orcid.org/0000-0002-5174-8508, https://orcid.org/0000-0002-9668-6961
:License: Creative Commons Attribution 4.0 International License
:Format: Turtle
:Download: `CHAMEO Homepage <https://github.com/emmo-repo/domain-characterisation-methodology>`_
:Documentation: `CHAMEO Documentation <https://github.com/emmo-repo/domain-characterisation-methodology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 802
    - **Root Nodes**: 29
    - **Leaf Nodes**: 459
    - **Maximum Depth**: 13
    - **Edges**: 1526

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 397
    - **Non-taxonomic Relations**: 4
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import CHAMEO

   # Initialize and load ontology
   ontology = CHAMEO()
   ontology.load("path/to/chameo.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
