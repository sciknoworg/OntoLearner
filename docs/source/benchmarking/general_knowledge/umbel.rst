

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Web Development
       * - **Current Version**
         - 1.50
       * - **Last Updated**
         - May 10, 2016
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - n3
       * - **Download**
         - `Download Upper Mapping and Binding Exchange Layer Vocabulary (UMBEL) <https://github.com/structureddynamics/UMBEL/tree/master/Ontology>`_

Upper Mapping and Binding Exchange Layer Vocabulary (UMBEL)
========================================================================================================

UMBEL (Upper Mapping and Binding Exchange Layer) is a comprehensive reference ontology and interoperability framework designed to facilitate semantic integration and data exchange across diverse domain vocabularies and datasets on the Web. It provides a broad, general-purpose reference structure of approximately 34,000 concepts organized hierarchically, serving as a semantic scaffolding to link, align, and interoperate disparate datasets, domain ontologies, and knowledge bases. UMBEL acts as a bridge layer enabling concept mappings between specialized domain vocabularies, allowing data from different sources to be semantically related and integrated. The vocabulary is designed as a base framework for constructing concept-based domain ontologies that are explicitly designed for semantic interoperability, reducing fragmentation in knowledge representation. UMBEL supports linked data applications by providing standardized concept definitions and mappings that enable automated reasoning and knowledge discovery across heterogeneous information sources.

**Example Usage**: Link concepts from domain-specific ontologies (e.g., medical terms from medical ontologies, product types from e-commerce vocabularies) to corresponding UMBEL concepts to enable cross-domain data integration and semantic reasoning.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1185
        * - **Total Edges**
          - 2868
        * - **Root Nodes**
          - 64
        * - **Leaf Nodes**
          - 302
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 99
        * - **Individuals**
          - 10
        * - **Properties**
          - 42

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 42
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 10.19
        * - **Depth Variance**
          - 83.14
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 162
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 27.42
        * - **Breadth Variance**
          - 1013.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 10
        * - **Taxonomic Relations**
          - 64
        * - **Non-taxonomic Relations**
          - 33
        * - **Average Terms per Type**
          - 10.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import UMBEL

    ontology = UMBEL()
    ontology.load("path/to/UMBEL-ontology.n3")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
