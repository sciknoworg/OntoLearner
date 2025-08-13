

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Computer Science
       * - **Current Version**
         - 3.4
       * - **Last Updated**
         - None
       * - **Creator**
         - Knowledge Media Institute, Open University
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Computer Science Ontology (CSO) <https://cso.kmi.open.ac.uk/home>`_

Computer Science Ontology (CSO)
========================================================================================================

The Computer Science Ontology (CSO) is a large-scale ontology of research areas in computer science.     It provides a comprehensive vocabulary of research topics in computing, organized in a hierarchical structure.      This class processes the Computer Science Ontology (CSO) with custom hooks for:     - Topic-based class detection     - superTopicOf relationships     - contributesTo relationships

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 25897
        * - **Total Edges**
          - 152243
        * - **Root Nodes**
          - 94
        * - **Leaf Nodes**
          - 11199
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 0
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.67
        * - **Depth Variance**
          - 0.22
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 187
        * - **Minimum Breadth**
          - 94
        * - **Average Breadth**
          - 140.50
        * - **Breadth Variance**
          - 2162.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 44204
        * - **Non-taxonomic Relations**
          - 49080
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CSO

    ontology = CSO()
    ontology.load("path/to/CSO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
