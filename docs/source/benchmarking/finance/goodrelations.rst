

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Finance
       * - **Category**
         - E-commerce
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2011-10-01
       * - **Creator**
         - Martin Hepp
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Good Relations Language Reference (GoodRelations) <https://www.heppnetz.de/ontologies/goodrelations/v1>`_

Good Relations Language Reference (GoodRelations)
========================================================================================================

GoodRelations is a standardized vocabulary (also known as "schema", "data dictionary",     or "ontology") for product, price, store, and company data that can (1) be embedded     into existing static and dynamic Web pages and that (2) can be processed by other computers.     This increases the visibility of your products and services in the latest generation     of search engines, recommender systems, and other novel applications.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 677
        * - **Total Edges**
          - 1816
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 206
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 98
        * - **Individuals**
          - 47
        * - **Properties**
          - 102

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 30
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 7.81
        * - **Depth Variance**
          - 73.22
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 33
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.77
        * - **Breadth Variance**
          - 55.21
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 46
        * - **Taxonomic Relations**
          - 25
        * - **Non-taxonomic Relations**
          - 264
        * - **Average Terms per Type**
          - 5.75
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GoodRelations

    ontology = GoodRelations()
    ontology.load("path/to/GoodRelations-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
