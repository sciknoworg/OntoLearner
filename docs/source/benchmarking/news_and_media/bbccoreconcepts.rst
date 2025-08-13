

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Core Concepts
       * - **Current Version**
         - 1.30
       * - **Last Updated**
         - 2019-11-21
       * - **Creator**
         - jeremy.tarling@bbc.co.uk, tom.hodgkinson@bbc.co.uk
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Core Concepts Ontology (BBCCoreConcepts) <https://www.bbc.co.uk/ontologies/core-concepts-ontology>`_

BBC Core Concepts Ontology (BBCCoreConcepts)
========================================================================================================

The generic BBC ontology for people, places, events, organisations, themes which represent things     that make sense across the BBC. This model is meant to be generic enough, and allow clients (domain experts)     link their own concepts e.g., athletes or politicians using rdfs:sublClassOf the particular concept.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 122
        * - **Total Edges**
          - 265
        * - **Root Nodes**
          - 4
        * - **Leaf Nodes**
          - 73
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 22
        * - **Individuals**
          - 0
        * - **Properties**
          - 29

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
          - 1.35
        * - **Depth Variance**
          - 0.63
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 11
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 6.67
        * - **Breadth Variance**
          - 9.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 25
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCCoreConcepts

    ontology = BBCCoreConcepts()
    ontology.load("path/to/BBCCoreConcepts-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
