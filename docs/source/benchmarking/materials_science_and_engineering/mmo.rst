

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - 1.0.1
       * - **Last Updated**
         - 2024-01-30
       * - **Creator**
         - Akhil Thomas, Ali Riza Durmaz
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Materials Mechanics Ontology (MMO) <https://iwm-micro-mechanics-public.pages.fraunhofer.de/ontologies/materials-mechanics-ontology/index-en.html>`_

Materials Mechanics Ontology (MMO)
========================================================================================================

The materials mechanics ontology is an application-level ontology that was created     for supporting named entity recognition tasks for materials fatigue domain. The ontology covers     some fairly general MSE concepts that could prospectively be merged into PMDco or other upper materials ontologies     such as descriptions of crystallographic defects and microstructural entities.     Furthermore, concepts related to the materials fatigue subdomain are also heavily incorporated.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1043
        * - **Total Edges**
          - 2402
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 509
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 428
        * - **Individuals**
          - 0
        * - **Properties**
          - 17

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 8
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.92
        * - **Depth Variance**
          - 5.32
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 17
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 8.89
        * - **Breadth Variance**
          - 21.65
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 566
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MMO

    ontology = MMO()
    ontology.load("path/to/MMO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
