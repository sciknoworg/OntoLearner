

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - General
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - 2024-11-06
       * - **Creator**
         - None
       * - **License**
         - BSD-3-Clause license
       * - **Format**
         - ttl
       * - **Download**
         - `Download Common Core Ontologies (CCO) <https://github.com/CommonCoreOntology/CommonCoreOntologies>`_

Common Core Ontologies (CCO)
========================================================================================================

The Common Core Ontologies (CCO) is a comprehensive suite of eleven interconnected ontologies providing logically well-defined generic terms and relations applicable across all domains of interest. CCO is built on formal semantic principles, ensuring that its concepts are unambiguous, semantically consistent, and applicable to diverse knowledge representation tasks. The ontology covers foundational concepts including objects, events, qualities, locations, and abstract entities, with explicit definitions of relationships between them. CCO is designed for maximum reusability across domain ontologies, enabling developers to extend CCO terms for specialized applications while maintaining semantic interoperability. The ontologies are documented with formal definitions, examples, and competency questions supporting both human understanding and computational reasoning. CCO has been adopted in enterprise information systems, knowledge graph construction, and semantic data integration projects requiring rigorous ontological foundations.

**Example Usage**:
Represent a business domain ontology by extending CCO's generic Object and Event concepts to define company-specific entities (employees, contracts, transactions) and their relationships, ensuring compatibility with other systems using CCO foundations.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 6002
        * - **Total Edges**
          - 13554
        * - **Root Nodes**
          - 19
        * - **Leaf Nodes**
          - 3389
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1539
        * - **Individuals**
          - 350
        * - **Properties**
          - 277

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 10
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.35
        * - **Depth Variance**
          - 5.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 56
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 23.18
        * - **Breadth Variance**
          - 276.88
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 362
        * - **Taxonomic Relations**
          - 1532
        * - **Non-taxonomic Relations**
          - 21
        * - **Average Terms per Type**
          - 10.06
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CCO

    ontology = CCO()
    ontology.load("path/to/CCO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
