

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Social Sciences
       * - **Category**
         - Social
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2018-07-06
       * - **Creator**
         - Mark Fox, Megan Katsumi
       * - **License**
         - None
       * - **Format**
         - rdf
       * - **Download**
         - `Download Contact Ontology (Contact) <https://enterpriseintegrationlab.github.io/icity/Contact/Contact_1.0/doc/index-en.html>`_

Contact Ontology (Contact)
========================================================================================================

The Contact Ontology is a specialized vocabulary for representing contact information, including addresses, phone numbers, email-related contact details, hours of operation, and associated location information [#contact-ontology]_. It reuses and extends contact-related modeling patterns to support city, business, organizational, and location-aware applications [#contact-ontology]_. The ontology introduces specialized concepts for representing operational availability, such as hours of operation, and connects contact information with spatial location data to support geographic lookup, mapping, and service discovery [#contact-ontology]_. By providing structured terms for addresses, contact channels, operating hours, and location associations, the Contact Ontology enables interoperable representation of business and organizational contact data [#contact-ontology]_. It supports applications such as customer relationship management, location-based services, facility management, city information systems, and service discovery platforms [#contact-ontology]_.

**Example Usage**: Represent a business location with Contact Ontology terms for street address, postal code, phone number, email contact, hours of operation, and associated geographic coordinates. This enables location mapping, contact discovery, service lookup, and integration with city or facility information systems [#contact-ontology]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 433
        * - **Total Edges**
          - 845
        * - **Root Nodes**
          - 129
        * - **Leaf Nodes**
          - 50
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 44
        * - **Individuals**
          - 1
        * - **Properties**
          - 64

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 16
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.54
        * - **Depth Variance**
          - 14.55
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 129
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 24.00
        * - **Breadth Variance**
          - 893.06
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1
        * - **Taxonomic Relations**
          - 97
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Contact

    ontology = Contact()
    ontology.load("path/to/Contact-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#contact-ontology] Enterprise Integration Laboratory. 2018.
   "Contact Ontology."
   Available at:
   `https://enterpriseintegrationlab.github.io/icity/Contact/Contact_1.0/doc/index-en.html <https://enterpriseintegrationlab.github.io/icity/Contact/Contact_1.0/doc/index-en.html>`_
