

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - 2024-01-29
       * - **Creator**
         - Ahmad Zainul Ihsan, Mehrdad Jalali, Rossella Aversa
       * - **License**
         - Creative Commons Attribution 3.0 Unported (CC BY 3.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download PRovenance Information in MAterials science (PRIMA) <https://materials-data-science-and-informatics.github.io/MDMC-NEP-top-level-ontology/PRIMA/complete/ver_2_0/index.html>`_

PRovenance Information in MAterials science (PRIMA)
========================================================================================================

The PRovenance Information in MAterials science (PRIMA) ontology is designed to capture provenance information in the materials science domain [#prima-github]_. It provides a structured vocabulary for describing the origins, history, activities, agents, equipment, software, settings, techniques, and data-related entities involved in materials science research workflows [#prima-github]_.

PRIMA supports the semantic annotation of experimental and computational workflows, enabling traceability, interoperability, data integration, and reuse of materials science information [#prima-github]_. Starting from PRIMA v3, the ontology modules are grounded in BFO and aligned with PMDco v3, improving compatibility with related materials science ontology resources [#prima-github]_. By providing standardized provenance metadata, PRIMA supports reproducibility, data authentication, and knowledge integration in materials science [#prima-github]_.

**Example Usage**:
Annotate a materials science dataset with PRIMA terms to describe the study, project, research users, equipment, software, settings, techniques, data acquisition, data analysis, and generated data products, enabling traceability and reproducibility of materials research workflows [#prima-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 444
        * - **Total Edges**
          - 1073
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 135
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 67
        * - **Individuals**
          - 0
        * - **Properties**
          - 67

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 14
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.39
        * - **Depth Variance**
          - 16.39
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 27
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 7.80
        * - **Breadth Variance**
          - 48.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 186
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PRIMA

    ontology = PRIMA()
    ontology.load("path/to/PRIMA-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#prima-github] Materials Data Science and Informatics. n.d.
   "PRovenance Information in MAterials science (PRIMA)."
   GitHub repository.
   Available at:
   `https://github.com/Materials-Data-Science-and-Informatics/MDMC-NEP-top-level-ontology <https://github.com/Materials-Data-Science-and-Informatics/MDMC-NEP-top-level-ontology>`_
