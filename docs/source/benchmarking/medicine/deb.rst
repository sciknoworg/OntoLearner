

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Biomaterials
       * - **Current Version**
         - 06/2021
       * - **Last Updated**
         - Jun 2, 2021
       * - **Creator**
         - Osnat Hakimi
       * - **License**
         - GPL-3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Devices, Experimental scaffolds and Biomaterials Ontology (DEB) <https://github.com/ProjectDebbie/Ontology_DEB>`_

Devices, Experimental scaffolds and Biomaterials Ontology (DEB)
========================================================================================================

The devices, experimental scaffolds, and biomaterials ontology (DEB) is an open resource     for organizing information about biomaterials, their design, manufacture, and biological testing.     It was developed using text analysis for identifying ontology terms from a biomaterials gold standard corpus,     systematically curated to represent the domain's lexicon. Topics covered were validated by members     of the biomaterials research community.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1081
        * - **Total Edges**
          - 2354
        * - **Root Nodes**
          - 533
        * - **Leaf Nodes**
          - 278
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 601
        * - **Individuals**
          - 0
        * - **Properties**
          - 120

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
          - 0.67
        * - **Depth Variance**
          - 0.59
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 533
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 213.80
        * - **Breadth Variance**
          - 43756.96
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 672
        * - **Non-taxonomic Relations**
          - 8
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DEB

    ontology = DEB()
    ontology.load("path/to/DEB-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
