iCalendar Vocabulary (iCalendar)
========================================================================================================================

Overview
--------
iCalendar is an Internet standard for exchanging calendar and scheduling data across different applications
and platforms using a standardized text-based format (.ics). It enables interoperability for events, tasks,
and scheduling, supporting features like recurring events, invitations, and time zone adjustments.
While widely used in applications like Google Calendar and Outlook, its complexity and partial implementations
pose challenges, leading to efforts to integrate it with Semantic Web technologies
for enhanced data linking and automation.

:Domain: Events
:Category: Calendar and Scheduling
:Current Version: 1.14
:Last Updated: 2004/04/07
:Creator: Dan Connolly, W3C, Libby Miller, ASemantics
:License: Open Publication License
:Format: RDF
:Download: `iCalendar Vocabulary (iCalendar) Homepage <https://www.w3.org/2002/12/cal/>`_

Graph Metrics
-------------
    - **Total Nodes**: 496
    - **Total Edges**: 1271
    - **Root Nodes**: 4
    - **Leaf Nodes**: 93

Knowledge coverage
------------------
    - Classes: 54
    - Individuals: 0
    - Properties: 49

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.60
    - **Depth Variance**: 0.24

Breadth metrics
------------------
    - **Maximum Breadth**: 6
    - **Minimum Breadth**: 4
    - **Average Breadth**: 5.00
    - **Breadth Variance**: 1.00

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2994
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import iCalendar

    # Initialize and load ontology
    ontology = iCalendar()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
