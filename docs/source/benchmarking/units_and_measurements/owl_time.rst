Time Ontology in OWL
====================

Overview
-----------------
OWL-Time is an OWL-2 DL ontology of temporal concepts, for describing the temporal properties of resources
in the world or described in Web pages. The ontology provides a vocabulary for expressing facts
about topological (ordering) relations among instants and intervals, together with information about durations,
and about temporal position including date-time information. Time positions and durations may be expressed
using either the conventional (Gregorian) calendar and clock, or using another temporal reference system
such as Unix-time, geologic time, or different calendars.

:Domain: Units and Measurements
:Category: Temporal Reasoning
:Current Version: 1.0
:Last Updated: 15 November 2022
:Producer: World Wide Web Consortium
:License: W3C Software Notice and Document License
:Format: TTL, OWL
:Download: `OWL-Time Homepage <https://www.w3.org/TR/owl-time/>`_
:Documentation: `OWL-Time Documentation <https://www.w3.org/TR/owl-time/>`_

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
    - **Total Nodes**: 700
    - **Root Nodes**: 0
    - **Leaf Nodes**: 532
    - **Maximum Depth**: 0
    - **Edges**: 1132

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 17
    - **Taxonomic Relations**: 529
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0.94

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import OWLTime

   # Initialize and load ontology
   time = OWLTime()
   time.load("path/to/ontology.owl")
   # Extract datasets
   data = time.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
