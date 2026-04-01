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
[#efo-site]_ [#efo-faq]_. EFO integrates terms from multiple biological
ontologies, including UBERON for anatomy, ChEBI for chemical compounds,
and the Cell Ontology, in order to support the annotation, analysis,
and visualization of experimental data [#efo-site]_ [#efo-faq]_. It is
widely used for annotating datasets in EMBL-EBI resources and external
projects such as the NHGRI-EBI GWAS Catalog, and it is also used as the
core ontology for Open Targets [#efo-site]_ [#gwas-2023]_. EFO enables
semantic interoperability, data integration, and ontology-based querying
across diverse datasets, facilitating cross-study comparison and data
reuse [#efo-site]_ [#gwas-2018]_. The ontology is actively maintained at
EMBL-EBI and continues to evolve in response to new data types and
research needs [#efo-team]_ [#efo-site]_. By providing a unified
framework for describing experimental factors, EFO supports data
sharing, discovery, and knowledge integration in genomics,
transcriptomics, and related life science domains [#efo-site]_
[#gwas-2023]_.

**Example Usage**: Annotate a gene expression or association dataset with
EFO terms to specify experimental variables such as tissue type,
disease or phenotype, treatment, and assay-related factors, enabling
semantic search, cross-study comparison, and meta-analysis across
biological datasets [#efo-site]_ [#gwas-2018]_.

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

.. [#efo-faq] EMBL-EBI. n.d. "FAQ EFO."
   Available at: `https://www.ebi.ac.uk/efo/faq.html <https://www.ebi.ac.uk/efo/faq.html>`_

.. [#efo-team] EMBL-EBI. n.d. "Samples, Phenotypes and Ontologies."
   Available at: `https://www.ebi.ac.uk/about/teams/samples-phenotypes-ontologies/ <https://www.ebi.ac.uk/about/teams/samples-phenotypes-ontologies/>`_

.. [#gwas-2018] Buniello, A., MacArthur, J. A. L., Cerezo, M.,
   Harris, L. W., Hayhurst, J., Malangone, C., McMahon, A.,
   Morales, J., Mountjoy, E., Sollis, E., Suveges, D., Vrousgou, O.,
   Whetzel, P. L., Amode, R., Guillen, J. A., Riat, H. S.,
   Trevanion, S. J., Hall, P., Junkins, H., Flicek, P.,
   Burdett, T., Hindorff, L. A., Cunningham, F., and Parkinson, H.
   2019. "The NHGRI-EBI GWAS Catalog of Published Genome-Wide
   Association Studies, Targeted Arrays and Summary Statistics 2019."
   *Nucleic Acids Research* 47(D1): D1005-D1012.
   doi:10.1093/nar/gky1120
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC6323933/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC6323933/>`_

.. [#gwas-2023] Sollis, E., Mosaku, A., Abid, A., Buniello, A.,
   Cerezo, M., Gil, L., Groza, T., Güneş, O., Hall, P.,
   Hayhurst, J. D., McMahon, A., Mountjoy, E., Parton, A.,
   Paschall, J., Lopes, E. N., Sanseau, P., Shamout, S.,
   Sheth, T., Riat, H. S., et al. 2023. "NHGRI-EBI GWAS Catalog:
   Knowledgebase and Deposition Resource."
   *Nucleic Acids Research* 51(D1): D977-D985.
   doi:10.1093/nar/gkac1010
   Available at: `https://academic.oup.com/nar/article/51/D1/D977/6814460 <https://academic.oup.com/nar/article/51/D1/D977/6814460>`_
