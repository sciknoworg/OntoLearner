iCalendar Vocabulary
====================

Overview
-----------------
iCalendar is an Internet standard for exchanging calendar and scheduling data across different applications
and platforms using a standardized text-based format (.ics). It enables interoperability for events, tasks,
and scheduling, supporting features like recurring events, invitations, and time zone adjustments.
While widely used in applications like Google Calendar and Outlook, its complexity and partial implementations
pose challenges, leading to efforts to integrate it with Semantic Web technologies
for enhanced data linking and automation.

:Domain: Calendar and Scheduling
:Category: Event Management
:Current Version: 1.14
:Last Updated: 2004/04/07
:Producer: Dan Connolly, W3C, Libby Miller, ASemantics
:License: Open Publication License
:Format: RDF
:Download: `iCalendar Homepage <https://www.w3.org/2002/12/cal/>`_
:Documentation: `iCalendar Documentation <https://www.w3.org/2002/12/cal/>`_

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
    - **Total Nodes**: 496
    - **Root Nodes**: 4
    - **Leaf Nodes**: 93
    - **Maximum Depth**: 1
    - **Edges**: 1271

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2994
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import ICalendar

   # Initialize and load ontology
   ical = ICalendar()
   ical.load("path/to/ontology.rdf")
   # Extract datasets
   data = ical.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
