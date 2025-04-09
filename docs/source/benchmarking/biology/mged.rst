The MGED Ontology
=================

Overview
-----------------
Concepts, definitions, terms, and resources for standardized description of a microarray experiment in support of MAGE v.1.
The MGED ontology is divided into the MGED Core ontology which is intended to be stable and in synch with MAGE v.1;
and the MGED Extended ontology which adds further associations and classes not found in MAGE v.1

:Domain: Materials Science and Engineering
:Category: Domain Ontology
:Current Version: 1.3.1.1
:Last Updated: Feb. 9, 2007
:Producer: Chris Stoeckert, Helen Parkinson, Trish Whetzel, Paul Spellman, Catherine A. Ball, Joseph White, John Matese, Liju Fan, Gilberto Fragoso, Mervi Heiskanen, Susanna Sansone, Helen Causton, Laurence Game, Chris Taylor
:License: CC-BY-4.0
:Format: OWL
:Download: `MGED Homepage <https://mged.sourceforge.net/ontologies/MGEDontology.php/>`_
:Documentation: `MGED Documentation <https://mged.sourceforge.net/ontologies/MGEDontology.php>`_

Base Metrics
---------------
    - Classes: 233
    - Individuals: 681
    - Properties: 14
    - Axioms: 0

Graph Metrics:
------------------
    - **Total Nodes**: 3427
    - **Root Nodes**: 730
    - **Leaf Nodes**: 2171
    - **Maximum Depth**: 13
    - **Edges**: 5101

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 744
    - **Taxonomic Relations**: 1536
    - **Non-taxonomic Relations**: 6
    - **Average Terms per Type**: 16.53


Usage Example
--------------
.. code-block:: python

    from ontolearner.ontology import MGED

    # Initialize and load ontology
    ontology = MGED()
    ontology.load("new/mged.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
