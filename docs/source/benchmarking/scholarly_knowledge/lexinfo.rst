.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Linguistics
       * - **Current Version**
         - 3.0
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - Apache 2.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download LexInfo (LexInfo) <https://lexinfo.net/index.html>`_

LexInfo (LexInfo)
========================================================================================================

LexInfo is an ontology for associating linguistic information with elements in an ontology at different levels of linguistic description and expressivity [#lexinfo-ontology]_ [#lexinfo-paper]_. It was originally developed to support the lemon model and is now used as a data category ontology for OntoLex-Lemon, providing linguistic categories for describing lexical resources in RDF relative to ontologies [#lexinfo-ontology]_. LexInfo enables the representation of linguistic information such as parts of speech, grammatical gender, number, case, syntactic frames, subcategorization patterns, and other morphosyntactic and lexical properties [#lexinfo-ontology]_ [#lexinfo-paper]_.

The ontology supports ontology-lexicon interfaces by making it possible to connect ontology entities, such as classes, properties, and individuals, with their lexical realizations and linguistic descriptions [#lexinfo-paper]_. This is important for ontology-based information extraction, ontology learning from text, question answering, ontology verbalization, lexical data publication, and multilingual linked data applications [#lexinfo-paper]_. LexInfo provides a reusable semantic vocabulary for describing linguistic features consistently across lexical resources, supporting interoperability between ontologies, lexicons, and natural language processing systems [#lexinfo-ontology]_.

Typical applications of LexInfo include semantic annotation of lexical entries, modeling linguistic features in OntoLex-Lemon lexicons, integrating heterogeneous lexical datasets, supporting ontology verbalization, and enriching knowledge graphs with linguistic metadata [#lexinfo-ontology]_ [#lexinfo-paper]_. By providing a standardized vocabulary for linguistic data categories, LexInfo enhances interoperability and reuse in computational linguistics, semantic web, and ontology engineering workflows [#lexinfo-paper]_.

**Example Usage**:
Annotate an ontology-linked lexical entry with LexInfo terms to specify its part of speech, grammatical number, gender, syntactic behavior, or subcategorization frame. This enables semantic search, ontology verbalization, multilingual lexical data integration, and use of lexical resources in natural language processing applications [#lexinfo-ontology]_ [#lexinfo-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 3351
        * - **Total Edges**
          - 5435
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 2308
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 334
        * - **Individuals**
          - 276
        * - **Properties**
          - 189

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.50
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 288
        * - **Taxonomic Relations**
          - 276
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 11.08
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import LexInfo

    ontology = LexInfo()
    ontology.load("path/to/LexInfo-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#lexinfo-ontology] OntoLex Community Group. n.d.
   "LexInfo: Data Category Ontology for OntoLex-Lemon."
   GitHub Repository.
   Available at:
   `https://github.com/ontolex/lexinfo <https://github.com/ontolex/lexinfo>`_

.. [#lexinfo-paper] Cimiano, Philipp, Paul Buitelaar,
   John McCrae, and Michael Sintek. 2011.
   "LexInfo: A Declarative Model for the Lexicon-Ontology Interface."
   *Journal of Web Semantics* 9(1): 29--51.
   DOI:
   `10.1016/j.websem.2010.11.001 <https://doi.org/10.1016/j.websem.2010.11.001>`_
