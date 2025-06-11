Agronomy Ontology (AgrO)
========================================================================================================================

Overview
--------
An ontology is a formal representation of a disciplinary domain, representing a semantic standard
that can be employed to annotate data where key concepts are defined, as well as the relationships
that exist between those concepts (Gruber, 2009). Ontologies provide a common language for different kinds of data
to be easily interpretable and interoperable allowing easier aggregation and analysis. The Agronomy Ontology (AgrO)
provides terms from the agronomy domain that are semantically organized and can facilitate the collection,
storage and use of agronomic data, enabling easy interpretation and reuse of the data by humans and machines alike.
To fully understand the implications of varying practices within cropping systems and derive insights,
it is often necessary to pull together information from data in different disciplinary domains.
For example, data on field management, soil, weather and crop phenotypes may need to be aggregated
to assess performance of particular crop under different management interventions. However,
agronomic data are often collected, described, and stored in inconsistent ways, impeding data comparison, mining,
interpretation reuse. The use of standards for metadata and data annotation play a key role
in addressing these challenges. While the CG Core Metadata Schema provides a metadata standard
to describe agricultural datasets, the Agronomy Ontology enables the description
of agronomic data variables using standard terms.

:Domain: Agriculture
:Category: Agronomy
:Current Version: 1.0
:Last Updated: 2022-11-02
:Creator: The Crop Ontology Consortium
:License: Creative Commons 4.0
:Format: RDF
:Download: `Agronomy Ontology (AgrO) Homepage <https://agroportal.lirmm.fr/ontologies/AGRO?p=summary>`_

Graph Metrics
-------------
    - **Total Nodes**: 31951
    - **Total Edges**: 80144
    - **Root Nodes**: 5369
    - **Leaf Nodes**: 14046

Knowledge coverage
------------------
    - Classes: 5778
    - Individuals: 326
    - Properties: 209

Hierarchical metrics
--------------------
    - **Maximum Depth**: 22
    - **Minimum Depth**: 0
    - **Average Depth**: 1.92
    - **Depth Variance**: 6.01

Breadth metrics
------------------
    - **Maximum Breadth**: 7562
    - **Minimum Breadth**: 6
    - **Average Breadth**: 1033.17
    - **Breadth Variance**: 4403827.97

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: 71
    - **Taxonomic Relations**: 10931
    - **Non-taxonomic Relations**: 1699
    - **Average Terms per Type**: 4.18

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import AgrO

    # Initialize and load ontology from local file
    ontology = AgrO()
    ontology.load("path/to/ontology.RDF")

    # Or load from a Hugging Face repository
    ontology = AgrO()
    ontology.load()

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
