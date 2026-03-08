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

The Building Material Ontology (BMO) is a domain ontology designed to represent the main concepts, types, layers, and properties of building materials used in construction and civil engineering. BMO provides a structured vocabulary for describing material composition, physical and chemical properties, functional layers, and relationships between materials in building assemblies. The ontology supports semantic annotation of building material data, enabling interoperability between construction databases, digital twins, and building information modeling (BIM) systems. BMO is designed for extensibility, allowing integration with other ontologies and standards for sustainability, performance, and regulatory compliance. By providing a standardized framework, BMO facilitates advanced search, material selection, lifecycle analysis, and knowledge sharing in the construction industry. The ontology is actively maintained and extended to incorporate new materials, technologies, and industry requirements.

**Example Usage**:
Annotate a BIM model with BMO terms to specify the material composition of a wall assembly, including layers (e.g., insulation, concrete, plaster), material properties (e.g., thermal conductivity, fire resistance), and sustainability attributes, enabling semantic search and integration with construction databases.

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
