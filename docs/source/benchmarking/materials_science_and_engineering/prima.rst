

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

The PRovenance Information in MAterials science (PRIMA) ontology is designed to capture provenance information in the materials science domain [#prima-doc]_. It provides a structured vocabulary for describing research activities and the associated agents, equipment, software, techniques, settings, datasets, and other entities involved in materials science workflows [#prima-doc]_.

PRIMA supports the semantic description of experimental and computational research workflows, helping to improve traceability, interoperability, and reuse of materials science data [#prima-doc]_. Its provenance-oriented approach complements broader efforts within the PRIMA initiative to provide consistent terminology and metadata for materials science and engineering [#prima-thesaurus-paper]_. Starting from PRIMA v3, the ontology is further aligned with BFO and PMDco to improve interoperability with other materials science ontology resources [#prima-doc]_.

**Example Usage**:
Annotate a materials science dataset with PRIMA terms to describe the research activity, involved users, equipment, software, techniques, experimental or computational steps, data acquisition and analysis activities, and resulting data products, thereby preserving provenance information needed for traceability and reuse [#prima-doc]_.

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

.. [#prima-doc] Ihsan, A. Z., Jalali, M.,
   and Aversa, R. 2024.
   "PRIMA Ontology - Complete."
   Ontology documentation.
   Available at:
   `https://materials-data-science-and-informatics.github.io/MDMC-NEP-top-level-ontology/PRIMA/complete/ver_2_0/index.html
   <https://materials-data-science-and-informatics.github.io/MDMC-NEP-top-level-ontology/PRIMA/complete/ver_2_0/index.html>`_

.. [#prima-thesaurus-paper] Aversa, R., Boubnov, A.,
   De Angelis, D., Eschke, C., Kabbe, M., Kraus, F.,
   Panighel, M., Thelen, R., and Valentinis, D. 2026.
   "The PRIMA Thesaurus for Materials Science and Engineering."
   *Advanced Engineering Materials*.
   Available at:
   `https://doi.org/10.1002/adem.202503159
   <https://doi.org/10.1002/adem.202503159>`_
