.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 4.0
       * - **Last Updated**
         - 2013-07-01
       * - **Creator**
         - http://oxgiraldo.wordpress.com
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download SMART Protocols Ontology: Document Module (SP-Document) <https://github.com/SMARTProtocols/SMART-Protocols>`_

SMART Protocols Ontology: Document Module (SP-Document)
========================================================================================================
SMART Protocols Ontology: Document Module is an ontology designed to represent metadata used to report an experimental protocol [#sp-document]_ [#sp-github]_. It provides a structured vocabulary for representing experimental protocol documents, protocol metadata, and related descriptive information, supporting semantic documentation of experimental protocols [#sp-document]_.

The ontology employs a class-based modeling approach, defining classes for protocol-related metadata such as protocol title, identifier, authorship, application, provenance, reagents, instruments, samples, objectives, and other information needed to report an experimental protocol [#sp-document]_ [#sp-github]_. Hierarchies and properties are used to organize protocol-document information into structured categories, enabling retrieval, comparison, and analysis of experimental protocol metadata [#sp-document]_. SP-Document supports the integration of protocol descriptions from different sources, promoting interoperability and data-driven research in experimental protocol documentation [#sp-github]_.

Typical applications of SP-Document include experimental protocol reporting, protocol metadata standardization, semantic annotation of protocol documents, protocol repository development, protocol discovery, and integration of protocol descriptions with scientific workflow and laboratory information systems [#sp-document]_ [#sp-github]_. By providing a standardized vocabulary and framework, SP-Document enhances interoperability, reuse, and semantic search in the field of experimental protocol documentation [#sp-document]_.

**Example Usage**:
Annotate an experimental protocol with SP-Document terms to specify the protocol title, identifier, authors, application, provenance, reagents, instruments, samples, objectives, and related metadata. This enables semantic search, protocol comparison, metadata integration, and use within experimental protocol documentation platforms [#sp-document]_ [#sp-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1489
        * - **Total Edges**
          - 3044
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 908
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 400
        * - **Individuals**
          - 45
        * - **Properties**
          - 43

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 9
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.96
        * - **Depth Variance**
          - 4.49
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 69
        * - **Minimum Breadth**
          - 8
        * - **Average Breadth**
          - 32.80
        * - **Breadth Variance**
          - 369.36
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 45
        * - **Taxonomic Relations**
          - 474
        * - **Non-taxonomic Relations**
          - 73
        * - **Average Terms per Type**
          - 2.65
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SPDocument

    ontology = SPDocument()
    ontology.load("path/to/SPDocument-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#sp-document] SMART Protocols. 2013.
   "SMART Protocols Ontology: Document Module."
   Available at:
   `https://vocab.linkeddata.es/SMARTProtocols/myDocumentation_SPdoc_18Abril2017/index_SPdoc_V4.0.html <https://vocab.linkeddata.es/SMARTProtocols/myDocumentation_SPdoc_18Abril2017/index_SPdoc_V4.0.html>`_

.. [#sp-github] Ontology Engineering Group, Universidad Politécnica de Madrid. n.d.
   "SMART-Protocols."
   GitHub Repository.
   Available at:
   `https://github.com/oeg-upm/SMART-Protocols <https://github.com/oeg-upm/SMART-Protocols>`_
