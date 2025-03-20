Human Disease Ontology (DOID)
==============================

Overview
-----------------
The Disease Ontology has been developed as a standardized ontology for human disease
with the purpose of providing the biomedical community with consistent,
reusable and sustainable descriptions of human disease terms,
phenotype characteristics and related medical vocabulary disease concepts.

:Domain: Biology, Life Sciences
:Category: Human Diseases
:Current Version:
:Last Updated: 2024-12-18
:Producer: The Open Biological and Biomedical Ontology Foundry
:License: Creative Commons 1.0
:Format: OWL
:Download: `DO Homepage <http://purl.obolibrary.org/obo/doid/releases/2024-12-18/doid.owl>`_
:Documentation: `DO Documentation <https://bioportal.bioontology.org/ontologies/DOID>`_

Base Metrics
---------------
    - Classes: 18,839
    - Individuals: 0
    - Properties: 45
    - Annotation Assertions:

Graph Metrics:
------------------
    - **Total Nodes**: 14281
    - **Root Nodes**: 11839
    - **Leaf Nodes**: 3
    - **Maximum Depth**: 12
    - **Edges**: 41351

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 41569
    - **Non-taxonomic Relations**: 25
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology.disease import DiseaseOntology

   # Initialize and load ontology
   do = DiseaseOntology()
   do.load("path/to/ontology.owl")
   # Extract datasets
   data = do.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
