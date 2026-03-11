

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

The BBC Core Concepts Ontology is a foundational vocabulary defining generic concepts that are universally relevant across BBC's diverse content domains including people, places, events, organizations, and themes. It provides a shared semantic model for representing real-world entities that frequently appear in BBC content, enabling consistent annotation and discovery across multiple media types and editorial departments. BBCCoreConcepts is designed to be sufficiently generic to serve as a base ontology, allowing domain experts and specialized ontologies to extend it for specific use cases (e.g., athletes for sports content, politicians for news content) through rdfs:subClassOf relationships. The ontology enables semantic interoperability across BBC's content production systems and linked data platforms by providing standardized definitions of common entities. BBCCoreConcepts facilitates sophisticated content linking and discovery by establishing shared semantic representations of entities referenced across diverse BBC programs and services.

**Example Usage**: Define domain-specific concepts by creating athlete, musician, or politician subclasses of the generic "Person" concept in BBC Core Concepts, enabling both generic searches and domain-specific searches for related content.

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
