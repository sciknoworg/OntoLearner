Framester Ontology (Framester)
========================================================================================================================

Overview
--------
Framester is a a frame-based ontological resource acting as a hub
between linguistic resources such as FrameNet, WordNet, VerbNet, BabelNet,
DBpedia, Yago, DOLCE-Zero, and leveraging this wealth of links to create
an interoperable predicate space formalized according to frame semantics and semiotics.
Framester uses WordNet and FrameNet at its core, expands it to other resources
transitively, and represents them in a formal version of frame semantics.

:Domain: Scholarly Knowledge
:Category: Linguistics
:Current Version: 1.0
:Last Updated: 19-04-2016
:Creator: Aldo Gangemi
:License: Creative Commons 4.0
:Format: RDF
:Download: `Framester Ontology (Framester) Homepage <http://150.146.207.114/lode/extract?url=http://ontologydesignpatterns.org/ont/framester/framester.owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 174
    - **Total Edges**: 398
    - **Root Nodes**: 85
    - **Leaf Nodes**: 38

Knowledge coverage
------------------
    - Classes: 59
    - Individuals: 0
    - Properties: 77

Hierarchical metrics
--------------------
    - **Maximum Depth**: 3
    - **Minimum Depth**: 0
    - **Average Depth**: 0.69
    - **Depth Variance**: 0.65

Breadth metrics
------------------
    - **Maximum Breadth**: 85
    - **Minimum Breadth**: 4
    - **Average Breadth**: 42.25
    - **Breadth Variance**: 937.69

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 135
    - **Non-taxonomic Relations**: 1
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import Framester

    # Initialize and load ontology from local file
    ontology = Framester()
    ontology.load("path/to/ontology.RDF")

    # Or load from a Hugging Face repository
    ontology = Framester()
    ontology.load()

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
