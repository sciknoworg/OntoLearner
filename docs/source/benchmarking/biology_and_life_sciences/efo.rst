.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Biology
       * - **Current Version**
         - 3.75.0
       * - **Last Updated**
         - 2025-02-17
       * - **Creator**
         - None
       * - **License**
         - Apache 2.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Experimental Factor Ontology (EFO) <https://www.ebi.ac.uk/efo>`_

Experimental Factor Ontology (EFO)
========================================================================================================

The Experimental Factor Ontology (EFO) is a comprehensive ontology developed to provide systematic, standardized descriptions of experimental variables and factors in biological and biomedical research. EFO integrates terms from multiple biological ontologies, including UBERON (anatomy), ChEBI (chemical compounds), and Cell Ontology, to support the annotation, analysis, and visualization of experimental data. It is widely used for annotating datasets in EBI databases, the GWAS catalog, and as the core ontology for Open Targets. EFO enables semantic interoperability, data integration, and advanced queries across diverse experimental datasets, facilitating reproducibility and meta-analysis. The ontology is actively maintained by the EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT) and is continuously updated to reflect new experimental techniques and research needs. By providing a unified framework for describing experimental factors, EFO supports data sharing, discovery, and knowledge integration in genomics, transcriptomics, and other life sciences domains.

**Example Usage**:
Annotate a gene expression dataset with EFO terms to specify experimental variables such as tissue type, disease state, treatment, and assay platform, enabling cross-study comparison and meta-analysis.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 948012
        * - **Total Edges**
          - 2874304
        * - **Root Nodes**
          - 308011
        * - **Leaf Nodes**
          - 443836
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 88311
        * - **Individuals**
          - 0
        * - **Properties**
          - 87

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.24
        * - **Depth Variance**
          - 2.14
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 308011
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 62043.14
        * - **Breadth Variance**
          - 11287110481.98
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 162458
        * - **Non-taxonomic Relations**
          - 10335
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EFO

    ontology = EFO()
    ontology.load("path/to/EFO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
