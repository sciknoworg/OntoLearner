

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.3.1
       * - **Last Updated**
         - 2025-03-10
       * - **Creator**
         - Metadata4Ing Workgroup
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Metadata for Intelligent Engineering (Metadata4Ing) <https://git.rwth-aachen.de/nfdi4ing/metadata4ing/metadata4ing>`_

Metadata for Intelligent Engineering (Metadata4Ing)
========================================================================================================

The ontology Metadata4Ing provides a framework for the semantic description of research data     and of the whole data generation process, embracing the object of investigation,     all sample and data manipulation methods and tools, the data files themselves,     and the roles of persons and institutions. The structure and application of the ontology     are based on the principles of modularity and inheritance.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1032
        * - **Total Edges**
          - 1517
        * - **Root Nodes**
          - 109
        * - **Leaf Nodes**
          - 731
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 48
        * - **Individuals**
          - 47
        * - **Properties**
          - 100

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.54
        * - **Depth Variance**
          - 1.36
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 413
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 109.75
        * - **Breadth Variance**
          - 18099.19
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 37
        * - **Taxonomic Relations**
          - 44
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 9.25
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Metadata4Ing

    ontology = Metadata4Ing()
    ontology.load("path/to/Metadata4Ing-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
