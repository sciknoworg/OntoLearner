BBC Sport Ontology
==============

Overview
-----------------
The Sport Ontology is a simple lightweight ontology for publishing data about competitive sports events.
The terms in this ontology allow data to be published about:
The structure of sports tournaments as a series of eventsThe competing of agents in a competitionThe type
of discipline a event involvesThe award associated with the competition and how received it...etc
Whilst it originates in a specific BBC use case, the Sport Ontology should be applicable
to a wide range of competitive sporting events data publishing use cases.
Care has been taken to try and ensure interoperability with more general ontologies in use.
In particular it draws heavily upon the events ontology.

:Domain: Sport
:Category: Sport
:Current Version: 3.2
:Last Updated:
:Producer: https://uk.linkedin.com/pub/jem-rayfield/27/b19/757, https://uk.linkedin.com/in/paulwilton, https://www.blockslabpillar.com, https://www.linkedin.com/in/tfgrahame, https://uk.linkedin.com/pub/stuart-williams/8/684/351, https://uk.linkedin.com/in/brianwmcbride
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Sport Homepage <https://www.bbc.co.uk/ontologies/sport-ontology>`_
:Documentation: `BBC Sport Documentation <https://www.bbc.co.uk/ontologies/sport-ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 232
    - **Root Nodes**: 42
    - **Leaf Nodes**: 115
    - **Maximum Depth**: 3
    - **Edges**: 490

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 40
    - **Taxonomic Relations**: 25
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 2.35

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCSport
   # Initialize and load ontology
   bbc_sport = BBCSport()
   bbc_sport.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_sport.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
