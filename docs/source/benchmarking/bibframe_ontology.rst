Bibliographic Framework Ontology (BIBFRAME)
======================

Overview
-----------------
The Bibframe vocabulary consists of RDF classes and properties used for the description of
items cataloged principally by libraries, but may also be used to describe items cataloged by museums and archives.
Classes include the three core classes - Work, Instance, and Item - in addition to many more
classes to support description. Properties describe characteristics of the resource being
described as well as relationships among resources. For example: one Work
might be a "translation of" another Work; an Instance may be an
"instance of" a particular Bibframe Work.  Other properties describe attributes of Works and Instances.  For
example: the Bibframe property "subject" expresses an important attribute of a Work
(what the Work is about), and the property "extent" (e.g. number of pages) expresses an
attribute of an Instance.

:Domain: Library Science
:Category: Education
:Current Version: 2.5.0
:Last Updated: 2022-10-03
:Producer: United States, Library of Congress
:License: Creative Commons 1.0
:Format: RDF/XML
:Download: `BIBFRAME Homepage <https://id.loc.gov/ontologies/bflc.html>`_
:Documentation: `BIBFRAME Documentation <https://id.loc.gov/ontologies/bflc.html>`_

Base Metrics
-------------------
    - Classes:
    - Individuals:
    - Properties:

Schema Metrics
-------------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics
------------------
    - **Total Nodes**: 967
    - **Root Nodes**: 6
    - **Leaf Nodes**: 578
    - **Maximum Depth**:
    - **Edges**: 2460

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 134
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import Bibframe

   # Initialize and load ontology
   bibframe = Bibframe()
   bibframe.load("path/to/ontology.owl")
   # Extract datasets
   data = bibframe.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
