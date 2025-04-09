Quantities, Units, Dimensions and Values (QUDV)
===============================================

Overview
-----------------
The SysML QUDV (Quantities, Units, Dimensions and Values) modelLibrary is specified in a UML/SysML
class/block diagram. In order to generalize its potential usage and alignment with other standardization efforts
concerning quantities and units, it is of interest to verify that the QUDV model can also be represented
in the form of an ontology using a formal ontology definition language.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 2009-10-30
:Last Updated: 2009-10-30
:Creator: SysML
:License: `Apache License 2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_
:Format: OWL
:Download: `QUDV Homepage <https://www.omgwiki.org/OMGSysML/doku.php?id=sysml-qudv:qudv_owl>`_
:Documentation: `QUDV Documentation <https://www.omgwiki.org/OMGSysML/doku.php?id=sysml-qudv:qudv_owl>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 186
    - **Root Nodes**: 4
    - **Leaf Nodes**: 20
    - **Maximum Depth**: 21
    - **Edges**: 491

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 9
    - **Non-taxonomic Relations**: 10
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

    from ontolearner.ontology import QUDV

    # Initialize and load ontology
    ontology = QUDV()
    ontology.load("path/to/qudv.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
