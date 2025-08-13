

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Information, Data, Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2022-11-07
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Information Artifact Ontology (IAO) <https://terminology.tib.eu/ts/ontologies/IAO>`_

Information Artifact Ontology (IAO)
========================================================================================================

The Information Artifact Ontology (IAO) is an ontology of information entities,     originally driven by work by the OBI digital entity and realizable information entity branch.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2303
        * - **Total Edges**
          - 4720
        * - **Root Nodes**
          - 151
        * - **Leaf Nodes**
          - 1523
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 292
        * - **Individuals**
          - 18
        * - **Properties**
          - 57

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.05
        * - **Depth Variance**
          - 4.06
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 280
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 63.00
        * - **Breadth Variance**
          - 8210.29
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 18
        * - **Taxonomic Relations**
          - 347
        * - **Non-taxonomic Relations**
          - 19
        * - **Average Terms per Type**
          - 6.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import IAO

    ontology = IAO()
    ontology.load("path/to/IAO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
