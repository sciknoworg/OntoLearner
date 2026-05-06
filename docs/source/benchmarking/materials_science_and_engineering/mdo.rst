.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Design
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - 2022-08-02
       * - **Creator**
         - Materials Design Division, National Institute for Materials Science (NIMS)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Materials Design Ontology (MDO) <https://github.com/LiUSemWeb/Materials-Design-Ontology/tree/master/>`_

Materials Design Ontology (MDO)
========================================================================================================

The Materials Design Ontology (MDO) is a domain ontology developed to represent knowledge in the materials design field, especially concepts from solid-state physics and computational materials science [#li2020]_ [#mdo-github]_. It defines concepts and relations for describing materials, structures, properties, calculations, and data used in materials design databases [#li2020]_.

MDO is guided by data models from well-known materials databases and the OPTIMADE effort, supporting improved interoperability and data integration across heterogeneous computational materials databases [#li2020]_ [#mdo-github]_. By providing a standardized vocabulary, MDO supports semantic annotation, data access, search, and reuse of materials design data [#li2020]_.

**Example Usage**:
Annotate a computational materials database with MDO terms to specify a material, its crystal structure, calculated properties, calculation information, and related database identifiers, enabling semantic search and integration across materials informatics platforms [#li2020]_ [#mdo-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 76
        * - **Total Edges**
          - 137
        * - **Root Nodes**
          - 14
        * - **Leaf Nodes**
          - 24
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 13
        * - **Individuals**
          - 2
        * - **Properties**
          - 13

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
          - 0.46
        * - **Depth Variance**
          - 0.33
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 8.00
        * - **Breadth Variance**
          - 28.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 2
        * - **Taxonomic Relations**
          - 3
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 2.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MDO

    ontology = MDO()
    ontology.load("path/to/MDO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#li2020] Li, H., Armiento, R., and Lambrix, P. 2020.
   "An Ontology for the Materials Design Domain."
   In *The Semantic Web -- ISWC 2020*, 212--227.
   DOI: 10.1007/978-3-030-62466-8_14.
   Available at:
   `https://arxiv.org/abs/2006.07712 <https://arxiv.org/abs/2006.07712>`_

.. [#mdo-github] LiUSemWeb. n.d.
   "Materials Design Ontology."
   GitHub repository.
   Available at:
   `https://github.com/LiUSemWeb/Materials-Design-Ontology <https://github.com/LiUSemWeb/Materials-Design-Ontology>`_
