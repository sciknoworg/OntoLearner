

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Linguistics
       * - **Current Version**
         - 2018a
       * - **Last Updated**
         - 2018-02-15
       * - **Creator**
         - Francesco Corcoglioniti, Marco Rospocher <https://dkm.fbk.eu/rospocher>
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Pre-Modern Ontology (PreMOn) <https://premon.fbk.eu/ontology/core#>`_

Pre-Modern Ontology (PreMOn)
========================================================================================================

The PreMOn Ontology is an extension of lemon (W3C Ontology Lexicon Community Group, 2015)     for representing predicate models and their mappings. The Core Module of the PreMOn Ontology     defines the main abstractions for modelling semantic classes with their semantic roles,     mappings between different predicate models, and annotations.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 115
        * - **Total Edges**
          - 213
        * - **Root Nodes**
          - 13
        * - **Leaf Nodes**
          - 45
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 15
        * - **Individuals**
          - 0
        * - **Properties**
          - 16

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
          - 1.80
        * - **Depth Variance**
          - 3.33
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
          - 7.29
        * - **Breadth Variance**
          - 38.49
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 17
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PreMOn

    ontology = PreMOn()
    ontology.load("path/to/PreMOn-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
