

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Data, Metadata
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download FAIR Vocabulary (FAIR) <https://terminology.tib.eu/ts/ontologies/FAIR>`_

FAIR Vocabulary (FAIR)
========================================================================================================

This is the formal vocabulary (ontology) describing the FAIR principles.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 92
        * - **Total Edges**
          - 180
        * - **Root Nodes**
          - 9
        * - **Leaf Nodes**
          - 37
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 7
        * - **Individuals**
          - 19
        * - **Properties**
          - 1

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.18
        * - **Depth Variance**
          - 0.15
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 9
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.50
        * - **Breadth Variance**
          - 12.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 19
        * - **Taxonomic Relations**
          - 3
        * - **Non-taxonomic Relations**
          - 3
        * - **Average Terms per Type**
          - 9.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FAIR

    ontology = FAIR()
    ontology.load("path/to/FAIR-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
