Ontology of Computer-Aided Process Engineering (OntoCAPE)
=========================================================

Overview
--------
OntoCAPE is a large-scale ontology for the domain of Computer Aided Process Engineering (CAPE). Represented in a formal,
machine-interpretable ontology language, OntoCAPE captures consensual knowledge of the process engineering domain
in a generic way such that it can be reused and shared by groups of people and across software systems.
On the basis of OntoCAPE, novel software support for various engineering activities can be developed;
possible applications include the systematic management and retrieval of simulation models and design documents,
electronic procurement of plant equipment, mathematical modeling,
as well as the integration of design data from distributed sources.

:Domain: Computer Aided Process Engineering
:Category: Scholarly Knowledge
:Current Version: 2.0
:Last Updated:
:Producer: RWTH Aachen University
:License: GNU General Public License.
:Format: OWL
:Download: `OntoCAPE Homepage <https://www.avt.rwth-aachen.de/cms/avt/forschung/sonstiges/software/~ipts/ontocape/?lidx=1>`_
:Documentation: `OntoCAPE Documentation <https://www.avt.rwth-aachen.de/cms/avt/forschung/sonstiges/software/~ipts/ontocape/?lidx=1>`_

Base Metrics
-------------
    - Classes:
    - Individuals:
    - Properties:

Schema Metrics
---------------
    - Attribute Richness:
    - Inheritance Richness:
    - Relationship Richness:

Graph Metrics
----------------
    - **Total Nodes**: 3979
    - **Root Nodes**: 146
    - **Leaf Nodes**: 856
    - **Maximum Depth**:
    - **Edges**: 9686

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 299
    - **Taxonomic Relations**: 4810
    - **Non-taxonomic Relations**: 645
    - **Average Terms per Type**: 7.29

Usage Example
-----------------
.. code-block:: python

   from ontolearner.ontology import OntoCAPE

   # Initialize and load ontology
   cape = OntoCAPE()
   cape.load("path/to/ontology.owl")
   # Extract datasets
   data = cape.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_non_taxonomic_relations
