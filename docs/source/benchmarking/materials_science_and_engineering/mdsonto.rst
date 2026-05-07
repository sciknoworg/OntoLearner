
.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Data Science
       * - **Current Version**
         - 0.3.1.16
       * - **Last Updated**
         - 2026-02-03
       * - **Creator**
         - SDLE Research Center
       * - **License**
         - CC BY-SA 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download The Modular Ontology for Materials and Data Science (MDS-Onto) <https://cwrusdle.bitbucket.io/files/MDS_Onto/index-en.html>`_

The Modular Ontology for Materials and Data Science (MDS-Onto)
==============================================================================

MDS-Onto is a domain-level ontology for Materials Data Science that provides structured terminology for representing materials-related data and applied data science concepts [#mds-paper]_. It is organized into six major modules: BuiltEnv, Exposure, Chemistry, Manufacture, Characterization, and Geospatial, with sub-modules such as FTIR, AFM, Chem-Rxn, PV-Module, and Accelerated Exposure [#mds-paper]_.

MDS-Onto follows a modular approach, defining classes and properties for each module to represent the complexity of materials data science [#mds-paper]_. It supports semantic annotation, interoperability, data integration, and knowledge graph construction across heterogeneous materials science datasets and digital platforms [#mds-paper]_. By providing a standardized framework, MDS-Onto facilitates data sharing, cross-domain integration, and reuse of materials and data science knowledge [#mds-paper]_.

**Example Usage**:
Annotate a materials database with MDS-Onto terms to specify material properties, manufacturing or synthesis processes, characterization data, exposure conditions, photovoltaic module information, or geospatial metadata, enabling semantic search and integration with materials informatics platforms [#mds-paper]_.


Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4362
        * - **Total Edges**
          - 13095
        * - **Root Nodes**
          - 92
        * - **Leaf Nodes**
          - 2226
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1710
        * - **Individuals**
          - 1
        * - **Properties**
          - 169

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
          - 1.03
        * - **Depth Variance**
          - 2.01
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 92
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 25.75
        * - **Breadth Variance**
          - 1093.94
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1
        * - **Taxonomic Relations**
          - 1648
        * - **Non-taxonomic Relations**
          - 259
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
-------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MDSOnto

    ontology = MDSOnto()
    ontology.load("path/to/MDSOnto-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------
.. [#mds-paper] Rajamohan, B. P., Bradley, A. C. H., Tran, V. D., et al. 2025.
   "Materials Data Science Ontology(MDS-Onto): Unifying Domain Knowledge in Materials and Applied Data Science."
   *Scientific Data*, 12, 628.
   DOI: 10.1038/s41597-025-04938-5.
   Available at:
   `https://www.nature.com/articles/s41597-025-04938-5 <https://www.nature.com/articles/s41597-025-04938-5>`_
