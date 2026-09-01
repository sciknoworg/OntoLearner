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
The BBC Creative Work Ontology (BBCCreativeWork) is an ontology used to describe creative works produced by the BBC and their associated metadata [#bbccreativework-ontology]_. It provides a structured vocabulary for representing creative works, their specific types such as BlogPost, NewsItem, and Programme, their audiences, and the tags associated with them [#bbccreativework-ontology]_.

BBCCreativeWork supports reading and writing creative works in the BBC triplestore and enables semantic annotation, content integration, discovery, and reuse across BBC digital platforms [#bbccreativework-ontology]_. By providing standardized terms for creative content and metadata, the ontology helps connect BBC content with topics, audiences, and related entities in linked-data systems [#bbccreativework-ontology]_.

**Example Usage**:
Annotate a BBC news article with BBCCreativeWork terms to specify that it is a **NewsItem**, link it to relevant tags or topics, identify its intended audience, and connect it to related creative works, enabling semantic search and content integration across BBC platforms [#bbccreativework-ontology]_.

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

References
----------

.. [#bbccreativework-ontology] BBC. 2012.
   "Creative Work Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/creativework.html <https://iptc.org/thirdparty/bbc-ontologies/creativework.html>`_
