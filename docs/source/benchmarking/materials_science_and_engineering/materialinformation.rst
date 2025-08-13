

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Toshihiro Ashino
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download Material Information Ontology (MaterialInformation) <https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MaterialInformation.owl>`_

Material Information Ontology (MaterialInformation)
========================================================================================================

The Material Information ontology is divided into smaller ontologies (partitions).     The partitions are Environment, Geometry, Material Information, Manufacturing Process, Property,     Substance, Unit Dimension, Structure, Equation and Physical Constant.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1155
        * - **Total Edges**
          - 2343
        * - **Root Nodes**
          - 596
        * - **Leaf Nodes**
          - 48
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 548
        * - **Individuals**
          - 410
        * - **Properties**
          - 98

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 11
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.82
        * - **Depth Variance**
          - 2.11
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 596
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 96.08
        * - **Breadth Variance**
          - 36614.24
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 404
        * - **Taxonomic Relations**
          - 605
        * - **Non-taxonomic Relations**
          - 30
        * - **Average Terms per Type**
          - 1.03
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MaterialInformation

    ontology = MaterialInformation()
    ontology.load("path/to/MaterialInformation-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
