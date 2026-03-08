

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Web and Internet
       * - **Category**
         - Web Development
       * - **Current Version**
         - None
       * - **Last Updated**
         - 13 July 2021
       * - **Creator**
         - Hydra W3C Community Group
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - jsonld
       * - **Download**
         - `Download Hydra Ontology (Hydra) <https://www.hydra-cg.com/spec/latest/core/#references>`_

Hydra Ontology (Hydra)
========================================================================================================

Hydra is a lightweight vocabulary and ontology for creating hypermedia-driven REST APIs that are self-describing and machine-actionable through semantic web technologies. It enables developers to create generic API clients that can automatically discover and interact with APIs by interpreting hypermedia controls and semantic metadata embedded in API responses. Hydra defines core concepts commonly used in Web APIs such as operations, properties, classes, and relationships, providing a standardized way to describe API structure and functionality. The vocabulary enables APIs to be self-documenting and interoperable, allowing clients to dynamically adapt to API changes without hardcoded endpoint knowledge. Hydra supports linked data and semantic web principles, enabling APIs to contribute to the broader linked open data ecosystem.

**Example Usage**: Define a REST API endpoint for a resource collection using Hydra vocabularies to describe available operations (GET, POST, DELETE), supported classes, properties with their types, and hypermedia links to related resources, enabling automated client discovery and interaction.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 154
        * - **Total Edges**
          - 452
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 86
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 2
        * - **Individuals**
          - 14
        * - **Properties**
          - 0

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
          - 14
        * - **Taxonomic Relations**
          - 15
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 14.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Hydra

    ontology = Hydra()
    ontology.load("path/to/Hydra-ontology.jsonld")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
