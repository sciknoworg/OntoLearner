Mental Functioning Ontology of Emotions - Emotion Module (MFOEM)
========================================================================================================================

Overview
--------
The Mental Functioning Ontology - Emotion Module (MFOEM) aims to include all relevant aspects of affective phenomena
including their bearers, the different types of emotions, moods, etc., their different parts and dimensions
of variation, their facial and vocal expressions, and the role of emotions and affective phenomena
in general in influencing human behavior.This class processes Mental Functioning Ontology of Emotions (MFOEM)
using default behavior.

:Domain: Medicine
:Category: Emotion
:Current Version: None
:Last Updated: None
:Creator: Swiss Centre for Affective Sciences & University at Buffalo
:License: Creative Commons 3.0
:Format: OWL
:Download: `Mental Functioning Ontology of Emotions - Emotion Module (MFOEM) Homepage <http://purl.obolibrary.org/obo/MFOEM.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 2542
    - **Total Edges**: 5116
    - **Root Nodes**: 163
    - **Leaf Nodes**: 1513

Knowledge coverage
------------------
    - Classes: 637
    - Individuals: 19
    - Properties: 22

Hierarchical metrics
--------------------
    - **Maximum Depth**: 13
    - **Minimum Depth**: 0
    - **Average Depth**: 2.24
    - **Depth Variance**: 5.65

Breadth metrics
------------------
    - **Maximum Breadth**: 274
    - **Minimum Breadth**: 1
    - **Average Breadth**: 65.07
    - **Breadth Variance**: 8317.35

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 19
    - **Taxonomic Relations**: 837
    - **Non-taxonomic Relations**: 20
    - **Average Terms per Type**: 4.75

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import MFOEM

    # Initialize and load ontology
    ontology = MFOEM()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
