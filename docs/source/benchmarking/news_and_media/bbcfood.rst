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

The BBC Food Ontology (BBCFood) is a lightweight ontology for publishing data about recipes, ingredients, menus, and diets on the web [#bbcfood-ontology]_. It provides a structured vocabulary for describing recipes, the foods they are made from, the foods they create, and the diets, menus, seasons, courses, and occasions for which they may be suitable [#bbcfood-ontology]_.

BBCFood originates from a BBC use case, but is designed to be applicable to a wide range of recipe-data publishing scenarios across the web [#bbcfood-ontology]_. By providing linked terms and relationships for food content, the ontology supports semantic annotation, interoperability, data integration, search, and reuse of recipe and culinary information [#bbcfood-ontology]_.

**Example Usage**:
Annotate a recipe database with BBCFood terms to specify recipes, ingredients, menus, diets, courses, seasons, and suitable occasions, enabling semantic search and integration with food and recipe publishing platforms [#bbcfood-ontology]_.

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

References
----------

.. [#bbcfood-ontology] BBC. 2014.
   "Food Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/fo.html <https://iptc.org/thirdparty/bbc-ontologies/fo.html>`_
