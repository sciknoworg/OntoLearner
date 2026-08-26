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

The SIOC (Semantically-Interlinked Online Communities) Ontology is a Semantic Web vocabulary for representing the structure and content of online communities [#sioc-eswc]_ [#sioc-paper]_. It provides a common semantic model for describing online community environments such as forums, blogs, mailing lists, social-networking systems, and related collaborative platforms [#sioc-eswc]_ [#sioc-paper]_. SIOC represents users, posts, forums, sites, containers, topics, and the relationships connecting community members with the content they create [#sioc-paper]_. The project was developed to overcome information fragmentation between otherwise isolated online community systems by enabling their data to be represented and linked using Semantic Web technologies [#sioc-eswc]_ [#sioc-paper]_. This common representation supports interoperability, integration, querying, and reuse of community information across different applications and platforms [#sioc-eswc]_ [#sioc-paper]_. SIOC can also be combined with other Semantic Web vocabularies to provide richer descriptions of users, social relationships, and online interactions [#sioc-paper]_.

**Example Usage**:
Annotate a forum or blog platform with SIOC terms to describe users, posts, forums, topics, and relationships between community members and content. This provides a machine-readable representation that supports semantic integration and exchange of online community information across different platforms [#sioc-eswc]_ [#sioc-paper]_.

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

.. [#sioc-paper] Passant, A., Bojārs, U., Breslin, J. G.,
   and Decker, S. 2010.
   "The SIOC Project: Semantically-Interlinked Online Communities,
   from Humans to Machines."
   In *Coordination, Organizations, Institutions and Norms
   in Agent Systems V*, Lecture Notes in Computer Science,
   vol. 6069. Springer, Berlin, Heidelberg.
   Available at:
   `https://doi.org/10.1007/978-3-642-14962-7_12
   <https://doi.org/10.1007/978-3-642-14962-7_12>`_

.. [#sioc-eswc] Breslin, J. G., Harth, A., Bojars, U.,
   and Decker, S. 2005.
   "Towards Semantically-Interlinked Online Communities."
   In *The Semantic Web: Research and Applications*,
   ESWC 2005, Lecture Notes in Computer Science,
   vol. 3532. Springer, Berlin, Heidelberg.
   Available at:
   `https://doi.org/10.1007/11431053_34
   <https://doi.org/10.1007/11431053_34>`_
