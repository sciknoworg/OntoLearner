

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Provenance
       * - **Current Version**
         - 1.9
       * - **Last Updated**
         - 2012-12-01
       * - **Creator**
         - LinkedData@bbc.co.uk
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Provenance News Ontology (BBCProvenance) <https://www.bbc.co.uk/ontologies/provenance-ontology>`_

BBC Provenance News Ontology (BBCProvenance)
========================================================================================================

The BBC Provenance News Ontology is a specialized vocabulary for capturing and representing provenance metadata about data quality, source attribution, and immediate data providers in RDF knowledge graphs and semantic web applications. It focuses on recording immediate data providers (e.g., which internal BBC team or external service provided data) rather than ultimate sources, enabling accountability and quality tracking in linked data systems. BBCProvenance applies provenance annotations to named graphs (quads in RDF stores), providing a fourth dimension to triples that enables context-aware data management and versioning. The ontology supports data governance and management in linked data platforms by providing standardized provenance metadata structures. BBCProvenance facilitates trust and quality assessment in semantic web applications by enabling transparent tracking of data origins and transformations.

**Example Usage**: Annotate geodata in a named graph with BBCProvenance terms indicating that the data was provided by the BBC Locator team (immediate provider) on a specific date, with specific quality assurance level, enabling proper attribution and version tracking.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 74
        * - **Total Edges**
          - 151
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 48
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 7
        * - **Individuals**
          - 1
        * - **Properties**
          - 18

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
          - 6
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCProvenance

    ontology = BBCProvenance()
    ontology.load("path/to/BBCProvenance-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
