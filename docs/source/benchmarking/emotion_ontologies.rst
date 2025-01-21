Mental Functioning Ontology - Emotion (MFOEM)
===========================================

Overview
-----------------
The Mental Functioning Ontology - Emotion Module (MFOEM) is an ontology for affective phenomena such as emotions and moods.

Ontology Statistics
-----------------
Current statistics from MFOEM:

* **Nodes**: 726
* **Edges**: 750
* **Graph Density**: 0.0014
* **Average Degree**: 2.07
* **Maximum Depth**: 13
* **Root Nodes**: 106
* **Leaf Nodes**: 443

Dataset Statistics
-----------------
The benchmark dataset includes:

* **Term Types**: 768
* **Taxonomic Relations**: 752
* **Non-taxonomic Relations**: 0
* **Average Terms per Type**: 76.80

Relationship Types
-----------------
1. **Taxonomic Relations**:
* subClassOf
* hasEmotionalCategory

2. **Non-taxonomic Relations**:
* part_of
* has_characteristic
* has_participant

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.emotion import EmotionOntology

    # Initialize and load ontology
    emotion = EmotionOntology()

    emotion.load("path/to/mfoem.owl")

    # Extract datasets
    data = cso.extract()
