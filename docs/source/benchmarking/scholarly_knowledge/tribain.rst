.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Patricia Kügler
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Tribology and Artificial Intelligence Ontology (TribAIn) <https://github.com/snow0815/tribAIn>`_

Tribology and Artificial Intelligence Ontology (TribAIn)
========================================================================================================

TribAIn is an ontology for the description of tribological experiments and their results. It is designed to be used in the context of the TribAIn project, which aims to develop a knowledge-based system for the design of tribological systems. It provides a structured vocabulary for representing tribological experiments, results, and related data, supporting both theoretical and experimental research in tribology.

The ontology employs a class-based modeling approach, defining classes for different types of tribological experiments, results, and related data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. TribAIn supports the integration of data from various sources, promoting interoperability and data-driven research in tribology.

Typical applications of TribAIn include the development of new tribological experiment methods, the optimization of tribological system design, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, TribAIn enhances collaboration and innovation in the field of tribology.

**Example Usage**:
Annotate a tribological experiment with TribAIn terms to specify experiment types, results, and related data, enabling semantic search and integration with tribology research platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 771
        * - **Total Edges**
          - 1723
        * - **Root Nodes**
          - 163
        * - **Leaf Nodes**
          - 279
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 241
        * - **Individuals**
          - 21
        * - **Properties**
          - 64

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 9
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.56
        * - **Depth Variance**
          - 2.52
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 320
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 72.90
        * - **Breadth Variance**
          - 9158.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 21
        * - **Taxonomic Relations**
          - 324
        * - **Non-taxonomic Relations**
          - 24
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import TribAIn

    ontology = TribAIn()
    ontology.load("path/to/TribAIn-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
