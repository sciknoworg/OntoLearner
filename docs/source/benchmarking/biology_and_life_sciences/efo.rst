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

The Experimental Factor Ontology (EFO) is a comprehensive ontology
developed to provide systematic, standardized descriptions of
experimental variables and factors in biological and biomedical research
[#efo-site]_ [#efo-paper]_. EFO integrates terms from multiple
biological ontologies in order to support the annotation, analysis, and
visualization of experimental data [#efo-site]_ [#efo-paper]_. It
provides a semantic framework for describing sample variables and
experimental conditions, enabling consistent data annotation and
interoperability across diverse datasets [#efo-paper]_ [#efo-site]_.
EFO is maintained by EMBL-EBI and serves as an important ontology
resource for biological data integration and reuse [#efo-site]_.
By providing a unified framework for describing experimental factors,
EFO supports data sharing, discovery, and knowledge integration in
genomics, transcriptomics, and related life science domains
[#efo-site]_ [#efo-paper]_.

**Example Usage**: Annotate a gene expression or association dataset with
EFO terms to specify experimental variables such as tissue type,
disease or phenotype, treatment, and assay-related factors, enabling
semantic search, cross-study comparison, and meta-analysis across
biological datasets [#efo-paper]_ [#efo-site]_.

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

References
----------

.. [#efo-site] EMBL-EBI. n.d. "The Experimental Factor Ontology."
   Available at: `https://www.ebi.ac.uk/efo/ <https://www.ebi.ac.uk/efo/>`_

.. [#efo-paper] Malone, J., Holloway, E., Adamusiak, T.,
   Kapushesky, M., Zheng, J., Kolesnikov, N., Zhukova, A.,
   Brazma, A., and Parkinson, H. 2010.
   "Modeling Sample Variables with an Experimental Factor Ontology."
   *Bioinformatics* 26(8): 1112-1118.
   Available at:
   https://academic.oup.com/bioinformatics/article/26/8/1112/208992
