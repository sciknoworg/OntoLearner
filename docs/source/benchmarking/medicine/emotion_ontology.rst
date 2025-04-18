Mental Functioning Ontology - Emotion (MFOEM)
==============================================

Overview
-----------------
The Mental Functioning Ontology - Emotion Module (MFOEM) aims to include all relevant aspects of affective phenomena
including their bearers, the different types of emotions, moods, etc., their different parts and dimensions of variation,
their facial and vocal expressions, and the role of emotions and affective phenomena
in general in influencing human behavior.

:Domain**: Medicine
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


Graph Metrics
-----------------
    - **Nodes**: 727
    - **Root Nodes**: 498
    - **Leaf Nodes**: 14
    - **Maximum Depth**: 13
    - **Edges**: 1446

Dataset Statistics
--------------------
Generated Benchmarks:
    - **Term Types**: 19
    - **Taxonomic Relations**: 832
    - **Non-taxonomic Relations**: 20
    - **Average Terms per Type**: 1.06

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology import EmotionOntology

    # Initialize and load ontology
    emotion = EmotionOntology()
    emotion.load("path/to/ontology.owl")
    # Extract datasets
    data = emotion.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
