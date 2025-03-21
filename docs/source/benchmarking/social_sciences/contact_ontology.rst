Contact Ontology
================

Overview
-----------------
Ontology to capture concepts related to contact information (addresses, phone numbers).
Reuses the iContact Ontology developed by the Enterprise Integration Lab in Toronto.
The iContact ontology is extended to introduce a specialized definition of Hours of Operation,
defined as a subclass of both the iContact definition of hours of operation,
and a subclass of the Recurring Event class defined in the iCity Recurring Event ontology.
The Contact ontology also extends the definition of address to include an associated location.

:Domain: Contact Information
:Category: Social
:Current Version: 1.0
:Last Updated: 2018-07-06
:Producer: Mark Fox, Megan Katsumi
:License:
:Format: OWL, TTL, CSV, NT
:Download: `Contact Ontology Homepage <https://enterpriseintegrationlab.github.io/icity/Contact/Contact_1.0/doc/index-en.html>`_
:Documentation: `Contact Ontology Documentation <https://enterpriseintegrationlab.github.io/icity/Contact/Contact_1.0/doc/index-en.html>`_

Base Metrics
---------------
    - Classes: 1
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 433
    - **Root Nodes**: 129
    - **Leaf Nodes**: 50
    - **Maximum Depth**: 22
    - **Edges**: 845

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 610
    - **Non-taxonomic Relations**: 7
    - **Average Terms per Type**: 0.12

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import Contact

   # Initialize and load ontology
   contact = Contact()
   contact.load("path/to/ontology.rdf")
   # Extract datasets
   data = contact.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
