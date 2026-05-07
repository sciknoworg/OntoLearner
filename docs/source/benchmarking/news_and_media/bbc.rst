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
The BBC Ontology (BBC) is an ontology used to describe BBC concepts in the BBC linked-data store [#bbc-ontology]_. It represents BBC divisions or products that publish linked data, the platforms for which BBC content is produced, and web documents that publish or are relevant to BBC content [#bbc-ontology]_.

The ontology codifies the logic connecting web documents, BBC products, and platforms [#bbc-ontology]_. It defines key classes such as Product, Platform, WebDocument, WebDocumentCategory, and NewsService, together with properties such as product, platform, primaryContent, primaryContentOf, hasOutput, covers, and servedBy [#bbc-ontology]_. By providing a structured vocabulary, the BBC Ontology supports semantic annotation, content integration, discovery, and linked-data representation across BBC digital services [#bbc-ontology]_.

**Example Usage**:
Annotate a BBC web document with BBC Ontology terms to specify the product it belongs to, such as BBC Sport, the platform it is intended for, such as HighWeb or Mobile, its primary creative work, and its web document category, enabling semantic search and integration across BBC linked-data systems [#bbc-ontology]_.

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

References
----------

.. [#bbc-ontology] BBC. 2012.
   "BBC Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/bbc.html <https://iptc.org/thirdparty/bbc-ontologies/bbc.html>`_
