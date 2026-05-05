

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

GoodRelations is a widely used ontology for describing products,
services, offers, and commercial entities on the Web [#gr-paper]_
[#gr-wiki]_. It provides a rich vocabulary for modeling commercial
information such as offers, business entities, price specifications,
availability, payment options, and delivery methods [#gr-paper]_
[#gr-ref]_. GoodRelations emphasizes machine-processable, fine-grained
descriptions of e-commerce information that support product discovery,
comparison, and automated processing on the Web [#gr-paper]_
[#gr-wiki]_. A key design principle is the distinction between products
or services, the offers made for them, and the legal entities that
provide them, together with detailed modeling of prices and commercial
conditions [#gr-paper]_ [#gr-ref]_. By providing a shared semantic
framework for commercial data, GoodRelations supports e-commerce SEO,
catalog integration, offer aggregation, and other Semantic Web and Web
data applications [#gr-paper]_ [#gr-wiki]_.

**Example Usage**: Describe a product offering as a ``gr:Offering``
that links to a product or service, includes a
``gr:UnitPriceSpecification`` with currency and price information, and
connects to a ``gr:BusinessEntity`` representing the seller together
with relevant payment, delivery, and offer-validity information, so
that the offering can be processed consistently by search engines,
marketplaces, and other web applications [#gr-ref]_ [#gr-paper]_.

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

References
----------

.. [#gr-paper] Hepp, M. 2008.
   "GoodRelations: An Ontology for Describing Products and Services
   Offers on the Web."
   In *Knowledge Engineering: Practice and Patterns*, Lecture Notes in
   Computer Science 5268, pp. 329-346.
   Available at: `https://www.heppnetz.de/files/GoodRelationsEKAW2008-crc-final.pdf <https://www.heppnetz.de/files/GoodRelationsEKAW2008-crc-final.pdf>`_

.. [#gr-ref] Hepp, M. 2010.
   "GoodRelations Language Reference."
   Available at: `https://www.heppnetz.de/ontologies/goodrelations/20100412/v1.html <https://www.heppnetz.de/ontologies/goodrelations/20100412/v1.html>`_

.. [#gr-wiki] GoodRelations Wiki. n.d.
   "Documentation/Intro."
   Available at: `https://wiki.goodrelations-vocabulary.org/Documentation/Intro <https://wiki.goodrelations-vocabulary.org/Documentation/Intro>`_
