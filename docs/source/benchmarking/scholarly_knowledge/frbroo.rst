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

FRBRoo (Functional Requirements for Bibliographic Records - object-oriented) is a formal ontology developed through the harmonization of the FRBR family of bibliographic conceptual models with the CIDOC Conceptual Reference Model (CIDOC CRM) [#frbroo-cidoc]_ [#frbroo-ifla]_. It is intended to capture and represent the underlying semantics of bibliographic information and to facilitate the integration, mediation, and interchange of bibliographic and museum information [#frbroo-cidoc]_. FRBRoo provides an object-oriented conceptual model for representing bibliographic entities, works, expressions, manifestations, items, agents, creation processes, publication events, identifiers, and relationships between cultural heritage resources [#frbroo-ifla]_.

The ontology reuses appropriate parts of CIDOC CRM and maps the entity-relationship models of the FRBR family into an object-oriented form [#frbroo-cidoc]_. This allows bibliographic information to be modeled together with museum and cultural heritage information using a shared semantic framework [#frbroo-cidoc]_ [#frbroo-ifla]_. FRBRoo supports semantic interoperability by making the structure and meaning of bibliographic records more explicit, enabling richer querying, reasoning, data mediation, and integration across library, archive, and museum systems [#frbroo-cidoc]_.

Typical applications of FRBRoo include bibliographic data modeling, cultural heritage knowledge graphs, library and museum data integration, semantic cataloging, authority data linking, and interoperability between bibliographic and museum information systems [#frbroo-ifla]_. By providing a formal ontology aligned with CIDOC CRM, FRBRoo supports the exchange, interpretation, and reuse of bibliographic and cultural heritage metadata across heterogeneous repositories [#frbroo-cidoc]_ [#frbroo-ifla]_.

**Example Usage**:
Annotate a bibliographic record with FRBRoo terms to represent a literary work, its expressions, manifestations, physical items, creators, publication events, identifiers, and relationships to museum or archival objects. This enables semantic search, cultural heritage data integration, and cross-domain discovery across library and museum information systems [#frbroo-cidoc]_ [#frbroo-ifla]_.

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

.. [#frbroo-ifla] IFLA. n.d.
   "FRBRoo model."
   Available at:
   `https://www.iflastandards.info/fr/frbr/frbroo.html <https://www.iflastandards.info/fr/frbr/frbroo.html>`_
