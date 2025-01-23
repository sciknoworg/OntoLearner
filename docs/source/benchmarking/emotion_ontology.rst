Mental Functioning Ontology - Emotion (MFOEM)
===========================================

Overview
-----------------
The Mental Functioning Ontology - Emotion Module (MFOEM) is an ontology for affective phenomena
such as emotions and moods.

Basic Information
-----------------
:Domain**: Psychology, Mental Health
:Category:
:Current Version:
:Last Updated Date:
:Producer: Swiss Centre for Affective Sciences & University at Buffalo
:License: Creative Commons 3.0
:Format: OWL
:Download: `Emotion Ontology <http://purl.obolibrary.org/obo/MFOEM.owl>`_
:Documentation:

Ontology Statistics
-----------------
Graph Metrics:
    - **Triples**:
    - **Nodes**: 726
    - **Edges**: 750

Hierarchical Structure:
    - **Maximum Depth**: 13
    - **Root Nodes**: 106
    - **Leaf Nodes**: 443

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 768
    - **Taxonomic Relations**: 752
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 76.80

Relationship Types
-----------------
Taxonomic Relations:
    - subClassOf
    - hasEmotionalCategory

Non-taxonomic Relations:
    - part_of
    - has_characteristic
    - has_participant

Alignments
-----------------
    - Basic Formal Ontology (BFO)
    - Mental Functioning Ontology (MF)

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.emotion import EmotionOntology

    # Initialize and load ontology
    emotion = EmotionOntology()

    emotion.load("path/to/mfoem.owl")

    # Extract datasets
    data = cso.extract()
