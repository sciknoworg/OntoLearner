.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - 1.0.1
       * - **Last Updated**
         - 2024-01-30
       * - **Creator**
         - Akhil Thomas, Ali Riza Durmaz
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Materials Mechanics Ontology (MMO) <https://iwm-micro-mechanics-public.pages.fraunhofer.de/ontologies/materials-mechanics-ontology/index-en.html>`_

Materials Mechanics Ontology (MMO)
========================================================================================================

The Materials Mechanics Ontology (MMO) is an application-level ontology developed to support named entity recognition tasks in the materials fatigue domain. It provides a structured vocabulary for describing concepts related to materials mechanics, including crystallographic defects, microstructural entities, and materials fatigue. MMO is designed to facilitate the integration of materials mechanics data, supporting both theoretical and experimental research in materials science.

The ontology employs a class-based modeling approach, defining classes for different types of materials, defects, and microstructures, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. MMO supports the integration of data from various sources, promoting interoperability and data-driven research in materials mechanics.

Typical applications of MMO include the development of new materials with specific mechanical properties, the optimization of materials for fatigue resistance, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, MMO enhances collaboration and innovation in the field of materials mechanics.

**Example Usage**:
Annotate a materials mechanics dataset with MMO terms to specify defect types, microstructural features, and fatigue properties, enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1043
        * - **Total Edges**
          - 2402
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 509
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 428
        * - **Individuals**
          - 0
        * - **Properties**
          - 17

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 8
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.92
        * - **Depth Variance**
          - 5.32
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 17
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 8.89
        * - **Breadth Variance**
          - 21.65
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 566
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MMO

    ontology = MMO()
    ontology.load("path/to/MMO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
