Semantic Sensor Network Ontology (SSN)
==========================

Overview
--------
The Semantic Sensor Network (SSN) ontology is an ontology for describing sensors and their observations,
the involved procedures, the studied features of interest, the samples used to do so, and the observed properties,
as well as actuators. SSN follows a horizontal and vertical modularization architecture
by including a lightweight but self-contained core ontology called SOSA (Sensor, Observation, Sample, and Actuator)
for its elementary classes and properties. With their different scope and different degrees of axiomatization,
SSN and SOSA are able to support a wide range of applications and use cases, including satellite imagery,
large-scale scientific monitoring, industrial and household infrastructures, social sensing, citizen science,
observation-driven ontology engineering, and the Web of Things. Both ontologies are described below,
and examples of their usage are given.

:Domain: Materials Science & Engineering
:Category: Sensor Networks
:Current Version: 1.0
:Last Updated: 2017-04-17
:Creator: W3C/OGC Spatial Data on the Web Working Group
:License: http://www.w3.org/Consortium/Legal/2015/copyright-software-and-document
:Format: RDF/XML, TTL
:Download: `Semantic Sensor Network Ontology (SSN) Homepage <https://github.com/w3c/sdw-sosa-ssn/tree/482484fe2edc1ba8aa7f19214a72bdb77123e833>`_

Graph Metrics
-------------
    - **Total Nodes**: 551
    - **Total Edges**: 1643
    - **Root Nodes**: 22
    - **Leaf Nodes**: 106

Knowledge coverage
------------------
    - Classes: 22
    - Individuals: 9
    - Properties: 38

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.15
    - **Depth Variance**: 0.13

Breadth metrics
------------------
    - **Maximum Breadth**: 22
    - **Minimum Breadth**: 4
    - **Average Breadth**: 13.00
    - **Breadth Variance**: 81.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 7
    - **Taxonomic Relations**: 7585
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 1.40

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import SSN

    # Initialize and load ontology
    ontology = SSN()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
