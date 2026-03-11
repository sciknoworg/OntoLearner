

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Storyline
       * - **Current Version**
         - 0.3
       * - **Last Updated**
         - 2013-05-01
       * - **Creator**
         - http://uk.linkedin.com/in/paulwilton, http://www.bbc.co.uk/blogs/internet/authors/Jeremy_Tarling, http://uk.linkedin.com/in/jarredmcginnis
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Storyline Ontology (BBCStoryline) <https://iptc.org/thirdparty/bbc-ontologies/storyline.html>`_

BBC Storyline Ontology (BBCStoryline)
========================================================================================================

The BBC Storyline Ontology is a generic semantic framework for describing, organizing, and managing news stories and narrative content across diverse media publishing platforms. It models the core concept of "Storyline" to distinguish between individual news content pieces (articles, reports, videos) and broader editorial narratives representing events or topics in the world. The ontology captures relationships between stories, events, entities (people, places, organizations), and time periods, enabling sophisticated content organization and discovery. BBCStoryline is designed to be flexible and adaptable, supporting different news publishers' approaches to story organization while providing standardized semantic structures. The ontology facilitates semantic linking of content across media platforms and enables advanced search, recommendation, and editorial workflow systems.

**Example Usage**: Represent a news story about a major political event using BBCStoryline terms to link individual articles (multiple reporters' perspectives), associated entities (politicians, organizations), timeline (chronological events), and related stories covering different aspects of the broader storyline.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 74
        * - **Total Edges**
          - 157
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 53
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 6
        * - **Individuals**
          - 0
        * - **Properties**
          - 12

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
          - 2
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCStoryline

    ontology = BBCStoryline()
    ontology.load("path/to/BBCStoryline-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
