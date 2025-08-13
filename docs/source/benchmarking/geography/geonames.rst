

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Geography
       * - **Category**
         - Geographic Knowledge
       * - **Current Version**
         - 3.3
       * - **Last Updated**
         - 2022-01-30
       * - **Creator**
         - Bernard Vatant
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download GeoNames Ontology (GeoNames) <https://www.geonames.org/ontology>`_

GeoNames Ontology (GeoNames)
========================================================================================================

The Geonames ontologies provides elements of description for geographical features,     in particular those defined in the geonames.org database.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4879
        * - **Total Edges**
          - 6631
        * - **Root Nodes**
          - 2
        * - **Leaf Nodes**
          - 4123
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 7
        * - **Individuals**
          - 699
        * - **Properties**
          - 30

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.18
        * - **Depth Variance**
          - 0.43
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 21
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 7.00
        * - **Breadth Variance**
          - 65.50
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 699
        * - **Taxonomic Relations**
          - 18
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 349.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GeoNames

    ontology = GeoNames()
    ontology.load("path/to/GeoNames-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
