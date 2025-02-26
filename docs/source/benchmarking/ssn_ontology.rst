Semantic Sensor Network Ontology
================================

Overview
-----------------
The Semantic Sensor Network (SSN) ontology is an ontology for describing sensors and their observations,
the involved procedures, the studied features of interest, the samples used to do so, and the observed properties,
as well as actuators. SSN follows a horizontal and vertical modularization architecture
by including a lightweight but self-contained core ontology called SOSA (Sensor, Observation, Sample, and Actuator)
for its elementary classes and properties. With their different scope and different degrees of axiomatization,
SSN and SOSA are able to support a wide range of applications and use cases, including satellite imagery,
large-scale scientific monitoring, industrial and household infrastructures, social sensing, citizen science,
observation-driven ontology engineering, and the Web of Things. Both ontologies are described below,
and examples of their usage are given.

:Domain: Sensor Networks
:Category: Material Science and Engineering
:Current Version: 1.0
:Last Updated: 2017-04-17
:Producer: W3C/OGC Spatial Data on the Web Working Group
:License: http://www.w3.org/Consortium/Legal/2015/copyright-software-and-document
:Format: RDF/XML, TTL
:Download: `SSN Homepage <https://github.com/w3c/sdw-sosa-ssn/tree/482484fe2edc1ba8aa7f19214a72bdb77123e833>`_
:Documentation: `SSN Documentation <https://github.com/w3c/sdw-sosa-ssn/tree/482484fe2edc1ba8aa7f19214a72bdb77123e833>`_

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
    - **Total Nodes**: 196
    - **Root Nodes**: 14
    - **Leaf Nodes**: 52
    - **Maximum Depth**:
    - **Edges**: 426

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 2
    - **Taxonomic Relations**: 514
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.40

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import SSN

   # Initialize and load ontology
   ssn = SSN()
   ssn.load("path/to/ontology.owl")
   # Extract datasets
   data = ssn.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
