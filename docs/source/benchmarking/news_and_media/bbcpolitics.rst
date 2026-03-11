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

The BBC Politics Ontology provides a formal vocabulary for describing and classifying political concepts, entities, and events as they appear in BBC news coverage. It models key political domain concepts including politicians, political parties, government institutions, legislative processes, electoral systems, and political ideologies. The ontology captures relationships between political entities (e.g., politicians affiliated with parties, parties contesting elections) and enables semantic annotation of news articles, television programs, and online content related to politics. It supports content discovery and automated linking of related political news stories across BBC's diverse platforms and archives. The ontology follows BBC's linked data principles and integrates with other BBC ontologies (People, Places, Organizations) to provide comprehensive semantic context.

**Example Usage**: Annotate a political news article with BBCPolitics terms to identify mentioned politicians (as foaf:Person instances), their party affiliations, relevant legislation being discussed, and electoral contexts.

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
