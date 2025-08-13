

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download Material Ontology (MatOnto) <https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MatOnto.owl>`_

Material Ontology (MatOnto)
========================================================================================================

The Material Ontology (MatOnto) is based on the upper level ontology, the BFO.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4753
        * - **Total Edges**
          - 11287
        * - **Root Nodes**
          - 33
        * - **Leaf Nodes**
          - 1063
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1307
        * - **Individuals**
          - 122
        * - **Properties**
          - 95

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 129
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 38.24
        * - **Depth Variance**
          - 1437.88
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 155
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 18.92
        * - **Breadth Variance**
          - 522.53
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 122
        * - **Taxonomic Relations**
          - 1215
        * - **Non-taxonomic Relations**
          - 167
        * - **Average Terms per Type**
          - 1.94
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MatOnto

    ontology = MatOnto()
    ontology.load("path/to/MatOnto-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
