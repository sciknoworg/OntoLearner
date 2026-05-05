

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

The Semanticscience Integrated Ontology (SIO) is a simple yet comprehensive upper-level ontology that provides foundational types and relations for consistent semantic knowledge representation across physical entities, processes, attributes, and information constructs [#sio-github]_ [#sio-paper]_. SIO defines core abstract concepts such as objects, processes, attributes, qualities, capabilities, functions, quantities, and information entities, enabling researchers to build domain-specific ontologies with consistent semantic foundations [#sio-paper]_. The ontology supports the interconnection of diverse knowledge domains through generalized entity and relationship types, facilitating interoperability across heterogeneous biological and biomedical ontologies [#sio-paper]_. SIO serves as a semantic foundation for linked data and semantic web projects including Bio2RDF and SADI, supporting biomedical data integration, semantic service discovery, and automated knowledge discovery [#sio-github]_ [#sio-paper]_. The ontology enables semantic reasoning and machine-actionable knowledge representation by providing explicit typing, relation hierarchies, and reusable design patterns that computational systems can interpret [#sio-paper]_.

**Example Usage**: Use SIO classes to type entities in a biomedical knowledge graph, such as ``protein``, ``gene``, ``organism``, ``dataset``, or ``data analysis``, and relate them using SIO properties to support automated biomedical data integration, semantic querying, and knowledge discovery [#sio-github]_ [#sio-paper]_.

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

References
----------

.. [#sio-github] MaastrichtU-IDS. n.d.
   "Semanticscience Integrated Ontology (SIO)."
   GitHub Repository.
   Available at:
   `https://github.com/MaastrichtU-IDS/semanticscience <https://github.com/MaastrichtU-IDS/semanticscience>`_

.. [#sio-paper] Dumontier, Michel, et al. 2014.
   "The Semanticscience Integrated Ontology (SIO) for biomedical research and knowledge discovery."
   *Journal of Biomedical Semantics* 5:14.
   DOI:
   `10.1186/2041-1480-5-14 <https://doi.org/10.1186/2041-1480-5-14>`_
