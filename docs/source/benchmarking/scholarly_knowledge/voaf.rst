.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Social Network
       * - **Current Version**
         - 2.3
       * - **Last Updated**
         - 2013-05-24
       * - **Creator**
         - Bernard Vatant
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Vocabulary of a Friend (VOAF) <https://lov.linkeddata.es/vocommons/voaf/v2.3/>`_

Vocabulary of a Friend (VOAF)
========================================================================================================
The Vocabulary of a Friend (VOAF) is a vocabulary specification providing elements allowing the description of vocabularies, such as RDFS vocabularies or OWL ontologies [#voaf-spec]_. It is based on Dublin Core and VoID, and provides a structured vocabulary for representing vocabulary metadata, supporting vocabulary description, discovery, reuse, and management [#voaf-spec]_.

The ontology employs a class-based modeling approach, defining classes for vocabularies and related vocabulary elements, along with properties to describe their characteristics and relationships [#voaf-spec]_. VOAF provides properties for expressing how vocabularies relate to one another, including whether they rely on, extend, specialize, annotate, or otherwise link to other vocabularies [#voaf-spec]_. These relationships enable structured retrieval, dependency tracking, and analysis of vocabulary networks [#voaf-spec]_.

Typical applications of VOAF include vocabulary documentation, vocabulary cataloging, ontology metadata management, linked data vocabulary discovery, vocabulary dependency analysis, and integration of vocabulary descriptions across semantic web platforms [#voaf-spec]_. By providing a standardized vocabulary and framework, VOAF enhances interoperability, reuse, and knowledge sharing in the field of vocabulary management [#voaf-spec]_.

**Example Usage**:
Annotate a vocabulary with VOAF terms to specify its type, metadata, reused vocabularies, extensions, specializations, and relationships to other vocabularies. This enables semantic search, vocabulary discovery, dependency analysis, and integration with vocabulary management platforms [#voaf-spec]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 175
        * - **Total Edges**
          - 304
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 129
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3
        * - **Individuals**
          - 1
        * - **Properties**
          - 21

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
          - 1
        * - **Taxonomic Relations**
          - 4
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import VOAF

    ontology = VOAF()
    ontology.load("path/to/VOAF-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#voaf-spec] VOAF. n.d.
   "Vocabulary of a Friend."
   Available at:
   `http://purl.org/vocommons/voaf <http://purl.org/vocommons/voaf>`_
