

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Spectroscopy
       * - **Current Version**
         - 2024-09-23
       * - **Last Updated**
         - 2024-09-23
       * - **Creator**
         - VIBSO Workgroup
       * - **License**
         - Creative Commons Attribution 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Vibrational Spectroscopy Ontology (VIBSO) <https://terminology.tib.eu/ts/ontologies/vibso>`_

Vibrational Spectroscopy Ontology (VIBSO)
========================================================================================================

The Vibrational Spectroscopy Ontology (VIBSO) is a domain-specific vocabulary for comprehensive and standardized semantic description of vibrational spectroscopy experiments and their resulting research data. It provides formal definitions of technical terms and concepts used in vibrational spectroscopy including spectroscopy types (infrared, Raman, NIR), sample preparation methods, measurement parameters, instrumentation, and data analysis procedures. VIBSO enables researchers to annotate spectroscopy datasets with machine-readable semantic metadata, making data FAIR (Findable, Accessible, Interoperable, Reusable) and supporting automated data discovery and integration. The ontology captures the complete experimental context including measurement conditions, instrument specifications, data processing steps, and quality metrics critical for reproducibility and data reuse. VIBSO facilitates semantic interoperability in spectroscopy databases, analytical chemistry platforms, and materials science research by providing unambiguous definitions of spectroscopic concepts.

**Example Usage**: Annotate a Raman spectroscopy experiment with VIBSO terms including spectroscopy type (Raman), sample material, laser wavelength, temperature conditions, and data processing methods to enable automated discovery of similar spectroscopic studies.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4007
        * - **Total Edges**
          - 8009
        * - **Root Nodes**
          - 328
        * - **Leaf Nodes**
          - 2547
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 598
        * - **Individuals**
          - 40
        * - **Properties**
          - 53

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.03
        * - **Depth Variance**
          - 2.77
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1131
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 188.29
        * - **Breadth Variance**
          - 98075.49
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 40
        * - **Taxonomic Relations**
          - 599
        * - **Non-taxonomic Relations**
          - 23
        * - **Average Terms per Type**
          - 2.35
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import VIBSO

    ontology = VIBSO()
    ontology.load("path/to/VIBSO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
