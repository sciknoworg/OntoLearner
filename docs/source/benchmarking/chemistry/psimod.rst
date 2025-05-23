Protein Modifications Ontology (PSIMOD)
========================================================================================================================

Overview
--------
PSI-MOD is an ontology developed by the Proteomics Standards Initiative (PSI) that describes protein chemical modifications,
logically linked by an is_a relationship in such a way as to form a direct acyclic graph (DAG).
The PSI-MOD ontology has more than 45 top-level nodes, and provides alternative hierarchical paths
for classifying protein modifications either by the molecular structure of the modification,
or by the amino acid residue that is modified.

:Domain: Chemistry
:Category: Protein Modifications
:Current Version: 1.031.6
:Last Updated: 2022-06-13
:Creator: None
:License: Creative Commons Attribution 4.0
:Format: OWL
:Download: `Protein Modifications Ontology (PSIMOD) Homepage <https://github.com/HUPO-PSI/psi-mod-CV>`_

Graph Metrics
-------------
    - **Total Nodes**: 28523
    - **Total Edges**: 86380
    - **Root Nodes**: 9338
    - **Leaf Nodes**: 16902

Knowledge coverage
------------------
    - Classes: 2098
    - Individuals: 0
    - Properties: 4

Hierarchical metrics
--------------------
    - **Maximum Depth**: 4
    - **Minimum Depth**: 0
    - **Average Depth**: 0.95
    - **Depth Variance**: 0.60

Breadth metrics
------------------
    - **Maximum Breadth**: 11284
    - **Minimum Breadth**: 4
    - **Average Breadth**: 5684.00
    - **Breadth Variance**: 22690827.20

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 7913
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.00

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import PSIMOD

    # Initialize and load ontology
    ontology = PSIMOD()
    ontology.load("path/to/ontology.OWL")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
