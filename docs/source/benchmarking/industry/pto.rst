

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Industry
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2025-02-21
       * - **Creator**
         - Martin Hepp
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Product Types Ontology (PTO) <http://www.productontology.org/>`_

Product Types Ontology (PTO)
========================================================================================================

The Product Types Ontology (PTO) is a vocabulary for standardized classification and semantic description of commercial products and services, designed to complement GoodRelations in semantic e-commerce applications [#pto-w3c]_ [#goodrelations-paper]_. PTO provides product and service type identifiers that can be used to describe what kind of product or service is being offered, while GoodRelations provides the commercial vocabulary for describing offers, prices, sellers, availability, and related e-commerce information [#pto-w3c]_ [#goodrelations-paper]_. PTO enables detailed product classification across diverse market segments, facilitating product discovery, comparison shopping, semantic search, and automated recommendation systems [#pto-w3c]_. The ontology can be used in web markup and linked data settings to make product information more machine-readable and easier for search engines, aggregation platforms, and e-commerce applications to process [#pto-w3c]_. By combining PTO product types with GoodRelations commercial properties such as price, availability, business entity, and offer information, organizations can create rich, machine-readable product descriptions for e-commerce applications [#goodrelations-paper]_.

**Example Usage**: Annotate a product listing with a PTO product type, such as ``Smartphone`` or ``Android_phone``, and link it to a GoodRelations ``Offering`` that describes the seller, price, availability, and delivery conditions. This enables automated product discovery, semantic search, and price comparison across e-commerce platforms [#pto-w3c]_ [#goodrelations-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4577
        * - **Total Edges**
          - 14125
        * - **Root Nodes**
          - 12
        * - **Leaf Nodes**
          - 1012
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1002
        * - **Individuals**
          - 3002
        * - **Properties**
          - 0

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.92
        * - **Depth Variance**
          - 0.87
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 12
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 8.33
        * - **Breadth Variance**
          - 14.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 3000
        * - **Taxonomic Relations**
          - 3996
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 3000.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PTO

    ontology = PTO()
    ontology.load("path/to/PTO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#pto-w3c] W3C Semantic Web Wiki. n.d.
   "Productontology."
   Available at:
   `https://www.w3.org/2001/sw/wiki/Productontology <https://www.w3.org/2001/sw/wiki/Productontology>`_

.. [#goodrelations-paper] Hepp, Martin. 2008.
   "GoodRelations: An Ontology for Describing Products and Services Offers on the Web."
   *Knowledge Engineering: Practice and Patterns*, EKAW 2008.
   DOI:
   `10.1007/978-3-540-87696-0_29 <https://doi.org/10.1007/978-3-540-87696-0_29>`_
