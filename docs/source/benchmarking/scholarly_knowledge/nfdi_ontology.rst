The National Research Data Infrastructure Ontology (NFDIcore)
=============================================================

Overview
-----------------
The National Research Data Infrastructure (NFDI) initiative has led to the formation of various consortia,
each focused on developing a research data infrastructure tailored to its specific domain.
To ensure interoperability across these consortia, the NFDIcore ontology has been developed
as a mid-level ontology for representing metadata related to NFDI resources, including individuals,
organizations, projects, data portals, and more.

:Domain: Scholarly Knowledge
:Category: Research Data Infrastructure
:Current Version: 3.0.0
:Last Updated: 2025-02-07
:Producer: Jörg Waitelonis, Oleksandra Bruns, Tabea Tietz, Etienne Posthumus, Hossein Beygi Nasrabadi, Harald Sack
:License: Creative Commons 1.0
:Format: RDF/XML, TTL, JSON-LD
:Download: `NFDIcore Homepage <https://ise-fizkarlsruhe.github.io/nfdicore/>`_
:Documentation: `NFDIcore Documentation <https://ise-fizkarlsruhe.github.io/nfdicore/>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 1849
    - **Root Nodes**: 84
    - **Leaf Nodes**: 1029
    - **Maximum Depth**:
    - **Edges**: 3525

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 391
    - **Non-taxonomic Relations**: 33
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import NFDIcore

   # Initialize and load ontology
   nfdi = NFDIcore()
   nfdi.load("path/to/ontology.owl")
   # Extract datasets
   data = nfdi.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
