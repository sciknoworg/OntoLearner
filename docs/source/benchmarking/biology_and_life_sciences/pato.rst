.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Biology
       * - **Current Version**
         - 1.2
       * - **Last Updated**
         - 2025-02-01
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Phenotype and Trait Ontology (PATO) <https://terminology.tib.eu/ts/ontologies/PATO>`_

Phenotype and Trait Ontology (PATO)
========================================================================================================

The Phenotype and Trait Ontology (PATO) is a structured vocabulary designed to describe phenotypic qualities, attributes, and traits across a wide range of biological organisms. It provides a standardized framework for annotating and analyzing phenotypic data, enabling researchers to compare and integrate data across species and studies. PATO defines qualities such as color, shape, size, and behavior, and links them to specific biological entities and contexts. The ontology is widely used in genetics, developmental biology, and evolutionary studies to describe phenotypic variations and their underlying genetic and environmental factors. By providing a common language for phenotypic traits, PATO facilitates data sharing, integration, and computational analysis in the life sciences. The ontology is actively maintained and updated to incorporate new terms and relationships as research advances.

**Example Usage**:
Annotate a genetic study with PATO terms to describe phenotypic traits such as "PATO:0000323 (red coloration)" for a flower petal or "PATO:0000383 (increased size)" for a specific organ, enabling cross-study comparisons and meta-analyses.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 98691
        * - **Total Edges**
          - 259386
        * - **Root Nodes**
          - 16564
        * - **Leaf Nodes**
          - 45644
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 13544
        * - **Individuals**
          - 0
        * - **Properties**
          - 252

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 20
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.73
        * - **Depth Variance**
          - 2.02
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 35876
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 4564.14
        * - **Breadth Variance**
          - 92888669.36
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 30496
        * - **Non-taxonomic Relations**
          - 752
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PATO

    ontology = PATO()
    ontology.load("path/to/PATO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
