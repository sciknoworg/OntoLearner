

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
         - `Download Point Defects Ontology (PODO) <https://github.com/OCDO/podo>`_

Point Defects Ontology (PODO)
========================================================================================================
The Point Defects Ontology (PODO) is a specialized ontology designed to describe point defects in crystalline materials [#podo-doc]_. It provides a structured vocabulary for representing point-defect concepts such as vacancies, interstitials, impurities, antisite defects, Frenkel defects, and Schottky defects [#podo-doc]_.

PODO supports the semantic representation of information related to point defects in crystalline materials, providing a common vocabulary for organizing and describing defect-related concepts [#podo-doc]_. This structured representation can support interoperability, data integration, querying, and reuse of point-defect information across materials science applications [#podo-doc]_.

**Example Usage**:
Annotate experimental or computational materials data with PODO terms to identify point-defect types such as vacancies, interstitials, impurities, antisite defects, Frenkel defects, and Schottky defects, enabling consistent representation and integration of defect-related information [#podo-doc]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 153
        * - **Total Edges**
          - 192
        * - **Root Nodes**
          - 38
        * - **Leaf Nodes**
          - 84
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 12
        * - **Individuals**
          - 0
        * - **Properties**
          - 5

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.57
        * - **Depth Variance**
          - 0.40
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 38
        * - **Minimum Breadth**
          - 6
        * - **Average Breadth**
          - 25.00
        * - **Breadth Variance**
          - 188.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 12
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PODO

    ontology = PODO()
    ontology.load("path/to/PODO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#podo-doc] OCDO. n.d.
   "Point Defects Ontology (PODO)."
   Version 0.0.1.
   Ontology documentation.
   Available at:
   `https://ocdo.github.io/podo/#0.0.1
   <https://ocdo.github.io/podo/#0.0.1>`_
