.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - News
       * - **Current Version**
         - 1.37
       * - **Last Updated**
         - 2012-12-01
       * - **Creator**
         - LinkedData@bbc.co.uk
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Ontology (BBC) <https://www.bbc.co.uk/ontologies/bbc-ontology/>`_

BBC Ontology (BBC)
========================================================================================================

The BBC Ontology (BBC) is a domain ontology developed to represent the structure, relationships, and metadata of BBC web documents, products, and platforms. It provides a standardized vocabulary for describing content types, thematic areas, editorial products, and the connections between them. The ontology enables semantic annotation of BBC content, supporting advanced search, personalized recommendations, and content integration across BBC's digital ecosystem. BBC is designed for extensibility and interoperability, allowing integration with other BBC ontologies and external vocabularies for broader data linking. By providing a common semantic framework, the BBC Ontology facilitates content discovery, analytics, and knowledge management for editorial, educational, and entertainment products. The ontology is maintained as an open resource and is actively extended to support new content types, platforms, and user experiences.

**Example Usage**:
Annotate a BBC web page with BBC Ontology terms to specify its content type (e.g., "NewsArticle"), associated product (e.g., "BBC News"), thematic area (e.g., "Education"), and relationships to related articles or platforms, enabling semantic search and cross-platform content integration.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 164
        * - **Total Edges**
          - 316
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 101
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 25
        * - **Individuals**
          - 10
        * - **Properties**
          - 24

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
          - 10
        * - **Taxonomic Relations**
          - 35
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 5.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBC

    ontology = BBC()
    ontology.load("path/to/BBC-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
