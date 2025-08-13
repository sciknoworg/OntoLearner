

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.4.3
       * - **Last Updated**
         - None
       * - **Creator**
         - Lukas Gold, Simon Stier
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Battery Value Chain Ontology (BVCO) <https://github.com/Battery-Value-Chain-Ontology/ontology>`_

Battery Value Chain Ontology (BVCO)
========================================================================================================

Basically, Battery Value Chain Ontology (BVCO) aims to model processes along the Battery value chain. Processes are     holistic perspective elements that transform inputs/educts (matter, energy, information)     into output/products (matter, energy, information) with the help of tools (devices, algorithms).     They can be decomposed into sub-processes and have predecessor and successor processes.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 804
        * - **Total Edges**
          - 1719
        * - **Root Nodes**
          - 85
        * - **Leaf Nodes**
          - 283
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 262
        * - **Individuals**
          - 0
        * - **Properties**
          - 6

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 14
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.47
        * - **Depth Variance**
          - 5.27
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 230
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 52.20
        * - **Breadth Variance**
          - 4920.43
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BVCO

    ontology = BVCO()
    ontology.load("path/to/BVCO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
