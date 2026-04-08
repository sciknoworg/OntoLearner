

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - 1.1.0
       * - **Last Updated**
         - 2017-10-19
       * - **Creator**
         - Daniel Schober
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Nuclear Magnetic Resonance Controlled Vocabulary (NMRCV) <https://terminology.tib.eu/ts/ontologies/NMRCV>`_

Nuclear Magnetic Resonance Controlled Vocabulary (NMRCV)
========================================================================================================

The Nuclear Magnetic Resonance Controlled Vocabulary (NMRCV) is an
MSI-approved controlled vocabulary developed to support standardized
annotation of nuclear magnetic resonance data and experiments
[#nmr-bioportal]_ [#nmrml-paper]_. It supports the nmrML XML format, a
vendor-agnostic open standard for the description, storage, and
exchange of raw NMR data, by providing standardized terms for
instrumentation, acquisition parameters, sample context, and other
experimental metadata [#nmrml-paper]_ [#nmr-bioportal]_. The vocabulary
serves as a flexible semantic layer alongside the nmrML schema,
allowing terminology to evolve independently while still supporting
semantic validation and interoperable data exchange [#nmrml-paper]_.
By providing a shared terminology for NMR experiments, NMRCV improves
semantic consistency, reproducibility, validation, and cross-study
integration across metabolomics and analytical chemistry workflows
[#nmr-bioportal]_ [#nmrml-paper]_.

**Example Usage**: Annotate an nmrML file with NMRCV terms to specify
the instrument type, pulse sequence, sample conditions, acquisition
parameters, and processing metadata, enabling standardized exchange,
validation, and cross-study comparison of NMR datasets
[#nmrml-paper]_ [#nmr-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1596
        * - **Total Edges**
          - 3951
        * - **Root Nodes**
          - 184
        * - **Leaf Nodes**
          - 662
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 757
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 5
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.01
        * - **Depth Variance**
          - 0.72
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 273
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 103.83
        * - **Breadth Variance**
          - 10836.47
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 792
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import NMRCV

    ontology = NMRCV()
    ontology.load("path/to/NMRCV-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#nmr-bioportal] NCBO BioPortal. n.d. "NMR-Controlled Vocabulary."
   Available at:
   `https://bioportal.bioontology.org/ontologies/NMR <https://bioportal.bioontology.org/ontologies/NMR>`_

.. [#nmrml-paper] Schober, D., Jacob, D., Wilson, M., Cruz, J. A.,
   Marcu, A., Grant, J. R., Moing, A., Deborde, C., de Figueiredo, L. F.,
   Haug, K., Rocca-Serra, P., Easton, J., Ebbels, T. M. D., Hao, J.,
   Ludwig, C., Nasi, N., Narayana, V. K., Sansone, S.-A., Viant, M. R.,
   and Wishart, D. S. 2018.
   "nmrML: A Community Supported Open Data Standard for the Description,
   Storage, and Exchange of NMR Data."
   *Analytical Chemistry* 90(1): 649-656.
   doi:10.1021/acs.analchem.7b02795
