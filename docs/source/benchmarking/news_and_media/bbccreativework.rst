.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Creative Work
       * - **Current Version**
         - 1.19
       * - **Last Updated**
         - 2012-12-01
       * - **Creator**
         - LinkedData@bbc.co.uk
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Creative Work Ontology (BBCCreativeWork) <https://www.bbc.co.uk/ontologies/creative-work-ontology>`_

BBC Creative Work Ontology (BBCCreativeWork)
========================================================================================================

The BBC Creative Work Ontology (BBCCreativeWork) is a domain ontology designed to represent creative works produced by the BBC, such as articles, blog posts, news items, programmes, and their associated metadata. It provides a structured vocabulary for describing creative works, their types, audiences, tags, and relationships to other works and entities. BBCCreativeWork supports semantic annotation of content, enabling advanced search, recommendation, and content management across BBC platforms. The ontology is designed for extensibility, allowing integration with other BBC ontologies and external vocabularies for broader data interoperability. By providing standardized terms and relationships, BBCCreativeWork facilitates content linking, audience targeting, and analytics in digital publishing. The ontology is maintained as an open resource and is actively extended to support new content types and publishing requirements.

**Example Usage**:
Annotate a BBC news article with BBCCreativeWork terms to specify its type (e.g., "NewsItem"), associated tags (e.g., "climate change"), intended audience (e.g., "general public"), and relationships to related programmes or blog posts, enabling semantic search and personalized content recommendations.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 137
        * - **Total Edges**
          - 300
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 80
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 20
        * - **Individuals**
          - 15
        * - **Properties**
          - 21

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
          - 15
        * - **Taxonomic Relations**
          - 17
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 5.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCCreativeWork

    ontology = BBCCreativeWork()
    ontology.load("path/to/BBCCreativeWork-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
