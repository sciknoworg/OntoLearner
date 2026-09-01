

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Geography
       * - **Category**
         - Geographic Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2019-02-17
       * - **Creator**
         - William R Hogan
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Geographical Entities Ontology (GEO) <https://github.com/mcwdsi/geographical-entity-ontology/blob/master/geo-all.owl>`_

Geographical Entities Ontology (GEO)
========================================================================================================

The Geographical Entities Ontology (GEO) provides a comprehensive inventory and formal representation of geopolitical and geographical entities, including sovereign states, administrative subdivisions, and various geographical regions [#geo-repo]_ [#geo-repo]_. GEO distinguishes between political entities, such as countries, provinces, and cities, and the territorial or regional entities associated with them, enabling precise semantic representation of geographic and geopolitical concepts [#geo-repo]_. The ontology uses hierarchical relationships to model administrative subdivisions and political jurisdictions at multiple levels, including national, state, regional, and local levels [#geo-repo]_ [#geo-repo]_. GEO facilitates location-aware data annotation, enabling applications in geopolitical analysis, administrative reporting, and location-based services to unambiguously identify geographic and political entities [#geo-repo]_. The ontology is designed for integration with other geographic and spatial ontologies, supporting linked data applications in geography, governance, and international relations [#geo-repo]_.

**Example Usage**: Annotate a political news article with GEO terms such as ``France`` as a sovereign state, linked to subdivisions such as ``Île-de-France`` and ``Paris`` as administrative entities, to enable geographic and political context discovery [#geo-repo]_ [#geo-repo]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 108572
        * - **Total Edges**
          - 246406
        * - **Root Nodes**
          - 298
        * - **Leaf Nodes**
          - 54170
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 397
        * - **Individuals**
          - 46948
        * - **Properties**
          - 75

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.91
        * - **Depth Variance**
          - 3.77
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 356
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 95.79
        * - **Breadth Variance**
          - 17126.60
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 34653
        * - **Taxonomic Relations**
          - 430
        * - **Non-taxonomic Relations**
          - 19
        * - **Average Terms per Type**
          - 1386.12
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GEO

    ontology = GEO()
    ontology.load("path/to/GEO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#geo-repo] Hogan, W. R., Hicks, A., Donovan, K. M.,
   and Brochhausen, M. n.d.
   "Geographical Entity Ontology (GEO)."
   GitHub repository.
   Available at:
   `https://github.com/ufbmi/geographical-entity-ontology
   <https://github.com/ufbmi/geographical-entity-ontology>`_
