

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Upper Ontology
       * - **Current Version**
         - 12.1.0
       * - **Last Updated**
         - 2024-Feb-27
       * - **Creator**
         - Semantic Arts
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download GIST Upper Ontology (GIST) <https://semanticarts.com/gist>`_

GIST Upper Ontology (GIST)
========================================================================================================

GIST is Semantic Arts' minimalist upper ontology designed specifically for enterprise information systems, providing maximum coverage of typical business concepts with minimal primitives and minimal ambiguity. It emphasizes practical expressiveness and semantic clarity, avoiding unnecessary complexity while maintaining rigorous logical foundations. GIST covers essential business entities including agents (people, organizations), objects, events, measurements, and abstract concepts, with clearly defined relationships between them. The ontology is deliberately lightweight to facilitate adoption and integration into existing enterprise systems while providing sufficient semantic richness for sophisticated business logic representation. GIST supports both simple and complex semantic queries, reasoning, and knowledge graph construction for enterprise data integration and business intelligence applications. The ontology has been widely adopted in financial services, healthcare, and government sectors requiring reliable semantic foundations for data governance.

**Example Usage**:
Design a healthcare enterprise ontology by extending GIST's Agent (to represent physicians, patients), Event (to represent treatments, procedures), and Object (to represent medications, medical devices) concepts to build a comprehensive healthcare knowledge graph for clinical decision support.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1352
        * - **Total Edges**
          - 2543
        * - **Root Nodes**
          - 77
        * - **Leaf Nodes**
          - 633
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 199
        * - **Individuals**
          - 8
        * - **Properties**
          - 113

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 27
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.14
        * - **Depth Variance**
          - 21.06
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 298
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 34.86
        * - **Breadth Variance**
          - 3571.91
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 8
        * - **Taxonomic Relations**
          - 39
        * - **Non-taxonomic Relations**
          - 56
        * - **Average Terms per Type**
          - 8.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GIST

    ontology = GIST()
    ontology.load("path/to/GIST-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
