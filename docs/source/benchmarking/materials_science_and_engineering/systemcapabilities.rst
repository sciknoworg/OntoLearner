

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science, Engineering, Systems
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2017-05-14
       * - **Creator**
         - W3C/OGC Spatial Data on the Web Working Group
       * - **License**
         - W3C Software and Document License
       * - **Format**
         - owl
       * - **Download**
         - `Download System Capabilities Ontology (SystemCapabilities) <https://terminology.tib.eu/ts/ontologies/SSNSYSTEM>`_

System Capabilities Ontology (SystemCapabilities)
========================================================================================================

This ontology describes system capabilities, operating ranges, and survival ranges.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 137
        * - **Total Edges**
          - 268
        * - **Root Nodes**
          - 14
        * - **Leaf Nodes**
          - 47
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 25
        * - **Individuals**
          - 3
        * - **Properties**
          - 8

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.22
        * - **Depth Variance**
          - 0.17
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 9.00
        * - **Breadth Variance**
          - 25.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 45
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SystemCapabilities

    ontology = SystemCapabilities()
    ontology.load("path/to/SystemCapabilities-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
