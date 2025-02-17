Academic Institution Internal Structure Ontology (AIISO)
========================================================

Overview
-----------------
The Academic Institution Internal Structure Ontology (AIISO) provides classes and properties to describe the internal organizational structure of an academic institution. AIISO is designed to work in partnership with Participation (http://purl.org/vocab/participation/schema), FOAF (http://xmlns.com/foaf/0.1/) and aiiso-roles (http://purl.org/vocab/aiiso-roles/schema) to describe the roles that people play within an institution.

:Domain: Academic Institution
:Category: Scholarly Knowledge
:Current Version: 1.0
:Last Updated: 2008-05-14
:Producer: Open University
:License: Creative Commons 4.0
:Format: RDF/XML
:Download: `AIISO Homepage <https://vocab.org/aiiso/>`_
:Documentation: `AIISO Documentation <https://vocab.org/aiiso/>`_

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

Graph Metrics
------------------
    - **Total Nodes**: 119
    - **Root Nodes**: 8
    - **Leaf Nodes**: 54
    - **Maximum Depth**:
    - **Edges**: 247

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 13
    - **Non-taxonomic Relations**: 3
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import AIISO

   # Initialize and load ontology
   aiiso = AIISO()
   aiiso.load("path/to/ontology.rdf")
   # Extract datasets
   data = aiiso.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
