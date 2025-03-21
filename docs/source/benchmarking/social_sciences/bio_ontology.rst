BIO: A vocabulary for biographical information
================================================

Overview
-----------------
The BIO vocabulary contains terms useful for finding out more about people and their backgrounds and has some cross-over into genealogical information.
The approach taken is to describe a person's life as a series of interconnected key events, around which other information can be woven.
This vocabulary defines the event framework and supplies a set of core event types that cover many use cases, but it is expected that it
will be extended in other vocabularies to suit their needs. The intention of this vocabulary is to describe biographical events of people
and this intention carries through to the definitions of the properties and classes which are person-centric rather than neutral. For example
the Employment event puts the person being employed as the principal agent in the event rather than the employer.

:Domain: Social Sciences
:Category: Biographical Information
:Current Version: 0.1
:Last Updated: 2010-05-10
:Producer: Ian Davis and David Galbraith
:License: Public Domain
:Format: RDF, TTL, CSV, NT
:Download: `BIO Homepage <https://vocab.org/bio/>`_
:Documentation: `BIO Documentation <https://vocab.org/bio/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 326
    - **Root Nodes**: 16
    - **Leaf Nodes**: 187
    - **Maximum Depth**:
    - **Edges**: 816

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 62
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0.17

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BIO

   # Initialize and load ontology
   bio = BIO()
   bio.load("path/to/ontology.owl")
   # Extract datasets
   data = bio.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
