

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Law
       * - **Category**
         - Legal Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2019-09
       * - **Creator**
         - Rhizomik
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Copyright Ontology (CopyrightOnto) <https://rhizomik.net/ontologies/copyrightonto/>`_

Copyright Ontology (CopyrightOnto)
========================================================================================================

The Copyright Ontology tries to formalise the copyright domain as a way to facilitate     automated (or computer-supported) copyright management through the whole content value chain,     as it is shaped by copyright law. Therefore, it does not focus just on the last step,     end-users permissions to consume content, like many rights languages and ontologies do.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 218
        * - **Total Edges**
          - 470
        * - **Root Nodes**
          - 6
        * - **Leaf Nodes**
          - 75
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 38
        * - **Individuals**
          - 7
        * - **Properties**
          - 12

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 8
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.93
        * - **Depth Variance**
          - 6.62
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 6
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 3.22
        * - **Breadth Variance**
          - 2.40
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 7
        * - **Taxonomic Relations**
          - 118
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 7.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CopyrightOnto

    ontology = CopyrightOnto()
    ontology.load("path/to/CopyrightOnto-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
