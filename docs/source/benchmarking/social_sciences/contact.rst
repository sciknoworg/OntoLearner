

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

Ontology to capture concepts related to contact information (addresses, phone numbers).     Reuses the iContact Ontology developed by the Enterprise Integration Lab in Toronto.     The iContact ontology is extended to introduce a specialized definition of Hours of Operation,     defined as a subclass of both the iContact definition of hours of operation,     and a subclass of the Recurring Event class defined in the iCity Recurring Event ontology.     The Contact ontology also extends the definition of address to include an associated location.

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
