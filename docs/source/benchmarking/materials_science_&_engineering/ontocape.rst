Ontology of Computer-Aided Process Engineering (OntoCAPE)
==========================

Overview
--------
OntoCAPE is a large-scale ontology for the domain of Computer Aided Process Engineering (CAPE). Represented in a formal,
machine-interpretable ontology language, OntoCAPE captures consensual knowledge of the process engineering domain
in a generic way such that it can be reused and shared by groups of people and across software systems.
On the basis of OntoCAPE, novel software support for various engineering activities can be developed;
possible applications include the systematic management and retrieval of simulation models and design documents,
electronic procurement of plant equipment, mathematical modeling,
as well as the integration of design data from distributed sources.

:Domain: Materials Science & Engineering
:Category: Manufacturing
:Current Version: 2.0
:Last Updated: None
:Creator: RWTH Aachen University
:License: GNU General Public License.
:Format: OWL
:Download: `Ontology of Computer-Aided Process Engineering (OntoCAPE) Homepage <https://www.avt.rwth-aachen.de/cms/avt/forschung/sonstiges/software/~ipts/ontocape/?lidx=1>`_

Graph Metrics
-------------
    - **Total Nodes**: 11
    - **Total Edges**: 10
    - **Root Nodes**: 1
    - **Leaf Nodes**: 10

Knowledge coverage
------------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Hierarchical metrics
--------------------
    - **Maximum Depth**: 1
    - **Minimum Depth**: 0
    - **Average Depth**: 0.91
    - **Depth Variance**: 0.08

Breadth metrics
------------------
    - **Maximum Breadth**: 10
    - **Minimum Breadth**: 1
    - **Average Breadth**: 5.50
    - **Breadth Variance**: 20.25

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 0
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import OntoCAPE

    # Initialize and load ontology
    ontology = OntoCAPE()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
