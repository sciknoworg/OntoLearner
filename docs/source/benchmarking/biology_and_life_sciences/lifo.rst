

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - General Purpose
       * - **Current Version**
         - 1.0.17
       * - **Last Updated**
         - March 11, 2018
       * - **Creator**
         - Yongqun "Oliver" He (YH)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Life Ontology (LifO) <https://bioportal.bioontology.org/ontologies/LIFO>`_

Life Ontology (LifO)
========================================================================================================

The Life Ontology (LifO) is an ontology of the life of organism. LifO represents the     life processes of organisms and related entities and relations. LifO is a general     purpose ontology that covers the common features associated with different     organisms such as unicellular prokaryotes (e.g., E. coli) and multicellular organisms (e.g., human).

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2140
        * - **Total Edges**
          - 4179
        * - **Root Nodes**
          - 43
        * - **Leaf Nodes**
          - 1522
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 239
        * - **Individuals**
          - 9
        * - **Properties**
          - 98

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
          - 1.18
        * - **Depth Variance**
          - 0.83
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 65
        * - **Minimum Breadth**
          - 17
        * - **Average Breadth**
          - 41.67
        * - **Breadth Variance**
          - 384.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 9
        * - **Taxonomic Relations**
          - 321
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 9.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import LIFO

    ontology = LIFO()
    ontology.load("path/to/LIFO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
