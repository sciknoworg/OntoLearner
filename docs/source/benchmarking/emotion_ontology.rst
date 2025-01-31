Mental Functioning Ontology - Emotion (MFOEM)
===========================================

Overview
-----------------
The Mental Functioning Ontology - Emotion Module (MFOEM) is an ontology for affective phenomena
such as emotions and moods.

:Domain**: Psychology, Mental Health
:Category: Emotion
:Current Version:
:Last Updated:
:Producer: Swiss Centre for Affective Sciences & University at Buffalo
:License: Creative Commons 3.0
:Format: OWL
:Download: `Emotion Ontology <http://purl.obolibrary.org/obo/MFOEM.owl>`_
:Documentation:

Base Metrics
---------------
    - Classes:
    - Properties:
    - Annotation Assertions:
    - DL Expressivity:

Schema Metrics
---------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics
-----------------
    - **Nodes**: 727
    - **Root Nodes**: 498
    - **Leaf Nodes**: 14
    - **Maximum Depth**: 13
    - **Edges**: 1446

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 19
    - **Taxonomic Relations**: 832
    - **Non-taxonomic Relations**: 20
    - **Average Terms per Type**: 1.06

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.emotion import EmotionOntology

    # Initialize and load ontology
    emotion = EmotionOntology()
    emotion.load("path/to/ontology.owl")
    # Extract datasets
    data = emotion.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
