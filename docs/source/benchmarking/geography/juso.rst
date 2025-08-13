

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Geography
       * - **Category**
         - geographical knowledge
       * - **Current Version**
         - 0.1.1
       * - **Last Updated**
         - 2015-11-10
       * - **Creator**
         - James G. Kim, LiST Inc.
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Juso Ontology (Juso) <https://rdfs.co/juso/0.1.1/html>`_

Juso Ontology (Juso)
========================================================================================================

Juso Ontology is a Web vocabulary for describing geographical addresses and features.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 319
        * - **Total Edges**
          - 607
        * - **Root Nodes**
          - 19
        * - **Leaf Nodes**
          - 227
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 30
        * - **Individuals**
          - 0
        * - **Properties**
          - 24

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
          - 1.93
        * - **Depth Variance**
          - 1.85
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 37
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 21.33
        * - **Breadth Variance**
          - 132.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 61
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Juso

    ontology = Juso()
    ontology.load("path/to/Juso-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
