

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Industry
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2025-02-21
       * - **Creator**
         - Martin Hepp
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Product Types Ontology (PTO) <http://www.productontology.org/>`_

Product Types Ontology (PTO)
========================================================================================================

The Product Types Ontology is designed to be used in combination with GoodRelations,     a standard vocabulary for the commercial aspects of offers.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4577
        * - **Total Edges**
          - 14125
        * - **Root Nodes**
          - 12
        * - **Leaf Nodes**
          - 1012
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1002
        * - **Individuals**
          - 3002
        * - **Properties**
          - 0

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.92
        * - **Depth Variance**
          - 0.87
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 12
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 8.33
        * - **Breadth Variance**
          - 14.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 3000
        * - **Taxonomic Relations**
          - 3996
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 3000.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PTO

    ontology = PTO()
    ontology.load("path/to/PTO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
