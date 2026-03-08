

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Finance
       * - **Category**
         - E-commerce
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2011-10-01
       * - **Creator**
         - Martin Hepp
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Good Relations Language Reference (GoodRelations) <https://www.heppnetz.de/ontologies/goodrelations/v1>`_

Good Relations Language Reference (GoodRelations)
========================================================================================================

GoodRelations is a widely-used ontology for describing products, services, offers, and commercial entities on the Web. It provides a rich vocabulary for modeling commercial information such as Products, Offers, Stores, Sellers, Payment and Delivery options, Price specifications, and Availability. GoodRelations emphasizes machine-actionable, fine-grained descriptions that support e-commerce discovery, comparison shopping, and automated processing by search engines, marketplaces, and recommendation systems. Key characteristics include a modular class structure (distinguishing Products/Services from Offers and Sellers), detailed modeling of price specifications (including currency, unit price, and price components), temporal validity of offers, and explicit representation of delivery and payment methods. The ontology is designed for interoperability: it can be embedded in HTML pages (microdata/RDFa/JSON-LD), linked with vocabularies like schema.org and FOAF, and exported in RDF/OWL for semantic-web use. GoodRelations supports provenance and business metadata, enabling trust and auditing use cases in marketplaces. Typical applications include SEO and product rich snippets, integration of catalog data across vendors, automated price aggregation, and semantic matching in recommender systems.

**Example usage**: describe a product offering as an gr:Offering that links to a gr:Product (with identifiers and brand), includes a gr:UnitPriceSpecification (with priceCurrency, price, and validFrom/validThrough), and connects to a gr:BusinessEntity representing the seller with contact details and opening hours.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 677
        * - **Total Edges**
          - 1816
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 206
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 98
        * - **Individuals**
          - 47
        * - **Properties**
          - 102

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 30
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 7.81
        * - **Depth Variance**
          - 73.22
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 33
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.77
        * - **Breadth Variance**
          - 55.21
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 46
        * - **Taxonomic Relations**
          - 25
        * - **Non-taxonomic Relations**
          - 264
        * - **Average Terms per Type**
          - 5.75
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GoodRelations

    ontology = GoodRelations()
    ontology.load("path/to/GoodRelations-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
