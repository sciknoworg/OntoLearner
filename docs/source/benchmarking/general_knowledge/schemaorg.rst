

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Web Development
       * - **Current Version**
         - 28.1
       * - **Last Updated**
         - 2024-11-22
       * - **Creator**
         - Schema.org Community
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Schema.org Ontology (SchemaOrg) <https://github.com/schemaorg/schemaorg/blob/main/data/releases/28.1/schemaorg.owl>`_

Schema.org Ontology (SchemaOrg)
========================================================================================================

Schema.org is a collaborative, community-driven initiative providing standardized schemas and ontologies for structured data markup across the entire web. It creates and maintains comprehensive vocabularies that enable webmasters, content creators, and developers to annotate web pages, email messages, and other digital resources with machine-readable semantic information. Schema.org covers diverse domains including products, organizations, events, publications, creative works, health and medical information, and many others. The schemas are designed for broad applicability across different industries while remaining flexible enough for domain-specific extensions. Schema.org markup is widely recognized and processed by major search engines, social media platforms, and aggregation services, directly impacting content discovery and presentation. The ontology facilitates knowledge graph construction, enhanced search results (rich snippets), and improved interoperability across web applications and services.

**Example Usage**:
Annotate a restaurant website with Schema.org markup including Organization (restaurant details), LocalBusiness (address, phone, hours), and AggregateRating (customer reviews) to enable search engines to display rich snippets with ratings, location, and hours directly in search results.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 15044
        * - **Total Edges**
          - 32425
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 2128
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3881
        * - **Individuals**
          - 0
        * - **Properties**
          - 1485

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
          - 0
        * - **Taxonomic Relations**
          - 1058
        * - **Non-taxonomic Relations**
          - 635
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SchemaOrg

    ontology = SchemaOrg()
    ontology.load("path/to/SchemaOrg-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
