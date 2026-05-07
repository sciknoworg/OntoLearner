

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Core Concepts
       * - **Current Version**
         - 1.30
       * - **Last Updated**
         - 2019-11-21
       * - **Creator**
         - jeremy.tarling@bbc.co.uk, tom.hodgkinson@bbc.co.uk
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Core Concepts Ontology (BBCCoreConcepts) <https://www.bbc.co.uk/ontologies/core-concepts-ontology>`_

BBC Core Concepts Ontology (BBCCoreConcepts)
========================================================================================================
The BBC Core Concepts Ontology (BBCCoreConcepts) is a generic BBC ontology for representing people, places, events, organisations, and themes that are relevant across BBC content domains [#bbccoreconcepts-ontology]_. It provides a shared semantic model for describing real-world entities that appear in BBC content and supports consistent annotation across different media types, products, and editorial areas [#bbccoreconcepts-ontology]_.

BBCCoreConcepts is designed to be generic enough for domain experts to extend it with domain-specific concepts, such as athletes or politicians, using ``rdfs:subClassOf`` relationships [#bbccoreconcepts-ontology]_. By providing common entity classes and relationships, the ontology supports semantic interoperability, content linking, discovery, and reuse across BBC linked-data systems [#bbccoreconcepts-ontology]_.

**Example Usage**:
Define domain-specific concepts such as athlete, musician, or politician as subclasses of the generic **Person** concept, enabling both broad searches for people and more specific searches for domain-relevant entities across BBC content [#bbccoreconcepts-ontology]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 122
        * - **Total Edges**
          - 265
        * - **Root Nodes**
          - 4
        * - **Leaf Nodes**
          - 73
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 22
        * - **Individuals**
          - 0
        * - **Properties**
          - 29

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.35
        * - **Depth Variance**
          - 0.63
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 11
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 6.67
        * - **Breadth Variance**
          - 9.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 25
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCCoreConcepts

    ontology = BBCCoreConcepts()
    ontology.load("path/to/BBCCoreConcepts-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bbccoreconcepts-ontology] BBC and IPTC. n.d.
   "Core Concepts Ontology."
   *BBC ontologies*.
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/index.html <https://iptc.org/thirdparty/bbc-ontologies/index.html>`_
