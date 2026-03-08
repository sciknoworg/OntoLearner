

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Arts and Humanities
       * - **Category**
         - Art History, Cultural Heritage
       * - **Current Version**
         - 2.1.0
       * - **Last Updated**
         - April 26th, 2024
       * - **Creator**
         - Knowledge Media Institute
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Icon Ontology (ICON) <https://w3id.org/icon/ontology/>`_

Icon Ontology (ICON)
========================================================================================================

The ICON ontology provides a formal framework for high-granularity art interpretation and analysis. It was developed by conceptualizing Panofsky's theory of levels of interpretation, enabling artworks to be systematically described according to three complementary analytical perspectives: Pre-iconographical (visual elements and their formal properties), Iconographical (symbolic meaning and subject matter), and Iconological (deeper cultural and philosophical context). This three-level approach enables comprehensive semantic annotation of artworks, capturing both surface-level visual descriptions and deeper interpretive insights. The ontology supports structured knowledge representation of artistic elements, iconographic themes, cultural references, and symbolic meanings. It facilitates semantic interoperability in digital art collections, museum databases, and art history research platforms. The ICON ontology enables advanced search and discovery capabilities based on artistic interpretation levels, supporting art historians, curators, and researchers in analyzing and understanding artworks. It also supports linked data integration with other cultural heritage ontologies and knowledge bases, enabling rich cross-domain art historical research and interpretation analysis.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 408
        * - **Total Edges**
          - 1091
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 131
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 76
        * - **Individuals**
          - 0
        * - **Properties**
          - 68

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 12
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.92
        * - **Depth Variance**
          - 13.34
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 13
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 8.62
        * - **Breadth Variance**
          - 4.24
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 65
        * - **Non-taxonomic Relations**
          - 4
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ICON

    ontology = ICON()
    ontology.load("path/to/ICON-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
