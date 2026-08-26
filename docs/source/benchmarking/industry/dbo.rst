.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Building Information
       * - **Current Version**
         - 0.0.1
       * - **Last Updated**
         - 02/23/2023
       * - **Creator**
         - Google
       * - **License**
         - Apache 2.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Digital Buildings Ontology (DBO) <https://github.com/google/digitalbuildings?tab=readme-ov-file>`_

Digital Buildings Ontology (DBO)
========================================================================================================

The Digital Buildings Ontology (DBO) is a structured vocabulary developed by Google for representing information about buildings and building-installed equipment [#dbo-github]_ [#dbo-iswc]_. DBO provides a semantic model for describing building assets, physical spaces, equipment, entity types, operational states, fields, units, and relationships in smart-building environments [#dbo-github]_ [#dbo-iswc]_. The ontology supports the integration and consistent representation of heterogeneous building data through a common semantic model and associated validation tooling [#dbo-github]_ [#dbo-ldac]_. DBO is designed to be extensible and applicable across different buildings and equipment configurations, supporting scalable deployment and reuse of building-management applications [#dbo-iswc]_ [#dbo-ldac]_. By standardizing how building systems and their relationships are represented, DBO supports building data management, monitoring, analytics, and interoperability across smart-building environments [#dbo-github]_ [#dbo-iswc]_. The ontology is open source and maintained through Google's Digital Buildings repository [#dbo-github]_.

**Example Usage**: Annotate a smart-building system with DBO terms to describe HVAC equipment, lighting systems, sensors, telemetry fields, operational states, and spatial locations, enabling consistent building-data representation, validation, monitoring, and integration with building-management applications [#dbo-github]_ [#dbo-iswc]_ [#dbo-ldac]_.
Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 13152
        * - **Total Edges**
          - 32491
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 686
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3032
        * - **Individuals**
          - 35
        * - **Properties**
          - 7

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.57
        * - **Depth Variance**
          - 0.82
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 3
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.75
        * - **Breadth Variance**
          - 0.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 35
        * - **Taxonomic Relations**
          - 18738
        * - **Non-taxonomic Relations**
          - 12
        * - **Average Terms per Type**
          - 2.06
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DBO

    ontology = DBO()
    ontology.load("path/to/DBO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#dbo-github] Google. n.d.
   "Digital Buildings."
   GitHub Repository.
   Available at:
   `https://github.com/google/digitalbuildings <https://github.com/google/digitalbuildings>`_

.. [#dbo-iswc] Berkoben, K., Kaed, C., and Sodorff, T. 2020.
   "A Digital Buildings Ontology for Google's Real Estate."
   In *ISWC 2020 Posters, Demos and Industry Tracks*.
   Available at:
   `https://ceur-ws.org/Vol-2721/paper510.pdf
   <https://ceur-ws.org/Vol-2721/paper510.pdf>`_

.. [#dbo-ldac] Kaed, C., Berkoben, K. 2020.
   "Digital Buildings."
   Presented at the 8th Linked Data in Architecture
   and Construction Workshop (LDAC 2020).
   Available at:
   `https://linkedbuildingdata.net/ldac2020/files/presentations/LDAC2020_IND6_CharbelKaed.pdf
   <https://linkedbuildingdata.net/ldac2020/files/presentations/LDAC2020_IND6_CharbelKaed.pdf>`_
