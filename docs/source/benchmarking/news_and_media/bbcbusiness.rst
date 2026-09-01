.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Business News
       * - **Current Version**
         - 0.5
       * - **Last Updated**
         - 2014-11-09
       * - **Creator**
         - https://www.bbc.co.uk/blogs/internet/authors/Jeremy_Tarling, https://uk.linkedin.com/in/amaalmohamed
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Business News Ontology (BBCBusiness) <https://www.bbc.co.uk/ontologies/business-news-ontology>`_

BBC Business News Ontology (BBCBusiness)
========================================================================================================
The BBC Business News Ontology (BBCBusiness) is a domain-specific ontology for describing concepts that occur in BBC business news [#bbcbusiness-ontology]_. It provides a structured vocabulary for representing business-news entities such as companies, private companies, public companies, market sectors, shares, stock markets, and market indexes [#bbcbusiness-ontology]_.

BBCBusiness supports semantic annotation and linked-data representation of business news content by defining classes and properties such as **Company**, **Sector**, **Share**, **Market**, **Index**, **companyLocation**, **parentCompany**, **sector**, **hasShare**, **listing**, **shareTicker**, and **marketTicker** [#bbcbusiness-ontology]_. By providing a standardized vocabulary, BBCBusiness supports business-news search, content integration, and semantic linking across BBC news data [#bbcbusiness-ontology]_.

**Example Usage**:
Annotate a business news article with BBCBusiness terms to specify the companies involved, whether they are public or private companies, their market sector, share information, stock-market listings, and ticker symbols, enabling semantic search and cross-platform business news integration [#bbcbusiness-ontology]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 50
        * - **Total Edges**
          - 95
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 35
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 5
        * - **Individuals**
          - 0
        * - **Properties**
          - 10

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
          - 5
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCBusiness

    ontology = BBCBusiness()
    ontology.load("path/to/BBCBusiness-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bbcbusiness-ontology] BBC. 2014.
   "Business News Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/business.html <https://iptc.org/thirdparty/bbc-ontologies/business.html>`_
