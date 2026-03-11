

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Basic
       * - **Current Version**
         - 1.59
       * - **Last Updated**
         - 03/25/2024
       * - **Creator**
         - M. Dumontier
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Semanticscience Integrated Ontology (SIO) <https://bioportal.bioontology.org/ontologies/SIO>`_

Semanticscience Integrated Ontology (SIO)
========================================================================================================

The Semanticscience Integrated Ontology (SIO) is a simple yet comprehensive upper-level ontology that provides foundational types and relations for consistent semantic knowledge representation across physical entities, processes, and information constructs. SIO defines core abstract concepts such as objects, processes, attributes, and information entities, enabling researchers to build domain-specific ontologies with consistent semantic foundations. The ontology supports interconnection of diverse knowledge domains through its generalized entity and relationship types, facilitating interoperability across heterogeneous biological and biomedical ontologies. SIO serves as the semantic backbone for major linked data projects including Bio2RDF (which integrates biological databases) and SADI (Semantic Automated Discovery and Integration framework). The ontology enables semantic reasoning and automated knowledge discovery by providing explicit typing and relationship hierarchies that computationally systems can interpret.

**Example Usage**: Use SIO classes to type entities in a knowledge graph (e.g., SIO:Protein, SIO:Gene, SIO:Organism) and relate them via SIO properties (e.g., SIO:is-derived-from, SIO:encodes, SIO:has-function) for automated biomedical data integration and discovery.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 7811
        * - **Total Edges**
          - 15701
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 4921
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1726
        * - **Individuals**
          - 0
        * - **Properties**
          - 212

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 20
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 6.67
        * - **Depth Variance**
          - 12.94
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 186
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 63.71
        * - **Breadth Variance**
          - 3373.16
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 2019
        * - **Non-taxonomic Relations**
          - 65
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SIO

    ontology = SIO()
    ontology.load("path/to/SIO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
