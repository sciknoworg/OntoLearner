.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Bibliographic Records
       * - **Current Version**
         - 2.4
       * - **Last Updated**
         - November 2015
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Functional Requirements for Bibliographic Records - object-oriented (FRBRoo) <https://ontome.net/namespace/6#summary>`_

Functional Requirements for Bibliographic Records - object-oriented (FRBRoo)
========================================================================================================

FRBRoo (Functional Requirements for Bibliographic Records - object-oriented) is a formal ontology developed through the harmonization of the FRBR family of bibliographic conceptual models with the CIDOC Conceptual Reference Model (CIDOC CRM) [#frbroo-cidoc]_. Its purpose is to express bibliographic concepts in an object-oriented form that is compatible with CIDOC CRM and to support the integration of bibliographic and museum information within a shared semantic framework [#frbroo-cidoc]_.

FRBRoo reuses relevant parts of CIDOC CRM and reformulates FRBR concepts in terms of classes, properties, events, and relationships [#frbroo-cidoc]_. It provides formal representations for bibliographic entities and processes such as works, expressions, manifestations, items, creation activities, publication activities, identifiers, and relationships between intellectual or physical resources [#frbroo-cidoc]_. By aligning bibliographic modeling with CIDOC CRM, FRBRoo supports semantic interoperability and the integration of information maintained by libraries, museums, archives, and other cultural heritage institutions [#frbroo-cidoc]_.

**Example Usage**:
Represent a literary work and its related expressions, manifestations, physical items, creators, and publication activities using FRBRoo classes and properties. This allows bibliographic information to be linked with museum or cultural heritage information modeled using CIDOC CRM [#frbroo-cidoc]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 491
        * - **Total Edges**
          - 886
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 344
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 83
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

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
          - 83
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FRBRoo

    ontology = FRBRoo()
    ontology.load("path/to/FRBRoo-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#frbroo-cidoc] International Working Group on FRBR and CIDOC CRM Harmonisation. 2015.
   "Definition of Object-Oriented FRBR."
   Available at:
   `https://cidoc-crm.org/sites/default/files/FRBRoo_V3.0.pdf <https://cidoc-crm.org/sites/default/files/FRBRoo_V3.0.pdf>`_
