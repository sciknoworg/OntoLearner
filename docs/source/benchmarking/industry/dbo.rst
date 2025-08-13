

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Building Information
       * - **Current Version**
         - 0.0.1
       * - **Last Updated**
         - 02/23/2023
       * - **Creator**
         - Google
       * - **License**
         - Apache 2.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Digital Buildings Ontology (DBO) <https://github.com/google/digitalbuildings?tab=readme-ov-file>`_

Digital Buildings Ontology (DBO)
========================================================================================================

The Digital Buildings ontology (DBO) is used by Google to represent structured information     about buildings and building-installed equipment.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 13152
        * - **Total Edges**
          - 32491
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 686
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3032
        * - **Individuals**
          - 35
        * - **Properties**
          - 7

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.57
        * - **Depth Variance**
          - 0.82
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 3
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.75
        * - **Breadth Variance**
          - 0.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 35
        * - **Taxonomic Relations**
          - 18738
        * - **Non-taxonomic Relations**
          - 12
        * - **Average Terms per Type**
          - 2.06
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DBO

    ontology = DBO()
    ontology.load("path/to/DBO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
