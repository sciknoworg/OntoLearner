Bibliographic Framework Ontology (BIBFRAME)
========================================================================================================================

Overview
--------
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

:Domain: Education
:Category: Library, Museums, Archives
:Current Version: 2.5.0
:Last Updated: 2022-10-03
:Creator: United States, Library of Congress
:License: Creative Commons 1.0
:Format: RDF
:Download: `Bibliographic Framework Ontology (BIBFRAME) Homepage <https://id.loc.gov/ontologies/bflc.html>`_

Graph Metrics
-------------
    - **Total Nodes**: 967
    - **Total Edges**: 2460
    - **Root Nodes**: 6
    - **Leaf Nodes**: 578

Knowledge coverage
------------------
    - Classes: 212
    - Individuals: 0
    - Properties: 215

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 1.11
    - **Depth Variance**: 0.54

Breadth metrics
------------------
    - **Maximum Breadth**: 22
    - **Minimum Breadth**: 2
    - **Average Breadth**: 9.00
    - **Breadth Variance**: 59.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 134
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import BIBFRAME

    # Initialize and load ontology
    ontology = BIBFRAME()
    ontology.load("path/to/ontology.RDF")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
