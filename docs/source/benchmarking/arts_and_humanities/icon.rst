

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Arts and Humanities
       * - **Category**
         - Art History, Cultural Heritage
       * - **Current Version**
         - 2.1.0
       * - **Last Updated**
         - April 26th, 2024
       * - **Creator**
         - Knowledge Media Institute
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Icon Ontology (ICON) <https://w3id.org/icon/ontology/>`_

Icon Ontology (ICON)
========================================================================================================

The ICON ontology provides a formal framework for high-granularity art
interpretation and analysis. It was developed by conceptualizing Panofsky’s
theory of levels of interpretation, enabling artworks to be systematically
described according to three complementary analytical perspectives:
Pre-iconographical (visual recognition and formal elements), Iconographical
(subject matter and represented themes), and Iconological (deeper symbolic,
cultural, and philosophical meanings) [#icon-paper]_. This three-level
approach enables comprehensive semantic annotation of artworks, capturing
both surface-level visual descriptions and deeper interpretive insights
[#icon-paper]_ [#icon-extension]_. The ontology supports structured
knowledge representation of artistic elements, iconographic themes,
cultural references, and symbolic meanings [#icon-paper]_. It facilitates
semantic interoperability in linked cultural heritage data by aligning with
other ontologies and knowledge bases, including CIDOC-CRM and VIR
[#icon-paper]_ [#icon-doc]_. The ICON ontology enables detailed modelling
of artistic interpretation for art history research, corpus annotation,
and linked data applications, supporting researchers and curators in
analyzing and comparing artworks across interpretation levels
[#icon-paper]_ [#icon-extension]_.

**Example Usage**: Annotate an artwork or museum object with ICON ontology
terms describing pre-iconographical elements, iconographical subjects,
and iconological meanings for example, identifying depicted figures,
their symbolic attributes, and the broader cultural or philosophical
interpretation of the scene to support semantic search, comparative art
historical analysis, and linked data integration across cultural heritage
datasets [#icon-paper]_ [#icon-extension]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 408
        * - **Total Edges**
          - 1091
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 131
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 76
        * - **Individuals**
          - 0
        * - **Properties**
          - 68

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 12
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.92
        * - **Depth Variance**
          - 13.34
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 13
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 8.62
        * - **Breadth Variance**
          - 4.24
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 65
        * - **Non-taxonomic Relations**
          - 4
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ICON

    ontology = ICON()
    ontology.load("path/to/ICON-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#icon-paper] Sartini, B., Baroncini, S., van Erp, M., Tomasi, F.,
   and Gangemi, A. 2023. "ICON: An Ontology for Comprehensive Artistic
   Interpretations."
   *ACM Journal on Computing and Cultural Heritage* 16(3), Article 59: 1-38.
   doi:10.1145/3594724

.. [#icon-extension] Sartini, B. 2023.
   "A Comparative Study of Simple and Complex Art Interpretations in
   Linked Open Data Using ICON Ontology."
   In *Proceedings of the Semantic Web and Ontology Design for Cultural
   Heritage Workshop (SWODCH 2023)*.
   CEUR Workshop Proceedings 3540.
   Available at: `https://ceur-ws.org/Vol-3540/paper4.pdf <https://ceur-ws.org/Vol-3540/paper4.pdf>`_

.. [#icon-doc] ICON Ontology Documentation. n.d.
   "ICON Ontology Documentation 2.0."
   Available at: `https://br0ast.github.io/ICON/ICONOntologyDocumentation2.0/index-en.html <https://br0ast.github.io/ICON/ICONOntologyDocumentation2.0/index-en.html>`_
