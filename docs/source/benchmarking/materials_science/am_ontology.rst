Additive Manufacturing Ontology (AMOntology)
=============================================

Overview
-----------------
The AM ontology has been developed following two major milestones. The ontology developed within the first milestone
includes AMProcessOntology, ModelOntology and AMOntology files. AMProcessOntology contains the set of entities
used to capture knowledge about additive manufacturing processes. ModelOntology contains the set of entities
used to capture knowledge about modeling concepts that represent (possibly) multi-physics multi-scale processes.
AMOntology uses AMProcessOntology and ModelOntology files to describe entities that capture knowledge
about characteristics of computational models for AM processes.

:Domain: Materials Science & Engineering
:Category: Manufacturing
:Current Version:
:Last Updated:
:Producer:
:License:
:Format: Turtle
:Download: `AMOntology Homepage <https://github.com/iassouroko/AMontology>`_
:Documentation: `AMOntology Documentation <https://github.com/iassouroko/AMontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 900
    - **Root Nodes**: 71
    - **Leaf Nodes**: 99
    - **Maximum Depth**: 24
    - **Edges**: 2299

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 59
    - **Taxonomic Relations**: 1603
    - **Non-taxonomic Relations**: 24
    - **Average Terms per Type**: 1.48

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import AMOntology

   # Initialize and load ontology
   ontology = AMOntology()
   ontology.load("path/to/am_ontology.ttl")

   # Extract datasets
   data = ontology.extract()

   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
