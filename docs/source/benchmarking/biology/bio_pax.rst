Biological Pathway Exchange (BioPAX) Ontology
==============================================

Overview
-----------------
Biological Pathway Exchange (BioPAX) is a standard language that aims to enable integration,
exchange, visualization and analysis of biological pathway data. Specifically, BioPAX supports
data exchange between pathway data groups and thus reduces the complexity of interchange between
data formats by providing an accepted standard format for pathway data. It is an open and collaborative effort
by the community of researchers, software developers, and institutions. BioPAX is defined in OWL DL
and is represented in the RDF/XML format

:Domain: Biology
:Category: Bioinformatics
:Current Version: 1.0
:Last Updated: 16 April 2015
:Producer:
:License:
:Format: OWL
:Download: `BioPAX Homepage <http://www.biopax.org/>`_
:Documentation: `BioPAX Documentation <http://www.biopax.org/>`_

Base Metrics
---------------
    - Classes: 69
    - Individuals: 0
    - Properties: 55

Graph Metrics:
------------------
    - **Total Nodes**: 555
    - **Root Nodes**: 68
    - **Leaf Nodes**: 200
    - **Maximum Depth**: 17
    - **Edges**: 1611

Dataset Statistics
-------------------
    - **Term Types**: 0
    - **Taxonomic Relations**: 292
    - **Non-taxonomic Relations**: 446
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BioPAX

   # Initialize and load ontology
   biopax = BioPAX()
   biopax.load("path/to/ontology.owl")
   # Extract datasets
   data = biopax.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
