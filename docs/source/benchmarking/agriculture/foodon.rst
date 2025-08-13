

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Agriculture
       * - **Category**
         - Diet, Metabolomics, and Nutrition
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2025-01-16
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Food Ontology (FoodON) <http://purl.obolibrary.org/obo/foodon.owl>`_

Food Ontology (FoodON)
========================================================================================================

FoodOn, the food ontology, contains vocabulary for naming food materials and their anatomical and taxonomic origins,     from raw harvested food to processed food products, for humans and domesticated animals.     It provides a neutral and ontology-driven standard for government agencies,     industry, nonprofits and consumers to name and reference food products and their components     throughout the food supply chain.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 176584
        * - **Total Edges**
          - 423840
        * - **Root Nodes**
          - 4834
        * - **Leaf Nodes**
          - 90848
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 47261
        * - **Individuals**
          - 16
        * - **Properties**
          - 197

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 23
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.24
        * - **Depth Variance**
          - 4.81
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 11122
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 1217.12
        * - **Breadth Variance**
          - 6546794.36
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 16
        * - **Taxonomic Relations**
          - 76228
        * - **Non-taxonomic Relations**
          - 2072
        * - **Average Terms per Type**
          - 8.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FoodOn

    ontology = FoodOn()
    ontology.load("path/to/FoodOn-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
