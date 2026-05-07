

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

The BRENDA Tissue Ontology (BTO) is a structured controlled vocabulary for describing and classifying enzyme sources, including tissues, cell lines, cell types, and cell cultures [#bto-github]_ [#bto-paper]_. Developed as part of the BRENDA enzyme information system, BTO provides standardized terminology for identifying biological sample origins in enzymatic, biochemical, and molecular biology studies [#bto-paper]_.

BTO supports semantic annotation and integration of enzyme-related data by linking tissue and cell-source information to biochemical research records [#bto-github]_ [#bto-paper]_. It includes terms for tissues, anatomical structures, organs, cell cultures, cell types, and cell lines from different organisms, enabling accurate search and comparison of enzymes studied in specific biological contexts [#bto-paper]_.

**Example Usage**:
Annotate an enzyme assay result with a BTO term such as **BTO:0000079** for liver or **BTO:0000142** for kidney to indicate the tissue source of the enzyme sample, enabling semantic search and integration with biochemical databases [#bto-github]_ [#bto-paper]_.

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

References
----------

.. [#bto-github] BRENDA-Enzymes. n.d.
   "BTO: BRENDA Tissue Ontology."
   GitHub repository.
   Available at:
   `https://github.com/BRENDA-Enzymes/BTO <https://github.com/BRENDA-Enzymes/BTO>`_

.. [#bto-paper] Gremse, M., Chang, A., Schomburg, I., Grote, A., Scheer, M., Ebeling, C., and Schomburg, D. 2011.
   "The BRENDA Tissue Ontology (BTO): The first all-integrating ontology of all organisms for enzyme sources."
   *Nucleic Acids Research*, 39, D507--D513.
   DOI: 10.1093/nar/gkq968.
   Available at:
   `https://pubmed.ncbi.nlm.nih.gov/21030441/ <https://pubmed.ncbi.nlm.nih.gov/21030441/>`_
