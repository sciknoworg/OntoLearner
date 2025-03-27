Proteomics Standards Initiative (PSI) Protein Modifications Ontology (PSI-MOD)
==============================================================================

Overview
-----------------
PSI-MOD is an ontology consisting of terms that describe protein chemical modifications,
logically linked by an is_a relationship in such a way as to form a direct acyclic graph (DAG).
The PSI-MOD ontology has more than 45 top-level nodes, and provides alternative hierarchical paths
for classifying protein modifications either by the molecular structure of the modification,
or by the amino acid residue that is modified.

:Domain: Chemistry
:Category: Protein Modifications
:Current Version: 1.031.6
:Last Updated: 2022-06-13
:Producer:
:License: Creative Commons Attribution 4.0
:Format: OWL
:Download: `PSI-MOD Homepage <https://github.com/HUPO-PSI/psi-mod-CV>`_
:Documentation: `PSI-MOD Documentation <https://terminology.tib.eu/ts/ontologies/MOD>`_

Base Metrics
---------------
    - Classes: 2098
    - Individuals: 0
    - Properties: 47

Graph Metrics:
------------------
    - **Total Nodes**: 28523
    - **Root Nodes**: 9338
    - **Leaf Nodes**: 16902
    - **Maximum Depth**: 10
    - **Edges**: 86380

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 8347
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python
    from ontolearner.ontology import PSIMOD

    # Initialize and load ontology
    ontology = PSIMOD()
    ontology.load("path/to/ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
