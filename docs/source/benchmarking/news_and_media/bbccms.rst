

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Content Management Systems
       * - **Current Version**
         - 3.7
       * - **Last Updated**
         - 2012-12-01
       * - **Creator**
         - LinkedData@bbc.co.uk
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC CMS Ontology (BBCCMS) <https://www.bbc.co.uk/ontologies/cms-ontology>`_

BBC CMS Ontology (BBCCMS)
========================================================================================================

The BBC CMS Ontology is a specialized vocabulary for representing and managing relationships between content management systems, creative content, and the entities that BBC produces content about. It defines standardized terms and structures for Content Management Systems (CMS) to interact with linked data platforms, enabling semantic representation of how content relates to real-world concepts. The ontology captures associations between different instances of the same concept across multiple BBC systems, ensuring consistency and linkage of related entities (people, places, organizations, events) referenced in content. BBCCMS facilitates content integration and semantic linking across BBC's diverse content production systems and publishing platforms. The ontology enables sophisticated content discovery and recommendations by providing explicit relationships between content and the concepts it addresses.

**Example Usage**: Link a BBC news article or program to BBC Core Concepts (people, organizations, places, events) with BBCCMS terms that establish how the same entity is referenced across different content pieces and editorial domains.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 68
        * - **Total Edges**
          - 137
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 41
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 20
        * - **Individuals**
          - 4
        * - **Properties**
          - 2

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
          - 4
        * - **Taxonomic Relations**
          - 17
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 4.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCCMS

    ontology = BBCCMS()
    ontology.load("path/to/BBCCMS-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
