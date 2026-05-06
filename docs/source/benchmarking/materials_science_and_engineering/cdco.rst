.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
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
         - `Download Crystallographic Defect Core Ontology (CDCO) <https://github.com/OCDO/cdco>`_

Crystallographic Defect Core Ontology (CDCO)
========================================================================================================

The Crystallographic Defect Core Ontology (CDCO) is a domain ontology designed to provide common terminology for crystallographic defects and support data integration in materials science [#cdco-doc]_. CDCO provides a structured vocabulary for representing crystalline materials, crystallographic defects, point defects, line defects, planar defects, and defect complexes [#cdco-doc]_.

The ontology supports semantic annotation of crystallographic defect data by defining relationships such as **has crystallographic defect**, **has defect complex**, and **is part of defect complex** [#cdco-doc]_ [#cdco-hasdefectcomplex]_. The **has defect complex** relation is used to link a crystalline material to a defect complex, where the defect complex represents two or more defects in close proximity that interact with each other [#cdco-hasdefectcomplex]_. By providing a standardized vocabulary, CDCO enables semantic search, data integration, and reuse of defect-related materials data [#cdco-doc]_.

**Example Usage**:
Annotate a materials database with CDCO terms to specify the crystallographic defects present in a crystalline material, such as point defects, line defects, planar defects, or defect complexes. For example, a crystalline material can be linked to a defect complex using **has defect complex**, enabling semantic search and integration with defect-related materials modelling tools [#cdco-doc]_ [#cdco-hasdefectcomplex]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 85
        * - **Total Edges**
          - 123
        * - **Root Nodes**
          - 8
        * - **Leaf Nodes**
          - 53
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 7
        * - **Individuals**
          - 0
        * - **Properties**
          - 2

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
          - 0.11
        * - **Depth Variance**
          - 0.10
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 8
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 4.50
        * - **Breadth Variance**
          - 12.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 4
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CDCO

    ontology = CDCO()
    ontology.load("path/to/CDCO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#cdco-doc] OCDO. n.d.
   "Crystallographic Defect Core Ontology (CDCO)."
   Ontology documentation.
   Available at:
   `https://ocdo.github.io/cdco/ <https://ocdo.github.io/cdco/>`_

.. [#cdco-hasdefectcomplex] OCDO. n.d.
   "has defect complex."
   *Crystallographic Defect Core Ontology (CDCO)*.
   Available at:
   `https://ocdo.github.io/cdco/#/hasDefectComplex <https://ocdo.github.io/cdco/#/hasDefectComplex>`_
