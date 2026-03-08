.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Properties
       * - **Current Version**
         - 0.0.8
       * - **Last Updated**
         - None
       * - **Creator**
         - María Poveda-Villalón, Serge Chávez-Feria
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Material Properties Ontology (MAT) <https://bimerr.iot.linkeddata.es/def/material-properties/>`_

Material Properties Ontology (MAT)
========================================================================================================

The Material Properties Ontology (MAT) is designed to provide a comprehensive vocabulary for describing building components, materials, and their properties within the construction industry. It focuses on supporting applications related to building renovation projects by offering a structured framework for representing material characteristics, performance metrics, and relationships between different building elements. MAT encompasses key entities such as materials, components, and properties, and models relationships to capture the complexity of construction materials.

The ontology employs a class-based modeling approach, defining classes for various material types and properties, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. MAT supports the integration of data from design, construction, and renovation projects, promoting interoperability and data-driven research in the construction industry.

Typical applications of MAT include the design and optimization of building materials for energy efficiency, the assessment of material properties for renovation projects, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, MAT enhances collaboration and innovation in the field of construction materials.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 263
        * - **Total Edges**
          - 691
        * - **Root Nodes**
          - 7
        * - **Leaf Nodes**
          - 52
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 140
        * - **Individuals**
          - 0
        * - **Properties**
          - 21

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 11
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.21
        * - **Depth Variance**
          - 11.10
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 12
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.67
        * - **Breadth Variance**
          - 7.22
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 128
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MAT

    ontology = MAT()
    ontology.load("path/to/MAT-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

**Example Usage**:
Annotate a building renovation project with MAT terms to specify material types, properties, and performance metrics, enabling semantic search and integration with construction informatics platforms.
