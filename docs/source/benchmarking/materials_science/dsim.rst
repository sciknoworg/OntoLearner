Dislocation Simulation and Model Ontology (DSIM)
=================================================

Overview
-----------------
Dislocation simulation and model ontology (DSIM) is an ontology developed to model various concepts
and relationships in the discrete dislocation dynamics domain and microscopy techniques
used in the dislocation domain. The various concepts are the numerical representation
of dislocation applied in the dislocation dynamic simulation and the pictorial concept of pixel
applied in representing dislocation in the experimental image, eg., TEM image, SEM image, and FIM image.

:Domain: Materials Science and Engineering
:Category: Materials Science
:Current Version: 1.0
:Last Updated: 17.08.2023
:Creator: Ahmad Zainul Ihsan
:License: Creative Commons Attribution 3.0 Unported (CC BY 3.0)
:Format: OWL/XML
:Download: `DSIM Homepage <https://github.com/OCDO/DSIM>`_
:Documentation: `DSIM Documentation <https://github.com/OCDO/DSIM>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics
------------------
    - **Total Nodes**: 313
    - **Root Nodes**: 19
    - **Leaf Nodes**: 119
    - **Maximum Depth**: 7
    - **Edges**: 673

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 164
    - **Non-taxonomic Relations**: 6
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import DSIM

    # Initialize and load ontology
    ontology = DSIM()
    ontology.load("path/to/dsim.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
