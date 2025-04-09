Devices, Experimental scaffolds and Biomaterials Ontology (DEB)
===============================================================

Overview
-----------------
The devices, experimental scaffolds, and biomaterials ontology (DEB) is an open resource
for organizing information about biomaterials, their design, manufacture, and biological testing.
It was developed using text analysis for identifying ontology terms from a biomaterials gold standard corpus,
systematically curated to represent the domain's lexicon. Topics covered were validated by members
of the biomaterials research community.

:Domain: Materials Science & Engineering
:Category: Materials Science
:Current Version: 06/2021
:Last Updated: Jun 2, 2021
:Producer: Osnat Hakimi
:License: GPL-3.0
:Format: OWL/XML
:Download: `DEB Homepage <https://github.com/ProjectDebbie/Ontology_DEB>`_
:Documentation: `DEB Documentation <https://github.com/ProjectDebbie/Ontology_DEB>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 1081
    - **Root Nodes**: 533
    - **Leaf Nodes**: 278
    - **Maximum Depth**: 6
    - **Edges**: 2354

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 820
    - **Non-taxonomic Relations**: 8
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import DEB

   # Initialize and load ontology
   ontology = DEB()
   ontology.load("path/to/deb.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
