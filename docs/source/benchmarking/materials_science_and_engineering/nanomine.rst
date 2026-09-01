.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - APACHE 2.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download NanoMine Ontology (NanoMine) <https://github.com/tetherless-world/nanomine-ontology>`_

NanoMine Ontology (NanoMine)
========================================================================================================

The NanoMine Ontology is a domain ontology developed to support research in polymer nanocomposites [#nanomine-ontology-paper]_ [#nanomine-schema]. It provides a structured vocabulary for representing relationships between polymer nanocomposite composition, processing methods, microstructure, characterization data, and resulting material properties [#nanomine-ontology-paper] [#nanomine-schema]_.

NanoMine supports semantic annotation, data integration, search, reuse, and analysis of polymer nanocomposite data [#nanomine-ontology-paper]_ [#nanomine-schema]. The ontology helps researchers explore processing-structure-property relationships and supports hypothesis development about how material composition and processing conditions affect nanocomposite performance [#nanomine-schema]. By providing a standardized semantic framework, NanoMine facilitates interoperability, knowledge sharing, and data-driven research in polymer nanocomposites [#nanomine-ontology-paper]_ [#nanomine-schema]_.

Example Usage:
Annotate a polymer nanocomposite dataset with NanoMine terms to specify polymer matrix, filler material, filler loading, processing method, characterization technique, microstructure information, and measured properties, enabling semantic search and integration with materials informatics platforms [#nanomine-ontology-paper]_ [#nanomine-schema]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 496
        * - **Total Edges**
          - 971
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 263
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 157
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

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
          - 212
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import NanoMine

    ontology = NanoMine()
    ontology.load("path/to/NanoMine-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#nanomine-ontology-paper] V. Rawte, J. McCusker, H. Zhao,
   L. C. Brinson, W. Chen, L. Schadler, and D. L. McGuinness,
   "An Ontology for a Polymer Nanocomposite Community Data Resource,"
   in *Proceedings of the 2017 ACM Web Science Conference
   (WebSci '17)*,
   pp. 411--412, 2017.
   `doi:10.1145/3091478.3098866 <https://doi.org/10.1145/3091478.3098866>`_

.. [#nanomine-schema] H. Zhao, Y. Wang, A. Lin, B. Hu,
   R. Yan, J. McCusker, W. Chen, D. L. McGuinness,
   L. Schadler, and L. C. Brinson,
   "NanoMine schema: An extensible data representation
   for polymer nanocomposites,"
   *APL Materials*, vol. 6, no. 11, Art. 111108, 2018.
   `doi:10.1063/1.5046839 <https://doi.org/10.1063/1.5046839>`_
