

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2025-03-11
       * - **Creator**
         - University of Warsaw
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Physico-chemical process ontology (REX) <https://terminology.tib.eu/ts/ontologies/REX>`_

Physico-chemical process ontology (REX)
========================================================================================================

REX is an ontology of physico-chemical processes, i.e. physico-chemical changes occurring in course of time.     REX includes both microscopic processes (involving molecular entities or subatomic particles) and macroscopic processes.     Some biochemical processes from Gene Ontology (GO Biological process) can be described as instances of REX.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2461
        * - **Total Edges**
          - 5630
        * - **Root Nodes**
          - 356
        * - **Leaf Nodes**
          - 1457
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 552
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
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.35
        * - **Depth Variance**
          - 0.97
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 978
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 304.57
        * - **Breadth Variance**
          - 116930.53
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 953
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import REX

    ontology = REX()
    ontology.load("path/to/REX-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
