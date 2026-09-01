

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Programmes
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - 2009/02/20
       * - **Creator**
         - https://moustaki.org/foaf.rdf#moustaki
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Programmes Ontology (BBCProgrammes) <https://www.bbc.co.uk/ontologies/programmes-ontology>`_

BBC Programmes Ontology (BBCProgrammes)
========================================================================================================

The BBC Programmes Ontology is a vocabulary for describing television and radio programmes, their structure, and their broadcast distribution [#bbcprogrammes-ontology]_. It covers programme brands, series or seasons, episodes, versions of episodes, broadcast events, broadcast services, and related programme information [#bbcprogrammes-ontology]_.

The ontology is grounded in BBC programme data modelling work and is inspired by the BBC PIPS database schema, which describes how brands, series, episodes, versions, and broadcasts interact with each other [#bbcprogrammes-ontology]_. By providing a standardized semantic structure, the BBC Programmes Ontology supports linked-data publication, programme discovery, metadata integration, and interchange of programme information on the Semantic Web [#bbcprogrammes-ontology]_.

**Example Usage**:
Represent a television programme using BBC Programmes Ontology terms by linking a brand such as **Doctor Who** to its series, episodes, versions, and broadcast events, including transmission information across BBC channels or services [#bbcprogrammes-ontology]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 218
        * - **Total Edges**
          - 620
        * - **Root Nodes**
          - 2
        * - **Leaf Nodes**
          - 129
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 40
        * - **Individuals**
          - 0
        * - **Properties**
          - 48

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
          - 1.57
        * - **Depth Variance**
          - 0.39
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 18
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 9.33
        * - **Breadth Variance**
          - 43.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 40
        * - **Non-taxonomic Relations**
          - 19
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCProgrammes

    ontology = BBCProgrammes()
    ontology.load("path/to/BBCProgrammes-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bbcprogrammes-ontology] BBC. 2009.
   "BBC Programmes Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/po.html <https://iptc.org/thirdparty/bbc-ontologies/po.html>`_
