

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemicals, Processes
       * - **Current Version**
         - 04-14-2022
       * - **Last Updated**
         - 04-14-2022
       * - **Creator**
         - Anna Dun, Wes A. Schafer, Yongqun "Oliver" He (YH), Zachary Dance
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download PROcess Chemistry Ontology (PROCO) <https://github.com/proco-ontology/PROCO>`_

PROcess Chemistry Ontology (PROCO)
========================================================================================================

PROCO (PROcess Chemistry Ontology) is a formal ontology that aims to standardly represent entities     and relations among entities in the domain of process chemistry.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 6258
        * - **Total Edges**
          - 11796
        * - **Root Nodes**
          - 89
        * - **Leaf Nodes**
          - 4646
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 970
        * - **Individuals**
          - 14
        * - **Properties**
          - 61

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 15
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.35
        * - **Depth Variance**
          - 8.54
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 228
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 60.19
        * - **Breadth Variance**
          - 4521.40
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 14
        * - **Taxonomic Relations**
          - 1757
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 7.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PROCO

    ontology = PROCO()
    ontology.load("path/to/PROCO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
