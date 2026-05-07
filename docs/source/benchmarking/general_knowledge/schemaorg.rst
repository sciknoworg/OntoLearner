

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

Schema.org is a collaborative, community-driven initiative that provides
a shared vocabulary for structured data markup on the web, in email
messages, and beyond [#schema-home]_ [#schema-paper]_. It enables
webmasters, content creators, and developers to annotate digital
resources with machine-readable semantic information that can be used by
search engines and other applications [#schema-home]_.

Schema.org provides extensible schemas for describing entities,
relationships, and actions across many domains, including people,
organizations, places, products, events, creative works, publications,
health and medical information, and other web resources [#schema-home]_.
The vocabulary can be expressed using formats such as JSON-LD, RDFa, and
Microdata, making it flexible for different publishing and data
integration scenarios [#schema-home]_ [#schema-paper]_.

Schema.org is designed for broad applicability across industries while
also supporting extension mechanisms for more specialized use cases
[#schema-home]_. Its markup is widely used by publishers and consumed by
major web applications to support structured data exchange, enhanced
search experiences, knowledge graph construction, content discovery, and
interoperability across web-based services [#schema-paper]_.

**Example Usage**: Annotate a restaurant website with Schema.org terms
such as Organization, LocalBusiness, address, openingHours, telephone,
and AggregateRating. This allows search engines and other applications to
understand the restaurant's location, contact details, opening hours, and
review information, supporting richer search results and improved
resource discovery [#schema-home]_ [#schema-paper]_.

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

References
----------

.. [#schema-home] Schema.org. n.d.
   "Schema.org."
   Available at:
   `https://schema.org/ <https://schema.org/>`_

.. [#schema-paper] Guha, R. V., Brickley, D., and Macbeth, S. 2016.
   "Schema.org: Evolution of Structured Data on the Web."
   *Communications of the ACM* 59(2): 44--51.
   DOI:
   `10.1145/2857274.2857276 <https://doi.org/10.1145/2857274.2857276>`_
