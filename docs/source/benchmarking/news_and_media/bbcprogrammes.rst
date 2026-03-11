

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

The BBC Programmes Ontology is a specialized vocabulary for describing television and radio programmes, their structure, and broadcast distribution across BBC platforms. It provides standardized terminology for representing programme hierarchies including brands (show franchises), series/seasons (annual or thematic groupings), episodes (individual content pieces), broadcast events (scheduled transmissions), and broadcast services (channels, stations). BBCProgrammes enables precise semantic annotation of broadcast content metadata including airing dates, durations, genres, and relationships between programmes. The ontology facilitates content discovery and programme management across BBC's television and radio platforms by providing standardized semantic structures. BBCProgrammes development was informed by extensive BBC programme data modelling experience, ensuring practical applicability in production systems.

**Example Usage**: Represent a television series using BBCProgrammes terms with brand (Doctor Who), seasons/series (Series 10, Series 11), individual episodes with episode numbers and air dates, and associated broadcast events showing transmission times across different BBC channels.

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
