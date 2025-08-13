

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Basic
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - 2020
       * - **Creator**
         - University at Buffalo
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Basic Formal Ontology (BFO) <https://github.com/BFO-ontology/BFO-2020/>`_

Basic Formal Ontology (BFO)
========================================================================================================

The Basic Formal Ontology (BFO) is a small, upper-level ontology that describes     the basic types of entities in the world and how they relate to each other.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 538
        * - **Total Edges**
          - 1002
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 276
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 84
        * - **Individuals**
          - 0
        * - **Properties**
          - 40

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
          - 4.21
        * - **Depth Variance**
          - 6.56
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 54
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 19.79
        * - **Breadth Variance**
          - 293.74
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 66
        * - **Non-taxonomic Relations**
          - 5
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BFO

    ontology = BFO()
    ontology.load("path/to/BFO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
