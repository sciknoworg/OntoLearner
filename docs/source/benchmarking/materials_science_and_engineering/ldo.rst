.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Defects
       * - **Current Version**
         - 1.0.0
       * - **Last Updated**
         - None
       * - **Creator**
         - https://orcid.org/0000-0001-7564-7990
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Line Defect Ontology (LDO) <https://github.com/OCDO/ldo>`_

Line Defect Ontology (LDO)
========================================================================================================

The Line Defect Ontology (LDO) is a domain ontology designed to describe line defects in crystalline materials, such as dislocations and disclinations [#ldo-github]_. LDO provides a structured vocabulary for representing line-defect concepts and their relationships, supporting the semantic description of linear defects in crystalline materials [#ldo-github]_.

The ontology enables semantic annotation of experimental and computational data related to line defects, supporting interoperability, data integration, semantic search, and reuse across materials science databases and research workflows [#ldo-github]_. By providing a standardized vocabulary, LDO facilitates knowledge sharing and comparison of line-defect information in materials science and engineering [#ldo-github]_.

**Example Usage**:
Annotate a transmission electron microscopy (TEM) dataset or computational materials dataset with LDO terms to specify line defects such as dislocations or disclinations, enabling semantic search and integration with crystallographic defect and materials modelling databases [#ldo-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 111
        * - **Total Edges**
          - 207
        * - **Root Nodes**
          - 6
        * - **Leaf Nodes**
          - 49
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 30
        * - **Individuals**
          - 0
        * - **Properties**
          - 11

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 4
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.25
        * - **Depth Variance**
          - 1.56
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 6
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 3.20
        * - **Breadth Variance**
          - 2.96
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 21
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import LDO

    ontology = LDO()
    ontology.load("path/to/LDO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#ldo-github] OCDO. n.d.
   "Line Defect Ontology (LDO)."
   GitHub repository.
   Available at:
   `https://github.com/OCDO/ldo <https://github.com/OCDO/ldo>`_
