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

The Devices, Experimental Scaffolds and Biomaterials Ontology (DEB) is an ontology developed to represent and organize information about biomaterials, medical devices, experimental scaffolds, and their associated biological evaluation data [#deb-paper]_ [#deb-github]_. It provides a structured semantic model for describing biomaterial composition, scaffold and device characteristics, fabrication and processing information, and biological or experimental data associated with biomaterials research [#deb-paper]_. DEB was designed to support the mapping, annotation, integration, and analysis of heterogeneous biomaterials data, helping information from different experiments and databases to be represented in a consistent and machine-readable form [#deb-paper]_. By providing shared terminology and relationships for biomaterials and experimental scaffolds, the ontology supports semantic search, data integration, and comparison of biomaterials research across studies [#deb-paper]_ [#deb-github]_.

**Example Usage**:
Annotate a biomaterials experiment with DEB terms describing the biomaterial or scaffold, device characteristics, fabrication or processing information, and associated biological evaluation data. This enables structured annotation, semantic search, integration, and comparison of biomaterials data across experiments and data sources [#deb-paper]_.

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

References
----------

.. [#deb-github] ProjectDebbie. n.d.
   "Ontology_DEB: The Device, Experimental Scaffolds and Biomaterials Ontology."
   GitHub repository.
   Available at:
   `https://github.com/ProjectDebbie/Ontology_DEB
   <https://github.com/ProjectDebbie/Ontology_DEB>`_

.. [#deb-paper] Hakimi, O., Gelpi, J. L., Krallinger, M.,
   Curi, F., Repchevsky, D., and Ginebra, M.-P. 2020.
   "The Devices, Experimental Scaffolds, and Biomaterials Ontology (DEB):
   A Tool for Mapping, Annotation, and Analysis of Biomaterials Data."
   *Advanced Functional Materials*, 30(16), 1909910.
   Available at:
   `https://doi.org/10.1002/adfm.201909910
   <https://doi.org/10.1002/adfm.201909910>`_
