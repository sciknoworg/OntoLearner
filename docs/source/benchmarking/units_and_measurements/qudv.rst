Quantities, Units, Dimensions and Values (QUDV)
==========================

Overview
--------
The SysML QUDV (Quantities, Units, Dimensions and Values) modelLibrary is specified in a UML/SysML
class/block diagram. In order to generalize its potential usage and alignment with other standardization efforts
concerning quantities and units, it is of interest to verify that the QUDV model can also be represented
in the form of an ontology using a formal ontology definition language.

:Domain: Units and Measurements
:Category: Units and Measurements
:Current Version: 2009-10-30
:Last Updated: 2009-10-30
:Creator: SysML
:License: Apache License 2.0
:Format: OWL
:Download: `Quantities, Units, Dimensions and Values (QUDV) Homepage <https://www.omgwiki.org/OMGSysML/doku.php?id=sysml-qudv:qudv_owl>`_

Graph Metrics
-------------
    - **Total Nodes**: 186
    - **Total Edges**: 491
    - **Root Nodes**: 4
    - **Leaf Nodes**: 20

Knowledge coverage
------------------
    - Classes: 33
    - Individuals: 0
    - Properties: 25

Hierarchical metrics
--------------------
    - **Maximum Depth**: 21
    - **Minimum Depth**: 0
    - **Average Depth**: 8.44
    - **Depth Variance**: 24.45

Breadth metrics
------------------
    - **Maximum Breadth**: 17
    - **Minimum Breadth**: 1
    - **Average Breadth**: 8.00
    - **Breadth Variance**: 22.18

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 9
    - **Non-taxonomic Relations**: 10
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import QUDV

    # Initialize and load ontology
    ontology = QUDV()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
