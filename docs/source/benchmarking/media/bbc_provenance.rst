BBC Provenance Ontology
===================

Overview
-----------------
An ontology to capture data about the provenance of data in an RDF Triple Store.
This provenance is focused on the immediate providers and not the ultimate source,
so for example, this would record that geodata was provided by the BBC Locator team,
and not geonames. In the Linked Data Platform, this data is applied to contexts or named graphs.
A named graph is, in effect, a 'fourth part' to a triple, hence the term 'quad store'.

:Domain: Media
:Category: News
:Current Version: 1.9
:Last Updated: 2012-12-01
:Producer: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Provenance Homepage <https://www.bbc.co.uk/ontologies/provenance-ontology>`_
:Documentation: `BBC Provenance Documentation <https://www.bbc.co.uk/ontologies/provenance-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 74
    - **Root Nodes**: 0
    - **Leaf Nodes**: 48
    - **Maximum Depth**: 0
    - **Edges**: 151

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 6
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.14

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCProvenance
   # Initialize and load ontology
   bbc_provenance = BBCProvenance()
   bbc_provenance.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_provenance.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
