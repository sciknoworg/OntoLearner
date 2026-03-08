.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Food and Beverage
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - 2014/03/18
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Food Ontology (BBCFood) <https://www.bbc.co.uk/ontologies/food-ontology>`_

BBC Food Ontology (BBCFood)
========================================================================================================

The BBC Food Ontology (BBCFood) is a lightweight ontology designed to represent recipes, ingredients, and culinary concepts for publishing food-related data on the web. It provides a structured vocabulary for describing foods, their components, preparation methods, dietary suitability, menus, courses, seasons, and occasions. BBCFood supports semantic annotation of recipes and food content, enabling interoperability and data integration across recipe websites, nutrition databases, and culinary applications. The ontology is designed for extensibility and can be adapted to a wide range of food data publishing use cases beyond the original BBC context. By providing standardized terms and relationships, BBCFood facilitates advanced search, recommendation, and personalized meal planning. The ontology is maintained as an open resource and is compatible with other food and nutrition ontologies for broader data integration.

**Example Usage**:
Annotate a recipe database with BBCFood terms to specify ingredients, preparation steps, dietary restrictions (e.g., "vegetarian"), and suitable occasions (e.g., "holiday dinner"), enabling semantic search and personalized recipe recommendations.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 108
        * - **Total Edges**
          - 267
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 63
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 17
        * - **Individuals**
          - 0
        * - **Properties**
          - 22

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
          - 5
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCFood

    ontology = BBCFood()
    ontology.load("path/to/BBCFood-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
