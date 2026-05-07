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

The NanoMine Ontology is a domain ontology developed to support research in polymer nanocomposites [#nanomine-github]_ [#nanomine-paper]_. It provides a structured vocabulary for representing relationships between polymer nanocomposite composition, processing methods, microstructure, characterization data, and resulting material properties [#nanomine-paper]_.

NanoMine supports semantic annotation, data integration, search, reuse, and analysis of polymer nanocomposite data [#nanomine-github]_ [#nanomine-paper]_. The ontology helps researchers explore processing-structure-property relationships and supports hypothesis development about how material composition and processing conditions affect nanocomposite performance [#nanomine-paper]_. By providing a standardized semantic framework, NanoMine facilitates interoperability, knowledge sharing, and data-driven research in polymer nanocomposites [#nanomine-github]_ [#nanomine-paper]_.

**Example Usage**:
Annotate a polymer nanocomposite dataset with NanoMine terms to specify polymer matrix, filler material, filler loading, processing method, characterization technique, microstructure information, and measured properties, enabling semantic search and integration with materials informatics platforms [#nanomine-github]_ [#nanomine-paper]_.

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

.. [#nanomine-github] Tetherless World. n.d.
   "nanomine-ontology: Ontology and related data support for the Nanomine project."
   GitHub repository.
   Available at:
   `https://github.com/tetherless-world/nanomine-ontology <https://github.com/tetherless-world/nanomine-ontology>`_

.. [#nanomine-paper] Zhao, H., Wang, Y., Lin, A., Hu, B., Yan, R., McCusker, J., Chen, W., McGuinness, D. L., Schadler, L., and Brinson, L. C. 2018.
   "NanoMine schema: An extensible data representation for polymer nanocomposites."
   *APL Materials*, 6, 111108.
   DOI: 10.1063/1.5046839.
   Available at:
   `https://pubs.aip.org/aip/apm/article/6/11/111108/121743/NanoMine-schema-An-extensible-data-representation <https://pubs.aip.org/aip/apm/article/6/11/111108/121743/NanoMine-schema-An-extensible-data-representation>`_
