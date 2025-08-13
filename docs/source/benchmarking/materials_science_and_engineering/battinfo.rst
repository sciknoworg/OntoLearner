

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
         - None
       * - **License**
         - None
       * - **Format**
         - ttl
       * - **Download**
         - `Download Battery Interface Ontology (BattINFO) <https://github.com/BIG-MAP/BattINFO>`_

Battery Interface Ontology (BattINFO)
========================================================================================================

BattINFO is a foundational resource for harmonizing battery knowledge representation     and enhancing data interoperability. The primary objective is to provide the necessary tools     to create FAIR (Findable, Accessible, Interoperable, Reusable) battery data     that can be integrated into the Semantic Web.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 27319
        * - **Total Edges**
          - 50787
        * - **Root Nodes**
          - 2855
        * - **Leaf Nodes**
          - 16852
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 4431
        * - **Individuals**
          - 7
        * - **Properties**
          - 304

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 27
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.09
        * - **Depth Variance**
          - 7.40
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 10695
        * - **Minimum Breadth**
          - 7
        * - **Average Breadth**
          - 827.86
        * - **Breadth Variance**
          - 4644992.84
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 10
        * - **Taxonomic Relations**
          - 195
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 10.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BattINFO

    ontology = BattINFO()
    ontology.load("path/to/BattINFO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
