

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

The Contact Ontology is a specialized vocabulary for representing and managing contact information and related communication metadata such as addresses, phone numbers, email addresses, and physical locations. It reuses and extends the iContact Ontology developed by the Enterprise Integration Lab, incorporating specialized definitions while maintaining backward compatibility. The ontology extends the iContact model by introducing Hours of Operation as a specialized concept defined as both a subclass of iContact hours of operation and the Recurring Event class from the iCity Recurring Event ontology. Contact Ontology enriches address representation by associating address data with spatial location information, enabling geocoding and location-aware applications. The ontology supports business and organizational applications including customer relationship management (CRM), location-based services, and facility management systems.

**Example Usage**: Represent a business location with Contact terms including street address, postal code, phone number, email, hours of operation (business hours), and associated geographic coordinates for location mapping and service discovery.

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
