

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Testing
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - 05/05/2022
       * - **Creator**
         - Birgit Skrotzki, Hossein Beygi Nasrabadi, Philipp von Hartrott, Vinicius Carrillo Beber, Yue Chen
       * - **License**
         - None
       * - **Format**
         - ttl
       * - **Download**
         - `Download MatoLab Brinell Test Ontology (MOL_BRINELL) <https://matportal.org/ontologies/MOL_BRINELL>`_

MatoLab Brinell Test Ontology (MOL_BRINELL)
========================================================================================================

An ontology for describing the Brinell hardness testing process, made in the Materials Open Lab Project.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 3648
        * - **Total Edges**
          - 16347
        * - **Root Nodes**
          - 29
        * - **Leaf Nodes**
          - 308
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 37
        * - **Individuals**
          - 3053
        * - **Properties**
          - 21

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
          - 0.26
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 29
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 12.67
        * - **Breadth Variance**
          - 141.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 3053
        * - **Taxonomic Relations**
          - 14
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 105.28
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MOLBRINELL

    ontology = MOLBRINELL()
    ontology.load("path/to/MOLBRINELL-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
