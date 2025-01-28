Computer Science Ontology (CSO)
==============================

Overview
-----------------
The Computer Science Ontology (CSO) is a large-scale ontology of research areas in computer science.
It provides a comprehensive vocabulary of research topics in computing, organized in a hierarchical structure.

:Domain: Computer Science
:Category: Research Areas
:Current Version: 3.4
:Last Updated: date
:Producer: Knowledge Media Institute, Open University
:License: Creative Commons 4.0
:Format: OWL, TTL, CSV, NT
:Download: `CSO Homepage <https://cso.kmi.open.ac.uk/home>`_
:Documentation: `CSO Documentation <https://cso.kmi.open.ac.uk/about>`_

Base Metrics
---------------
    - Axioms: {axioms}
    - Classes: {class_count}
    - Object Properties: {op_count}
    - Data Properties: {dp_count}
    - Annotation Assertions: {ann_count}
    - DL Expressivity: {dl_expr}

Schema Metrics
---------------
    - Attribute Richness: {attr_richness}
    - Inheritance Richness: {inh_richness}
    - Relationship Richness: {rel_richness}
    - Axiom/Class Ratio: {acr}
    - Equivalence Ratio: {eq_ratio}

Graph Metrics:
------------------
    - **Total Nodes**: 14,604
    - **Root Nodes**: 9
    - **Leaf Nodes**: 8,353
    - **Maximum Depth**: 11
    - **Edges**: 93,289
    - Average Depth: {avg_depth}
    - External Classes: {ext_class_count}
    - Maximum Breadth: {max_breadth}
    - Average Breadth: {avg_breadth}
    - Tangledness: {tangledness}

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

Class Axioms
   - relatedEquivalent (represents equivalent classes/synonyms)

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
