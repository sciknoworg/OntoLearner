The Environment Ontology (ENVO)
===============================

Overview
-----------------
ENVO is an expressive, community ontology which helps humans, machines,
and semantic web applications understand environmental entities of all kinds,
from microscopic to intergalactic scales. As a FAIR-compliant resource, it promotes interoperability
through the concise, controlled description of all things environmental.

:Domain: Ecology
:Category: Environment, Ecosystems, Habitats
:Current Version: 2024-07-01
:Last Updated: 2024-07-01
:Producer: Pier Luigi Buttigieg (https://orcid.org/0000-0002-4366-3088)
:License: Creative Commons 1.0
:Format: OWL, OBO, JSON
:Download: `ENVO Homepage <https://obofoundry.org/ontology/envo.html>`_
:Documentation: `ENVO Documentation <http://environmentontology.org>`_

Base Metrics
---------------
    - Classes: 7041
    - Individuals: 44
    - Properties: 208
    - Annotation Assertions: 0

Graph Metrics
-------------
    - **Total Nodes**: 7423
    - **Root Nodes**: 4399
    - **Leaf Nodes**: 75
    - **Maximum Depth**: 35
    - **Edges**: 16119

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 46
    - **Taxonomic Relations**: 15937
    - **Non-taxonomic Relations**: 147
    - **Average Terms per Type**: 2.30

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import ENVO

   # Initialize and load ontology
   envo = ENVO()
   env.load("path/to/ontology.owl")
   # Extract datasets
   data = env.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
