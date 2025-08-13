

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Social Sciences
       * - **Category**
         - Social
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - 23 May 2017
       * - **Creator**
         - None
       * - **License**
         - W3C Document License
       * - **Format**
         - ttl
       * - **Download**
         - `Download Activity Streams 2.0 Ontology (AS2) <https://github.com/w3c/activitystreams?tab=License-1-ov-file#readme>`_

Activity Streams 2.0 Ontology (AS2)
========================================================================================================

The Activity Streams 2.0 ontology is a vocabulary for describing social activities and actions.     It is based on the Activity Streams 2.0 specification and provides a set of classes and properties     for describing activities on the web.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 426
        * - **Total Edges**
          - 945
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 120
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 107
        * - **Individuals**
          - 1
        * - **Properties**
          - 69

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 0
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.00
        * - **Depth Variance**
          - 0.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 0
        * - **Minimum Breadth**
          - 0
        * - **Average Breadth**
          - 0.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1
        * - **Taxonomic Relations**
          - 55
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AS2

    ontology = AS2()
    ontology.load("path/to/AS2-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
