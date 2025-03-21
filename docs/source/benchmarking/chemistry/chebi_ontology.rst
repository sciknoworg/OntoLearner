Chemical Entities of Biological Interest Ontology (ChEBI)
=========================================================

Overview
-----------------
Chemical Entities of Biological Interest (ChEBI) is a dictionary of molecular entities
focused on ‘small’ chemical compounds. The term ‘molecular entity’ refers to any constitutionally
or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer, etc.,
identifiable as a separately distinguishable entity. The molecular entities in question
are either products of nature or synthetic products used to intervene in the processes of living organisms.
ChEBI incorporates an ontological classification, whereby the relationships between molecular entities
or classes of entities and their parents and/or children are specified.

:Domain: Chemistry
:Category: Chemical Entities
:Current Version: 239
:Last Updated: 01/01/2025
:Producer:
:License: Creative Commons 4.0
:Format: OWL, OBO, JSON
:Download: `ChEBI Homepage <https://www.ebi.ac.uk/chebi/>`_
:Documentation: `ChEBI Documentation <https://www.ebi.ac.uk/chebi>`_

Base Metrics
---------------
    - Classes: 220,816
    - Individuals: 0
    - Properties: 47

Graph Metrics:
------------------
    - **Total Nodes**: 202549
    - **Root Nodes**: 188890
    - **Leaf Nodes**: 456
    - **Maximum Depth**: 23
    - **Edges**: 685993

Dataset Statistics
-------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 739976
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import ChEBI

   # Initialize and load ontology
   chebi = ChEBI()
   chebi.load("path/to/ontology.owl")
   # Extract datasets
   data = chebi.extract()
   # Access specific relations
   term_types = data.term_typings
