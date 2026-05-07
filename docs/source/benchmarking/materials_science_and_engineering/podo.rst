

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
The Point Defect Ontology (PODO) is a specialized ontology designed to describe point defects in crystalline materials [#podo-github]_. It provides a structured vocabulary for representing point-defect concepts such as vacancies, interstitials, impurities, antisite defects, Frenkel defects, and Schottky defects [#podo-github]_.

PODO supports semantic annotation of experimental and computational data related to point defects, enabling interoperability, semantic search, data integration, and reuse across materials science databases and research workflows [#podo-github]_. By providing a standardized representation of point-defect knowledge, PODO helps organize and compare defect-related information in crystalline materials [#podo-github]_.

**Example Usage**:
Annotate a first-principles DFT study of point defects in semiconductors with PODO terms to specify point-defect types such as vacancies, interstitials, impurities, antisite defects, Frenkel defects, or Schottky defects, enabling semantic search and integration with materials informatics platforms [#podo-github]_.

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

.. [#podo-github] OCDO. n.d.
   "Point Defects Ontology (PODO)."
   GitHub repository.
   Available at:
   `https://github.com/OCDO/podo <https://github.com/OCDO/podo>`_s
