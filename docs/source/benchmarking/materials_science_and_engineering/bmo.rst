.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - 2019-12-10
       * - **Creator**
         - Janakiram Karlapudi, Prathap Valluru
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Building Material Ontology (BMO) <https://matportal.org/ontologies/BUILDMAT>`_

Building Material Ontology (BMO)
========================================================================================================

The Building Material Ontology (BMO) is a domain ontology designed to represent the main concepts, types, layers, and properties of building materials used in construction and civil engineering [#bmo-doc]_. BMO provides a structured vocabulary for describing material composition, material properties, functional layers, values, units, and relationships between materials in building assemblies [#bmo-doc]_. The ontology supports semantic annotation of building material data, enabling interoperability between construction databases, Building Information Modeling (BIM) systems, and digital construction platforms [#bmo-doc]_. By providing a standardized framework, BMO facilitates material information management, data integration, semantic search, and knowledge sharing in construction workflows [#bmo-doc]_.

**Example Usage**:
Annotate a BIM model with BMO terms to specify the material composition of a wall assembly, including layers such as insulation, concrete, or plaster, material properties such as thermal conductivity, density, and fire resistance, and related values or units. This enables semantic search and integration with construction databases, BIM tools, and building-performance analysis systems [#bmo-doc]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 203
        * - **Total Edges**
          - 420
        * - **Root Nodes**
          - 83
        * - **Leaf Nodes**
          - 68
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 24
        * - **Individuals**
          - 12
        * - **Properties**
          - 62

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.91
        * - **Depth Variance**
          - 1.30
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 83
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 27.29
        * - **Breadth Variance**
          - 1092.20
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 12
        * - **Taxonomic Relations**
          - 20
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 3.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BMO

    ontology = BMO()
    ontology.load("path/to/BMO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bmo-doc] Digital Construction Ontologies. 2021.
   "Digital Construction Materials."
   Ontology documentation.
   Available at:
   `https://digitalconstruction.github.io/Materials/v/0.5/ <https://digitalconstruction.github.io/Materials/v/0.5/>`_
