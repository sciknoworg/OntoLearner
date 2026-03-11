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

The Data Catalog Vocabulary (DCAT) is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web. It provides a structured vocabulary for describing datasets, data services, and catalogs, supporting both theoretical and experimental research in data management.

The ontology employs a class-based modeling approach, defining classes for different types of datasets, data services, and catalogs, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. DCAT supports the integration of data from various sources, promoting interoperability and data-driven research in data management.

Typical applications of DCAT include the development of new data cataloging methods, the optimization of data management practices, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, DCAT enhances collaboration and innovation in the field of data management.

**Example Usage**:
Annotate a data catalog with DCAT terms to specify dataset types, data services, and catalog structures, enabling semantic search and integration with data management platforms.

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
