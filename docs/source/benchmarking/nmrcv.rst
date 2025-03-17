The Nuclear Magnetic Resonance Controlled Vocabulary (NMRCV)
============================================================

Overview
-----------------
This artefact is an MSI-approved controlled vocabulary primarily developed under COSMOS EU and PhenoMeNal EU governance.
The nmrCV is supporting the nmrML XML format with standardized terms. nmrML is a vendor agnostic open access NMR raw data standard.
Its primaly role is analogous to the mzCV for the PSI-approved mzML XML format. It uses BFO2.0 as its Top level.
This CV was derived from two predecessors (The NMR CV from the David Wishart Group, developed by Joseph Cruz)
and the MSI nmr CV developed by Daniel Schober at the EBI. This simple taxonomy of terms (no DL semantics used)
serves the nuclear magnetic resonance markup language (nmrML) with meaningful descriptors to amend the nmrML xml file
with CV terms. Metabolomics scientists are encouraged to use this CV to annotrate their raw and experimental context data,
i.e. within nmrML. The approach to have an exchange syntax mixed of an xsd and CV stems from the PSI mzML effort.
The reason to branch out from an xsd into a CV is, that in areas where the terminology is likely to change faster
than the nmrML xsd could be updated and aligned, an externally and decentrallised maintained CV can accompensate
for such dynamics in a more flexible way. A second reason for this set-up is that semantic validity of CV terms
used in an nmrML XML instance (allowed CV terms, position/relation to each other, cardinality) can be validated
by rule-based proprietary validators: By means of cardinality specifications and XPath expressions defined
in an XML mapping file (an instances of the CvMappingRules.xsd ), one can define what ontology terms are allowed
in a specific location of the data model.

:Domain: Chemistry
:Category: Chemistry
:Current Version: 1.1.0
:Last Updated: 2017-10-19
:Producer: Daniel Schober
:License: Creative Commons 4.0
:Format: OWL
:Download: `nmrCV Homepage <https://terminology.tib.eu/ts/ontologies/NMRCV>`_
:Documentation: `nmrCV Documentation <https://terminology.tib.eu/ts/ontologies/NMRCV>`_

Base Metrics
---------------
    - Classes: 792
    - Properties: 46
    - Individuals: 0

Graph Metrics:
------------------
    - **Nodes**: 1596
    - **Root Nodes**: 184
    - **Leaf Nodes**: 662
    - **Maximum Depth**: 8
    - **Edges**: 3951

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 792
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
-----------------
.. code-block:: python

    from ontolearner.ontology.nmrcv import NMRCV

    # Initialize and load ontology
    nmrcv = NMRCV()
    # Load ontology from file
    nmrcv.load("path/to/ontology.owl")
    # Extract datasets
    data = nmrcv.extract()
    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
