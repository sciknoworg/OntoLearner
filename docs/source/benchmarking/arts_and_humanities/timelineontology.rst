

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Arts and Humanities
       * - **Category**
         - Music Theory
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 25th October 2007
       * - **Creator**
         - Christopher Sutton, Yves Raimond, Matthias Mauch
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Timeline Ontology (TimelineOntology) <https://github.com/motools/timelineontology>`_

Timeline Ontology (TimelineOntology)
========================================================================================================

The Timeline Ontology is centered around the notion of timeline,     seen here as a way to identify a temporal backbone.     A timeline may support a signal, a video, a score, a work, etc.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 286
        * - **Total Edges**
          - 652
        * - **Root Nodes**
          - 20
        * - **Leaf Nodes**
          - 89
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 47
        * - **Individuals**
          - 2
        * - **Properties**
          - 46

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 5
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.28
        * - **Depth Variance**
          - 1.89
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 20
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 9.67
        * - **Breadth Variance**
          - 56.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 2
        * - **Taxonomic Relations**
          - 28
        * - **Non-taxonomic Relations**
          - 10
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import TimelineOntology

    ontology = TimelineOntology()
    ontology.load("path/to/TimelineOntology-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
