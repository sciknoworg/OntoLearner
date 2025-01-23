Computer Science Ontology (CSO)
==============================

Overview
-----------------
The Computer Science Ontology (CSO) is a large-scale ontology of research areas in computer science.
It provides a comprehensive vocabulary of research topics in computing, organized in a hierarchical structure.

Basic Information
---------------
:Domain: Computer Science
:Category: Research Areas
:Current Version: 3.4
:Last Updated: date
:Producer: Knowledge Media Institute, Open University
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `CSO Homepage <https://cso.kmi.open.ac.uk/home>`_
:Documentation: `CSO Documentation <https://cso.kmi.open.ac.uk/about>`_

Ontology Statistics
------------------
Graph Metrics:
    - **Total Triples**:
    - **Nodes**: 14,604
    - **Edges**: 93,289

Hierarchical Structure:
    - **Maximum Depth**: 11
    - **Root Nodes**: 9
    - **Leaf Nodes**: 8,353

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 14,604
    - **Taxonomic Relations**: 44,204
    - **Non-taxonomic Relations**: 58,984
    - **Average Terms per Type**: 14,604.00

Relationship Types
----------------
Taxonomic Relations:
   - superTopicOf: 44,204
   - subTopicOf

Non-taxonomic Relations:
   - contributesTo
   - relatedEquivalent

Alignments
-----------------
Direct mappings via sameAs relationships with:
    - DBpedia
    - Schema.org
    - Wikidata
    - Microsoft Academic Graph

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology.computer import ComputerOntology

   # Initialize and load ontology
   cso = ComputerOntology()

   cso.load("path/to/CSO.3.4.owl")

   # Extract datasets
   data = cso.extract()

    # Access specific relations
    term_types = data['term_typings']
    taxonomic_relations = data['type_taxonomies']
    non_taxonomic_relations = data['type_non_taxonomic_relations']
