

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Molecular Biology, Genetics
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2024-11-03
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Gene Ontology (GO) <https://geneontology.org/docs/download-ontology/>`_

Gene Ontology (GO)
========================================================================================================

The Gene Ontology (GO) is a comprehensive resource that provides
structured controlled vocabularies for the annotation of gene products
with respect to their molecular function, cellular component, and
biological process roles [#go-site]_ [#go-2026]_. Developed
collaboratively by the Gene Ontology Consortium, GO enables consistent
annotation of genes and proteins across diverse species and databases
[#go-2026]_ [#go-site]_. The ontology is organized into three
hierarchical namespaces: Biological Process, describing the larger
biological objectives to which a gene product contributes; Molecular
Function, characterizing its molecular activity; and Cellular
Component, indicating where that activity occurs [#go-site]_
[#go-2026]_. GO supports biological data analysis by enabling
researchers to compare gene functions, identify enriched biological
processes or functions in genomics datasets, and understand
relationships among genes and gene products in biological systems
[#go-2026]_ [#go-site]_. By providing a shared semantic framework for
functional annotation, GO facilitates data integration, comparative
genomics, and computational analysis across the life sciences
[#go-2026]_ [#go-site]_.

**Example Usage**: Annotate a protein such as TP53 with GO terms for
biological process, molecular function, and cellular component, for
example terms related to apoptotic process, DNA binding, and nucleus, to
enable standardized functional annotation, enrichment analysis, and
cross-database comparison [#go-site]_ [#go-2026]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 534820
        * - **Total Edges**
          - 1419487
        * - **Root Nodes**
          - 133995
        * - **Leaf Nodes**
          - 293179
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 62046
        * - **Individuals**
          - 0
        * - **Properties**
          - 9

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.24
        * - **Depth Variance**
          - 1.08
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 204650
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 66849.38
        * - **Breadth Variance**
          - 6433980645.23
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 156430
        * - **Non-taxonomic Relations**
          - 30
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GO

    ontology = GO()
    ontology.load("path/to/GO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#go-site] Gene Ontology Consortium. n.d. "The Gene Ontology Resource."
   Available at: `https://geneontology.org/ <https://geneontology.org/>`_

.. [#go-2026] The Gene Ontology Consortium. 2026.
   "The Gene Ontology Knowledgebase in 2026."
   *Nucleic Acids Research* 54(D1): D1779-D1790.
   doi:10.1093/nar/gkaf1292
   Available at: `https://academic.oup.com/nar/article/54/D1/D1779/8383826 <https://academic.oup.com/nar/article/54/D1/D1779/8383826>`_
