The Experimental Factor Ontology (EFO)
=======================================

Overview
-----------------
The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables
available in EBI databases, and for projects such as the GWAS catalog. It combines parts of several biological ontologies,
such as UBERON anatomy, ChEBI chemical compounds, and Cell Ontology. The scope of EFO is to support the annotation,
analysis and visualization of data handled by many groups at the EBI and as the core ontology for Open Targets.
EFO is developed by the EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT).

:Domain: Biology
:Category: Biology
:Current Version: 3.75.0
:Last Updated: 2025-02-17
:Producer:
:License: Apache 2.0
:Format: OWL, TTL, CSV, NT
:Download: `EFO Homepage <https://www.ebi.ac.uk/efo>`_
:Documentation: `EFO Documentation <https://www.ebi.ac.uk/efo>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Nodes**:
    - **Root Nodes**:
    - **Leaf Nodes**:
    - **Maximum Depth**:
    - **Edges**:

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**:
    - **Taxonomic Relations**:
    - **Non-taxonomic Relations**:
    - **Average Terms per Type**:

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import EFO

   # Initialize and load ontology
   efo = EFO()
   efo.load("path/to/ontology.owl")
   # Extract datasets
   data = efo.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
