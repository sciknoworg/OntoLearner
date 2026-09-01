.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Politics
       * - **Current Version**
         - 0.9
       * - **Last Updated**
         - 2014-01-06
       * - **Creator**
         - https://www.r4isstatic.com/
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Politics News Ontology (BBCPolitics) <https://www.bbc.co.uk/ontologies/politics-ontology>`_

BBC Politics News Ontology (BBCPolitics)
========================================================================================================
The BBC Politics Ontology is an ontology for describing politics, especially local government and elections [#bbcpolitics-ontology]_. It was originally designed for UK local and European elections and provides a structured vocabulary for political concepts such as constituencies, councils, elections, political parties, and statistical geographies [#bbcpolitics-ontology]_.

The ontology defines classes such as Constituency, Council, Election, PoliticalParty, and StatisticalGeography, and links them to broader BBC Core Concepts such as organisations, events, and places [#bbcpolitics-ontology]*. It also defines relationships such as governsGSS, which relates a political organisation such as a council to the statistical geography it governs [#bbcpolitics-ontology]*. By providing a standardized vocabulary, the BBC Politics Ontology supports semantic annotation, content linking, and discovery of political content in BBC linked-data systems [#bbcpolitics-ontology]_.

**Example Usage**:
Annotate a political news article with BBC Politics Ontology terms to specify an election, constituency, council, political party, or governed statistical geography, enabling semantic search and integration with BBC political news and election data [#bbcpolitics-ontology]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 43
        * - **Total Edges**
          - 75
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 30
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 7
        * - **Individuals**
          - 0
        * - **Properties**
          - 5

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
          - 6
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCPolitics

    ontology = BBCPolitics()
    ontology.load("path/to/BBCPolitics-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bbcpolitics-ontology] BBC. 2014.
   "Politics Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/politics.html <https://iptc.org/thirdparty/bbc-ontologies/politics.html>`_
