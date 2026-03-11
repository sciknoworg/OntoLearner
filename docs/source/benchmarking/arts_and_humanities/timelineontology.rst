

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

The Timeline Ontology provides a formal framework for representing and managing temporal information in multimedia and music contexts. It centers around the notion of timelines as temporal backbones that can support various types of media including signals, videos, musical scores, and musical works. The ontology enables precise temporal annotation and synchronization of multimedia elements, allowing for structured representation of time-based relationships between different media components. It supports rich temporal modeling including durations, intervals, and temporal landmarks within multimedia documents. The Timeline Ontology facilitates content synchronization across different representations, such as aligning audio signals with musical notation or video with accompanying metadata. It is particularly valuable for music information retrieval systems, multimedia annotation tools, and digital humanities research. The ontology enables advanced applications including temporal querying of multimedia content, cross-media alignment, and time-aware metadata management. By providing a common temporal framework, the Timeline Ontology supports interoperability in music and media analysis systems, enabling researchers and practitioners to work with complex temporal structures in a standardized, machine-readable format.

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
