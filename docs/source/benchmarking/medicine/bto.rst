

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Enzyme
       * - **Current Version**
         - 2021-10-26
       * - **Last Updated**
         - 2021-10-26
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download BRENDA Tissue Ontology (BTO) <https://terminology.tib.eu/ts/ontologies/BTO>`_

BRENDA Tissue Ontology (BTO)
========================================================================================================

The BRENDA Tissue Ontology (BTO) is a structured controlled vocabulary for systematically describing and classifying the tissues, cell lines, cell types, and cell cultures that serve as sources for enzymatic and biochemical studies. Developed as part of the BRENDA (BRaunschweig ENzyme DAtabase) project, BTO provides standardized terminology for identifying experimental sample origins and biological sources in biochemistry and molecular biology research. The ontology includes comprehensive hierarchical classifications of human tissues, animal tissues, plant tissues, and microbial cell types, enabling precise semantic annotation of biological materials used in enzyme research and biotechnology. BTO supports data integration across biochemical databases and enables accurate searches for enzymes studied in specific tissue contexts.

**Example Usage**: Annotate an enzyme assay result with a BTO term like "BTO:0000079" (liver) or "BTO:0000142" (kidney) to indicate the tissue source of the enzyme sample.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 37130
        * - **Total Edges**
          - 86188
        * - **Root Nodes**
          - 5619
        * - **Leaf Nodes**
          - 21886
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 6569
        * - **Individuals**
          - 0
        * - **Properties**
          - 10

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.37
        * - **Depth Variance**
          - 0.68
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 16002
        * - **Minimum Breadth**
          - 9
        * - **Average Breadth**
          - 4411.62
        * - **Breadth Variance**
          - 36150459.73
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 5888
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BTO

    ontology = BTO()
    ontology.load("path/to/BTO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
