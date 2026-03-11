

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Food and Beverage
       * - **Category**
         - Wine
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - rdf
       * - **Download**
         - `Download Wine Ontology (Wine) <https://github.com/UCDavisLibrary/wine-ontology>`_

Wine Ontology (Wine)
========================================================================================================

The Wine Ontology is a comprehensive RDF-based vocabulary for describing wines, wine-making processes, vineyards, and the wine industry. It provides a detailed classification system for different types of wines (red, white, rosé, sparkling), wine regions, grape varieties, producers, and tasting characteristics. The ontology captures properties such as alcohol content, acidity, vintage year, and flavor profiles, enabling precise semantic representation of wine products and attributes. It integrates with related ontologies for representing food, geography, and commercial information, supporting applications in e-commerce, wine recommendation systems, and food science research. Example: A specific wine instance can be linked to its grape variety (Pinot Noir), wine region (Burgundy), producer, vintage year, and taste descriptors through well-defined ontology properties.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 729
        * - **Total Edges**
          - 1816
        * - **Root Nodes**
          - 84
        * - **Leaf Nodes**
          - 22
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 101
        * - **Individuals**
          - 161
        * - **Properties**
          - 13

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 41
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.51
        * - **Depth Variance**
          - 29.20
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 164
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 17.19
        * - **Breadth Variance**
          - 1612.73
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 161
        * - **Taxonomic Relations**
          - 47
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 4.13
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Wine

    ontology = Wine()
    ontology.load("path/to/Wine-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
