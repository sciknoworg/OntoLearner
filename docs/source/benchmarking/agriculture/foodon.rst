

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

FoodOn  is a farm-to-fork food ontology that provides a comprehensive
vocabulary for naming and classifying food materials across the food
supply chain [#foodon-home]_ [#foodon-paper]_. It covers raw harvested
foods, their botanical and zoological origins, and processed food
products intended for both human consumption and animal feed
[#foodon-home]_ [#foodon-paper]_. FoodOn integrates anatomical,
taxonomic, and other reusable ontology terms to support precise semantic
representation of food items, their components, and related food
processes [#foodon-home]_ [#foodon-paper]_. It is designed as an open,
ontology-driven standard that supports consistent food description and
interoperability across government, industry, research, and other
food-related systems [#foodon-paper]_ [#foodon-home]_. Its hierarchical
structure supports relationships among source organisms, anatomical
parts, processing methods, preservation methods, packaging, and final
food products [#foodon-home]_ [#foodon-paper]_. By providing
unambiguous semantic definitions, FoodOn supports standardized naming,
food safety traceability, quality control, nutrition and dietary
research, and data integration across food-related databases and
applications [#foodon-paper]_ [#foodon-home]_.

**Example Usage**: Annotate a food product dataset with FoodOn terms for source organisms,
anatomical parts, processing methods, packaging, and final food products
to enable standardized description, interoperable data exchange, and
traceability across food safety, nutrition, and supply chain systems
[#foodon-home]_ [#foodon-paper]_.

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

References
----------

.. [#foodon-home] FoodOn. n.d. "FoodOn: A farm to fork ontology."
   Available at: https://foodon.org/

.. [#foodon-paper] Dooley, D. M., Griffiths, E. J., Gosal, G. S.,
   Buttigieg, P. L., Hoehndorf, R., Lange, M. C., Schriml, L. M.,
   Brinkman, F. S. L., and Hsiao, W. W. L. 2018.
   "FoodOn: a harmonized food ontology to increase global food
   traceability, quality control and data integration."
   *npj Science of Food* 2:23.
   doi:10.1038/s41538-018-0032-6
