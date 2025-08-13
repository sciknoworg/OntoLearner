

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.2
       * - **Last Updated**
         - None
       * - **Creator**
         - REACT project team
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download The Heat Pump Ontology (HPOnt) <https://react2020.github.io/REACT-ONTOLOGY/HPOnt/index-en.html/>`_

The Heat Pump Ontology (HPOnt)
========================================================================================================

The Heat Pump Ontology (HPOnt) aims to formalize and represent all the relevant information of Heat Pumps.     The HPOnt has been developed as part of the REACT project which has received funding     from the European Union’s Horizon 2020 research and innovation programme under grant agreement no. 824395.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 84
        * - **Total Edges**
          - 143
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 43
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 4
        * - **Individuals**
          - 6
        * - **Properties**
          - 12

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 4
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.13
        * - **Depth Variance**
          - 1.98
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 16
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 6.00
        * - **Breadth Variance**
          - 27.20
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 5
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 2.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import HPOnt

    ontology = HPOnt()
    ontology.load("path/to/HPOnt-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
