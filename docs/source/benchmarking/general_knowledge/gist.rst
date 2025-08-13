

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Upper Ontology
       * - **Current Version**
         - 12.1.0
       * - **Last Updated**
         - 2024-Feb-27
       * - **Creator**
         - Semantic Arts
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download GIST Upper Ontology (GIST) <https://semanticarts.com/gist>`_

GIST Upper Ontology (GIST)
========================================================================================================

Gist is Semantic Arts' minimalist upper ontology for the enterprise.     It is designed to have the maximum coverage of typical business ontology concepts     with the fewest number of primitives and the least amount of ambiguity.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1352
        * - **Total Edges**
          - 2543
        * - **Root Nodes**
          - 77
        * - **Leaf Nodes**
          - 633
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 199
        * - **Individuals**
          - 8
        * - **Properties**
          - 113

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 27
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.14
        * - **Depth Variance**
          - 21.06
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 298
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 34.86
        * - **Breadth Variance**
          - 3571.91
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 8
        * - **Taxonomic Relations**
          - 39
        * - **Non-taxonomic Relations**
          - 56
        * - **Average Terms per Type**
          - 8.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GIST

    ontology = GIST()
    ontology.load("path/to/GIST-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
