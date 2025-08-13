

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - Sep 15, 2022
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - ttl
       * - **Download**
         - `Download Material Science Lab Equipment Ontology (MSLE) <https://github.com/MehrdadJalali-AI/MSLE-Ontology>`_

Material Science Lab Equipment Ontology (MSLE)
========================================================================================================

The current ontology describes Material Science Lab Equipment.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 146
        * - **Total Edges**
          - 479
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 52
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 45
        * - **Individuals**
          - 3
        * - **Properties**
          - 10

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.77
        * - **Depth Variance**
          - 1.70
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 53
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 17.75
        * - **Breadth Variance**
          - 353.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 3
        * - **Taxonomic Relations**
          - 47
        * - **Non-taxonomic Relations**
          - 228
        * - **Average Terms per Type**
          - 1.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MSLE

    ontology = MSLE()
    ontology.load("path/to/MSLE-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
