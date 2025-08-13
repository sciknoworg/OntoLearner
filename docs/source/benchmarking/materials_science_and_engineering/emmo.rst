

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Modelling
       * - **Current Version**
         - 1.0.0-rc3
       * - **Last Updated**
         - 2024-03
       * - **Creator**
         - European Materials Modelling Council (EMMC)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download The Elementary Multiperspective Material Ontology (EMMO) <https://emmo-repo.github.io/>`_

The Elementary Multiperspective Material Ontology (EMMO)
========================================================================================================

The Elementary Multiperspective Material Ontology (EMMO) is the result of a multidisciplinary effort within the EMMC,     aimed at the development of a standard representational ontology framework based on current materials modelling     and characterization knowledge. Instead of starting from general upper level concepts, as done by other ontologies,     the EMMO development started from the very bottom level, using the actual picture of the physical world coming     from applied sciences, and in particular from physics and material sciences.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 13613
        * - **Total Edges**
          - 30349
        * - **Root Nodes**
          - 281
        * - **Leaf Nodes**
          - 7742
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 2448
        * - **Individuals**
          - 2
        * - **Properties**
          - 181

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 41
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 8.16
        * - **Depth Variance**
          - 107.87
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 552
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 67.24
        * - **Breadth Variance**
          - 14619.32
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 2
        * - **Taxonomic Relations**
          - 16281
        * - **Non-taxonomic Relations**
          - 52
        * - **Average Terms per Type**
          - 2.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EMMO

    ontology = EMMO()
    ontology.load("path/to/EMMO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
