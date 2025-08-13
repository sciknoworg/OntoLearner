

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Design
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - 2022-08-02
       * - **Creator**
         - Materials Design Division, National Institute for Materials Science (NIMS)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Materials Design Ontology (MDO) <https://github.com/LiUSemWeb/Materials-Design-Ontology/tree/master/>`_

Materials Design Ontology (MDO)
========================================================================================================

MDO is an ontology for materials design field, representing the domain knowledge specifically related     to solid-state physics and computational materials science.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 76
        * - **Total Edges**
          - 137
        * - **Root Nodes**
          - 14
        * - **Leaf Nodes**
          - 24
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 13
        * - **Individuals**
          - 2
        * - **Properties**
          - 13

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
          - 0.46
        * - **Depth Variance**
          - 0.33
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 8.00
        * - **Breadth Variance**
          - 28.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 2
        * - **Taxonomic Relations**
          - 3
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 2.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MDO

    ontology = MDO()
    ontology.load("path/to/MDO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
