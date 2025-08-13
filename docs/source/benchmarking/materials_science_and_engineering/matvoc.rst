

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.0.0
       * - **Last Updated**
         - 2022-12-12
       * - **Creator**
         - Tatyana Sheveleva, Javad Chamanara
       * - **License**
         - MIT License
       * - **Format**
         - rdf
       * - **Download**
         - `Download Materials Vocabulary (MatVoc) <https://stream-project.github.io/#overv>`_

Materials Vocabulary (MatVoc)
========================================================================================================

The official ontology produced in the context of the STREAM project.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 94
        * - **Total Edges**
          - 161
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 44
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 28
        * - **Individuals**
          - 0
        * - **Properties**
          - 15

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
          - 0.62
        * - **Depth Variance**
          - 0.48
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 16
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 10.67
        * - **Breadth Variance**
          - 24.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 6
        * - **Non-taxonomic Relations**
          - 7
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MatVoc

    ontology = MatVoc()
    ontology.load("path/to/MatVoc-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
