

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 4.0
       * - **Last Updated**
         - 2013-07-01
       * - **Creator**
         - http://oxgiraldo.wordpress.com
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download SMART Protocols Ontology: Document Module (SP-Document) <https://github.com/SMARTProtocols/SMART-Protocols>`_

SMART Protocols Ontology: Document Module (SP-Document)
========================================================================================================

SMART Protocols Ontology: Document Module is an ontology designed     to represent metadata used to report an experimental protocol.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1489
        * - **Total Edges**
          - 3044
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 908
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 400
        * - **Individuals**
          - 45
        * - **Properties**
          - 43

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 9
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.96
        * - **Depth Variance**
          - 4.49
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 69
        * - **Minimum Breadth**
          - 8
        * - **Average Breadth**
          - 32.80
        * - **Breadth Variance**
          - 369.36
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 45
        * - **Taxonomic Relations**
          - 474
        * - **Non-taxonomic Relations**
          - 73
        * - **Average Terms per Type**
          - 2.65
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SPDocument

    ontology = SPDocument()
    ontology.load("path/to/SPDocument-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
