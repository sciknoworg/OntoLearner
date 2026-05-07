.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Social Sciences
       * - **Category**
         - Social Networks
       * - **Current Version**
         - 1.36
       * - **Last Updated**
         - 2018/02/28
       * - **Creator**
         - Data Science Institute, NUI Galway
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Semantically-Interlinked Online Communities (SIOC) <http://rdfs.org/sioc/spec/>`_

Semantically-Interlinked Online Communities (SIOC)
========================================================================================================

The SIOC (Semantically-Interlinked Online Communities) Ontology is a widely used ontology for describing the information and structure of online communities on the Semantic Web [#sioc-spec]_ [#sioc-project]_. It provides a standardized vocabulary for representing discussion forums, blogs, wikis, mailing lists, social networks, and other collaborative platforms [#sioc-spec]_. SIOC enables the modeling of users, posts, threads, forums, sites, containers, topics, and relationships between community members and user-generated content [#sioc-spec]_. By providing a common semantic framework, SIOC facilitates interoperability between social platforms, supports data integration, and enables advanced queries and analytics over online community data [#sioc-project]_ [#sioc-spec]_. The ontology is used in social web applications, social media analysis, digital humanities, and knowledge graph construction to link and analyze user-generated content across platforms [#sioc-project]_. SIOC is designed to be extensible, allowing it to be used together with other vocabularies and modules for richer descriptions of online community data [#sioc-spec]_.

**Example Usage**:
Annotate a forum or blog platform with SIOC terms to describe users, posts, threads, forums, topics, and relationships between community members and content. This enables semantic search, cross-platform analysis, and interoperability of online community interactions [#sioc-spec]_ [#sioc-project]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 230
        * - **Total Edges**
          - 551
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 123
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 14
        * - **Individuals**
          - 0
        * - **Properties**
          - 91

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 0
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.00
        * - **Depth Variance**
          - 0.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 0
        * - **Minimum Breadth**
          - 0
        * - **Average Breadth**
          - 0.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 9
        * - **Non-taxonomic Relations**
          - 31
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SIOC

    ontology = SIOC()
    ontology.load("path/to/SIOC-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#sioc-spec] Breslin, John G., Stefan Decker, Andreas Harth,
   and Uldis Bojars. 2007.
   "SIOC Core Ontology Specification."
   W3C Member Submission.
   Available at:
   `https://www.w3.org/submissions/sioc-spec/ <https://www.w3.org/submissions/sioc-spec/>`_

.. [#sioc-project] SIOC Project. n.d.
   "Semantically-Interlinked Online Communities."
   Available at:
   `https://sioc-project.org/ <https://sioc-project.org/>`_
