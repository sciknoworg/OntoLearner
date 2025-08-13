

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Modeling
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2021-01-02
       * - **Creator**
         - Ilian T. Todorov, Martin Thomas Horsch, Michael A. Seaton, Silvia Chiacchiera
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Virtual Materials Marketplace Ontologies (VIMMP) <https://matportal.org/ontologies/VIMMP_ONTOLOGIES>`_

Virtual Materials Marketplace Ontologies (VIMMP)
========================================================================================================

The Virtual Materials Marketplace (VIMMP) project is developing an open platform for providing     and accessing services related to materials modelling. Within VIMMP, a system of marketplace-level ontologies     is developed to characterize services, models, and interactions between users; the European Materials     and Modelling Ontology (EMMO, recently renamed while keeping the original acronym) is employed     as a top-level ontology. The ontologies are used to annotate data that are stored in the ZONTAL Space component     of VIMMP and to support the ingest and retrieval of data and metadata at the VIMMP marketplace front-end.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 6149
        * - **Total Edges**
          - 15298
        * - **Root Nodes**
          - 841
        * - **Leaf Nodes**
          - 1948
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1234
        * - **Individuals**
          - 911
        * - **Properties**
          - 771

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 20
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.17
        * - **Depth Variance**
          - 12.15
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1383
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 263.38
        * - **Breadth Variance**
          - 147256.81
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1763
        * - **Taxonomic Relations**
          - 2474
        * - **Non-taxonomic Relations**
          - 278
        * - **Average Terms per Type**
          - 6.14
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import VIMMP

    ontology = VIMMP()
    ontology.load("path/to/VIMMP-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
