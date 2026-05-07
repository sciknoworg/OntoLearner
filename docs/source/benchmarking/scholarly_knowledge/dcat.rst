.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Data Catalogs
       * - **Current Version**
         - 3.0
       * - **Last Updated**
         - 22 August 2024
       * - **Creator**
         - Digital Enterprise Research Institute (DERI)
       * - **License**
         - W3C Document License
       * - **Format**
         - rdf
       * - **Download**
         - `Download Data Catalog Vocabulary (DCAT) <https://www.w3.org/TR/vocab-dcat-3/>`_

Data Catalog Vocabulary (DCAT)
========================================================================================================

The Data Catalog Vocabulary (DCAT) is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web [#dcat-version3]_ [#dcat-cdif]_. It provides a structured semantic model for describing catalogs, datasets, dataset series, data services, distributions, catalog records, and related metadata, enabling dataset descriptions to be shared and processed in a machine-readable form [#dcat-version3]_. DCAT supports dataset discovery by allowing metadata from different catalogs to be aggregated, searched, exchanged, and reused through a common vocabulary [#dcat-version3]_ [#dcat-cdif]_.

The ontology defines classes and properties for describing catalog resources, including dataset titles, descriptions, publishers, themes, keywords, access URLs, download URLs, formats, licenses, temporal coverage, spatial coverage, and relationships between datasets, distributions, and services [#dcat-version3]_. These structured metadata descriptions support efficient retrieval, catalog integration, and interoperability across heterogeneous data infrastructures [#dcat-cdif]_.

Typical applications of DCAT include open data portals, research data repositories, government data catalogs, enterprise data management platforms, and cross-domain metadata exchange systems [#dcat-version3]_ [#dcat-cdif]_. By providing a standardized semantic framework, DCAT enhances data discoverability, metadata interoperability, catalog integration, and reuse across diverse data management environments [#dcat-version3]_.

**Example Usage**:
Annotate a data catalog with DCAT terms to describe datasets, data services, distributions, catalog records, publishers, access URLs, licenses, formats, and thematic categories. This enables semantic search, metadata aggregation, federated catalog discovery, and integration with data management platforms [#dcat-version3]_ [#dcat-cdif]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 987
        * - **Total Edges**
          - 1313
        * - **Root Nodes**
          - 7
        * - **Leaf Nodes**
          - 908
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 10
        * - **Individuals**
          - 0
        * - **Properties**
          - 39

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.42
        * - **Depth Variance**
          - 0.58
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 121
        * - **Minimum Breadth**
          - 7
        * - **Average Breadth**
          - 54.50
        * - **Breadth Variance**
          - 2135.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 8
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DCAT

    ontology = DCAT()
    ontology.load("path/to/DCAT-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#dcat-version3] W3C. 2024.
   "Data Catalog Vocabulary (DCAT) - Version 3."
   W3C Recommendation.
   Available at:
   `https://www.w3.org/TR/vocab-dcat-3/ <https://www.w3.org/TR/vocab-dcat-3/>`_

.. [#dcat-cdif] Cross-Domain Interoperability Framework. n.d.
   "DCAT Metadata."
   Available at:
   `https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/dcat.html <https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/dcat.html>`_
