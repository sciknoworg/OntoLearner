.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Design
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - 2022-08-02
       * - **Creator**
         - Materials Design Division, National Institute for Materials Science (NIMS)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Materials Design Ontology (MDO) <https://github.com/LiUSemWeb/Materials-Design-Ontology/tree/master/>`_

Materials Design Ontology (MDO)
========================================================================================================

The Materials Design Ontology (MDO) is a comprehensive framework developed to represent domain knowledge in the field of materials design, particularly focusing on solid-state physics and computational materials science. MDO provides a structured vocabulary for describing materials, their properties, and design processes, supporting both theoretical and experimental research in materials science.

The ontology employs a class-based modeling approach, defining classes for different types of materials, properties, and design processes, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. MDO supports the integration of data from computational simulations and experimental studies, promoting interoperability and data-driven research in materials design.

Typical applications of MDO include the development of new materials with specific properties, the optimization of materials for industrial applications, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, MDO enhances collaboration and innovation in the field of materials design.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 76
        * - **Total Edges**
          - 137
        * - **Root Nodes**
          - 14
        * - **Leaf Nodes**
          - 24
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 13
        * - **Individuals**
          - 2
        * - **Properties**
          - 13

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.46
        * - **Depth Variance**
          - 0.33
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 8.00
        * - **Breadth Variance**
          - 28.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 2
        * - **Taxonomic Relations**
          - 3
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 2.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MDO

    ontology = MDO()
    ontology.load("path/to/MDO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

**Example Usage**:
Annotate a materials design project with MDO terms to specify material types, design processes, and properties, enabling semantic search and integration with materials informatics platforms.
