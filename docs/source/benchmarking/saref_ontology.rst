SAREF: the Smart Applications REFerence ontology
=================================================

Overview
-----------------
The Smart Applications REFerence (SAREF) suite of ontologies forms a shared model of consensus
intended to enable semantic interoperability between solutions from different providers
and among various activity sectors in the Internet of Things (IoT),
thus contributing to the development of data spaces. SAREF is published as a set of open standards
produced by ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M).

:Domain: Internet of Things
:Category: interoperability
:Current Version: 3.2.1
:Last Updated: 2020-12-31
:Producer: ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M)
:License:
:Format: OWL, RDF/XML, TTL, JSON-LD
:Download: `SAREF Homepage <https://saref.etsi.org/core/v3.2.1/>`_
:Documentation: `SAREF Documentation <https://saref.etsi.org/index.html>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Schema Metrics
---------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics:
------------------
    - **Total Nodes**: 804
    - **Root Nodes**: 14
    - **Leaf Nodes**: 376
    - **Maximum Depth**:
    - **Edges**: 1720

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 10
    - **Taxonomic Relations**: 224
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 2.50

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import SAREF

   # Initialize and load ontology
   saref = SAREF()
   saref.load("path/to/ontology.owl")
   # Extract datasets
   data = saref.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
