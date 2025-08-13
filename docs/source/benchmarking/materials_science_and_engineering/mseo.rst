

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Thomas Hanke, Fraunhofer IWM
       * - **License**
         - MIT License
       * - **Format**
         - ttl
       * - **Download**
         - `Download Materials Science and Engineering Ontology (MSEO) <https://github.com/Mat-O-Lab/MSEO>`_

Materials Science and Engineering Ontology (MSEO)
========================================================================================================

MSEO utilizes the IOF Ontology stack giving materials scientists and engineers the ability     to represent their experiments and resulting data. The goal is to create machine and human readable sematic data     which can be easily digested by other science domains. It is a product of the joint venture Materials Open Lab Project     between the Bundesanstalt für Materialforschung und -prüfung (BAM) and the Fraunhofer Group MATERIALS     and uses the BWMD ontology created by Fraunhofer IWM as a starting point.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 543
        * - **Total Edges**
          - 782
        * - **Root Nodes**
          - 12
        * - **Leaf Nodes**
          - 396
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 138
        * - **Individuals**
          - 0
        * - **Properties**
          - 2

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 4
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.44
        * - **Depth Variance**
          - 1.58
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 18
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 9.60
        * - **Breadth Variance**
          - 24.24
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 102
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MSEO

    ontology = MSEO()
    ontology.load("path/to/MSEO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
