

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.3.0.0
       * - **Last Updated**
         - 03/24/2024
       * - **Creator**
         - SDLE Research Center
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Materials Data Science Ontology (MDS) <https://matportal.org/ontologies/MDS>`_

Materials Data Science Ontology (MDS)
========================================================================================================

Materials Data Science (MDS) is an ontology encompassing multiple domains relevant to materials science,     chemical synthesis and characterizations, photovoltaics and geospatial datasets. The terms used for classes,     subclasses and instances are mapped to PMDCo and BFO Ontologies.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 657
        * - **Total Edges**
          - 1457
        * - **Root Nodes**
          - 63
        * - **Leaf Nodes**
          - 303
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 363
        * - **Individuals**
          - 0
        * - **Properties**
          - 10

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
          - 0.86
        * - **Depth Variance**
          - 0.57
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 87
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 46.00
        * - **Breadth Variance**
          - 997.50
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 351
        * - **Non-taxonomic Relations**
          - 128
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MDS

    ontology = MDS()
    ontology.load("path/to/MDS-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
