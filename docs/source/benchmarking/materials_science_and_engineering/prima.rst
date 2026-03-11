

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

PRIMA is a comprehensive ontology that formalizes and captures provenance information essential for understanding the complete lifecycle and traceability of materials science data, experiments, and computational workflows. It provides structured vocabulary for describing the origins, history, transformations, and chain of custody of materials science information from experimental synthesis through characterization to computational modeling. PRIMA enables documentation of experimental procedures, computational methods, instruments used, software tools employed, and human researchers involved in materials science investigations. The ontology captures temporal information (when experiments were conducted), spatial context (where work was performed), and relationships between different research activities and resulting data. PRIMA facilitates reproducibility, data authentication, and knowledge integration in materials science by providing standardized provenance metadata compatible with linked data standards.

**Example Usage**: Annotate a materials science dataset with PRIMA terms describing experimental origin (synthesis method, instrument, date), processing steps applied, computational analyses performed, and final data product generation, enabling complete traceability and reproducibility of materials discovery workflows.

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
