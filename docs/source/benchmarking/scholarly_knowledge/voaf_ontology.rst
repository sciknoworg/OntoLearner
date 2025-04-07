Vocabulary of a Friend (VOAF) Ontology
=======================================

Overview
-----------------
VOAF is a vocabulary specification providing elements allowing the description of vocabularies
(RDFS vocabularies or OWL ontologies) used in the Linked Data Cloud. In particular it provides properties
expressing the different ways such vocabularies can rely on, extend, specify, annotate or otherwise link to each other.
It relies itself on Dublin Core and voiD. The name of the vocabulary makes an explicit reference
to FOAF because VOAF can be used to define networks of vocabularies in a way similar to the one FOAF
is used to define networks of people.

:Domain: Linked Data
:Category: Social Network
:Current Version: 2.3
:Last Updated: 2013-05-24
:Producer: Bernard Vatant
:License: Creative Commons 3.0
:Format: RDF/XML
:Download: `VOAF Homepage <https://lov.linkeddata.es/vocommons/voaf/v2.3/>`_
:Documentation: `VOAF Documentation <https://lov.linkeddata.es/vocommons/voaf/v2.3/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 175
    - **Root Nodes**: 0
    - **Leaf Nodes**: 129
    - **Maximum Depth**:
    - **Edges**: 304

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 4
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.11

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import VOAF

   # Initialize and load ontology
   voaf = VOAF()
   voaf.load("path/to/ontology.owl")
   # Extract datasets
   data = voaf.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
