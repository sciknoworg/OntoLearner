.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - General Purpose
       * - **Current Version**
         - 1.0.17
       * - **Last Updated**
         - March 11, 2018
       * - **Creator**
         - Yongqun "Oliver" He (YH)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Life Ontology (LifO) <https://bioportal.bioontology.org/ontologies/LIFO>`_

Life Ontology (LifO)
========================================================================================================

The Life Ontology (LifO) is a general-purpose ontology designed to represent the life processes of organisms and their associated entities and relationships. It provides a structured framework for describing common biological features across diverse organisms, including unicellular prokaryotes like E. coli and multicellular organisms such as humans. LifO captures essential biological concepts such as growth, reproduction, metabolism, and adaptation, enabling researchers to model and analyze life processes in a standardized manner. The ontology supports interoperability between biological databases and facilitates the integration of diverse datasets for comparative studies. LifO is particularly useful in systems biology, evolutionary research, and bioinformatics applications, where a unified representation of life processes is essential for data analysis and hypothesis generation. By providing a common vocabulary for life sciences, LifO enhances data sharing, reproducibility, and collaborative research.

**Example Usage**:
Use LifO to annotate a dataset describing the metabolic pathways of E. coli, linking each pathway to its corresponding life process and associated biological entities, enabling cross-species comparisons and functional analyses.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2140
        * - **Total Edges**
          - 4179
        * - **Root Nodes**
          - 43
        * - **Leaf Nodes**
          - 1522
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 239
        * - **Individuals**
          - 9
        * - **Properties**
          - 98

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.18
        * - **Depth Variance**
          - 0.83
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 65
        * - **Minimum Breadth**
          - 17
        * - **Average Breadth**
          - 41.67
        * - **Breadth Variance**
          - 384.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 9
        * - **Taxonomic Relations**
          - 321
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 9.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import LIFO

    ontology = LIFO()
    ontology.load("path/to/LIFO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
