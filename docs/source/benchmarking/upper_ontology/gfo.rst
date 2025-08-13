

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Upper Ontology
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2024-11-18
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download General Formal Ontology (GFO) <https://onto-med.github.io/GFO/release/2024-11-18/index-en.html>`_

General Formal Ontology (GFO)
========================================================================================================

The General Formal Ontology is a top-level ontology for conceptual modeling,     which is being constantly further developed by Onto-Med. It includes elaborations of categories like objects,     processes, time and space, properties, relations, roles, functions, facts, and situations.     Moreover, we are working on an integration with the notion of levels of reality in order     to more appropriately capture entities in the material, mental, and social areas.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 296
        * - **Total Edges**
          - 708
        * - **Root Nodes**
          - 42
        * - **Leaf Nodes**
          - 71
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 94
        * - **Individuals**
          - 1
        * - **Properties**
          - 67

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 12
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.94
        * - **Depth Variance**
          - 3.22
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 88
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 21.23
        * - **Breadth Variance**
          - 874.02
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1
        * - **Taxonomic Relations**
          - 143
        * - **Non-taxonomic Relations**
          - 34
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GFO

    ontology = GFO()
    ontology.load("path/to/GFO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
