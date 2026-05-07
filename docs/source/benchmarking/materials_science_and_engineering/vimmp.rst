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

The Virtual Materials Marketplace Ontologies (VIMMP) are a system of marketplace-level ontologies developed as part of the Virtual Materials Marketplace project [#vimmp-paper]_. The VIMMP project aims to provide an open platform for providing and accessing services related to materials modelling [#vimmp-paper]_. Within VIMMP, the ontologies are used to characterise services, models, and interactions between users, with the European Materials and Modelling Ontology (EMMO) employed as a top-level ontology [#vimmp-paper]_.

The VIMMP ontologies support semantic annotation of marketplace data stored in the ZONTAL Space component and help with the ingest and retrieval of data and metadata at the VIMMP marketplace frontend [#vimmp-paper]_. By providing a structured semantic framework, the ontologies support interoperability, data management, knowledge sharing, and integration of materials modelling services and workflows [#vimmp-paper]_.

**Example Usage**:
Annotate a materials modelling project with VIMMP ontology terms to specify service types, models, simulation workflows, user interactions, and marketplace metadata, enabling semantic search and integration with materials modelling and marketplace platforms [#vimmp-paper]_.

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

References
----------

.. [#vimmp-paper] Horsch, M. T., Chiacchiera, S., Seaton, M. A., Todorov, I. T., Šindelka, K., Lísal, M., Andreon, B., Bayro Kaiser, E., Mogni, G., Goldbeck, G., Kunze, R., Summer, G., Fiseni, A., Brüning, H., Schiffels, P., and Leite Cavalcanti, W. 2020.
   "Ontologies for the Virtual Materials Marketplace."
   arXiv:1912.01519.
   DOI: 10.48550/arXiv.1912.01519.
   Available at:
   `https://arxiv.org/abs/1912.01519 <https://arxiv.org/abs/1912.01519>`_
