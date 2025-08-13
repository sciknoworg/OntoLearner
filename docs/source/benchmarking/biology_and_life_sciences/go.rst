

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Molecular Biology, Genetics
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2024-11-03
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Gene Ontology (GO) <https://geneontology.org/docs/download-ontology/>`_

Gene Ontology (GO)
========================================================================================================

The Gene Ontology (GO) Provides structured controlled vocabularies for the annotation of gene products     with respect to their molecular function, cellular component, and biological role.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 534820
        * - **Total Edges**
          - 1419487
        * - **Root Nodes**
          - 133995
        * - **Leaf Nodes**
          - 293179
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 62046
        * - **Individuals**
          - 0
        * - **Properties**
          - 9

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.24
        * - **Depth Variance**
          - 1.08
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 204650
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 66849.38
        * - **Breadth Variance**
          - 6433980645.23
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 156430
        * - **Non-taxonomic Relations**
          - 30
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GO

    ontology = GO()
    ontology.load("path/to/GO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
