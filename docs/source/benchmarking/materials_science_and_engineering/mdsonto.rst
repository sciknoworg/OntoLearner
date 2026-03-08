
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

MDS-Onto is a domain-level ontology that describes terms in Materials Data Science. It is divided into six large modules: BuiltEnv, Exposure, Chemistry, Manufacture, Characterization, and Geospatial. Each module contains multiple sub-modules such as FTIR, AFM, Chem-Rxn, PV-Module, and Accelerated Exposure, providing a comprehensive framework for representing data and processes in materials science.

MDS-Onto employs a modular approach, defining classes and properties for each module to capture the complexity of materials data science. It supports semantic annotation of materials data, enabling interoperability, data integration, and advanced analysis across research databases and digital platforms. By providing a standardized framework, MDS-Onto facilitates cross-study comparison, materials selection, and knowledge sharing in materials research and industry.

Typical applications include the integration of materials data from various sources, the development of new materials with specific properties, and the optimization of manufacturing processes. The ontology is actively maintained and extended to incorporate new materials, technologies, and research requirements.

**Example Usage**:
Annotate a materials database with MDS-Onto terms to specify material properties, processes, and data, enabling semantic search and integration with materials informatics platforms.


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
