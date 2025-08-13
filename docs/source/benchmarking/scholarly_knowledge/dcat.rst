

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

Data Catalog Vocabulary (DCAT) is an RDF vocabulary designed to facilitate interoperability     between data catalogs published on the Web. This document defines the schema and provides examples for its use.     DCAT enables a publisher to describe datasets and data services in a catalog using a standard model     and vocabulary that facilitates the consumption and aggregation of metadata from multiple catalogs.     This can increase the discoverability of datasets and data services. It also makes it possible     to have a decentralized approach to publishing data catalogs and makes federated search for datasets across catalogs     in multiple sites possible using the same query mechanism and structure. Aggregated DCAT metadata     can serve as a manifest file as part of the digital preservation process.

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
