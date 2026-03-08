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

The FRBRoo (Functional Requirements for Bibliographic Records - object-oriented) initiative is a joint effort of the CIDOC Conceptual Reference Model and Functional Requirements for Bibliographic Records international working groups to establish a formal ontology intended to capture and represent the underlying semantics of bibliographic information and to facilitate the integration, mediation, and interchange of bibliographic and museum information. It provides a structured vocabulary for representing bibliographic records, concepts, and relationships, supporting both theoretical and experimental research in bibliographic information management.

The ontology employs a class-based modeling approach, defining classes for different types of bibliographic records, concepts, and relationships, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. FRBRoo supports the integration of data from various sources, promoting interoperability and data-driven research in bibliographic information management.

Typical applications of FRBRoo include the development of new bibliographic information management methods, the optimization of bibliographic record management practices, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, FRBRoo enhances collaboration and innovation in the field of bibliographic information management.

**Example Usage**:
Annotate a bibliographic record with FRBRoo terms to specify record types, concepts, and relationships, enabling semantic search and integration with bibliographic information management platforms.

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
