

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

Hydra is a lightweight vocabulary and ontology for creating hypermedia-driven Web APIs that are self-describing and machine-actionable through semantic web technologies [#hydra-core]_ [#hydra-paper]_. It enables developers to create generic API clients that can automatically discover and interact with APIs by interpreting hypermedia controls and semantic metadata embedded in API responses [#hydra-core]_. Hydra defines core concepts commonly used in Web APIs, such as API documentation, supported classes, supported properties, operations, links, collections, and entry points, providing a standardized way to describe API structure and functionality [#hydra-core]_. The vocabulary enables APIs to be more self-describing and interoperable, allowing clients to understand available state transitions and construct valid HTTP requests without relying only on hardcoded endpoint knowledge [#hydra-core]_ [#hydra-paper]_. Hydra supports Linked Data and REST principles, helping APIs contribute to broader linked data ecosystems while preserving loose coupling, maintainability, evolvability, and scalability [#hydra-paper]_.

**Example Usage**: Define a REST API endpoint for a resource collection using Hydra vocabulary terms to describe available operations such as ``GET``, ``POST``, and ``DELETE``, supported classes, properties and their types, entry points, collections, and hypermedia links to related resources. This enables automated client discovery, interaction, and adaptation to API structure [#hydra-core]_ [#hydra-paper]_.

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

References
----------

.. [#hydra-core] Hydra W3C Community Group. 2021.
   "Hydra Core Vocabulary."
   Available at:
   `https://www.hydra-cg.com/spec/latest/core/ <https://www.hydra-cg.com/spec/latest/core/>`_

.. [#hydra-paper] Lanthaler, Markus, and Christian Gütl. 2013.
   "Hydra: A Vocabulary for Hypermedia-Driven Web APIs."
   *Proceedings of the 6th Workshop on Linked Data on the Web (LDOW 2013)*.
   Available at:
   `https://ceur-ws.org/Vol-996/papers/ldow2013-paper-03.pdf <https://ceur-ws.org/Vol-996/papers/ldow2013-paper-03.pdf>`_
