

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

The BBC Storyline Ontology is a generic model for describing and organising news storylines [#bbcstoryline-ontology]_. It uses the central concept of Storyline to distinguish between an individual piece of news content, such as an article or report, and the broader editorial perspective on events occurring in the world [#bbcstoryline-ontology]_.

The ontology supports the organisation of storyline components, which may be ordered using an index, arranged temporally, or represented as a graph to describe parallel developments [#bbcstoryline-ontology]_. By providing a structured semantic framework, the BBC Storyline Ontology supports content organisation, semantic linking, discovery, and management of news narratives across media publishing platforms [#bbcstoryline-ontology]_.

**Example Usage**:
Represent a news storyline about a major political event by linking individual articles, reports, related events, entities, time periods, and parallel developments into a broader editorial storyline, enabling semantic search and organisation of related news content [#bbcstoryline-ontology]_.

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

References
----------

.. [#bbcstoryline-ontology] BBC. 2013.
   "Storyline Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/storyline.html <https://iptc.org/thirdparty/bbc-ontologies/storyline.html>`_
