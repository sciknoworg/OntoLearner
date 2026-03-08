.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Domain Ontology
       * - **Current Version**
         - 1.3.1.1
       * - **Last Updated**
         - Feb. 9, 2007
       * - **Creator**
         - Chris Stoeckert, Helen Parkinson, Trish Whetzel, Paul Spellman, Catherine A. Ball, Joseph White, John Matese, Liju Fan, Gilberto Fragoso, Mervi Heiskanen, Susanna Sansone, Helen Causton, Laurence Game, Chris Taylor
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download MGED Ontology (MGED) <https://mged.sourceforge.net/ontologies/MGEDontology.php/>`_

MGED Ontology (MGED)
========================================================================================================

The MGED Ontology (MGED) is a domain-specific ontology designed to standardize the description of microarray experiments. It provides a structured vocabulary for representing experimental designs, protocols, and data in the context of microarray gene expression studies. The ontology is divided into two components: the MGED Core Ontology, which aligns with the Microarray Gene Expression (MAGE) standard, and the MGED Extended Ontology, which introduces additional classes and associations beyond the MAGE specification. MGED facilitates interoperability between microarray data repositories, enabling researchers to share, compare, and analyze experimental data effectively. By providing a common framework for describing experimental metadata, MGED supports reproducibility, data integration, and meta-analysis in functional genomics research. The ontology is widely used in bioinformatics tools and databases to annotate experimental datasets and ensure compliance with community standards.

**Example Usage**:
Annotate a microarray experiment with MGED terms to describe the experimental design, sample preparation protocols, and data processing steps, ensuring that the dataset is interoperable with other repositories and tools.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 3427
        * - **Total Edges**
          - 5101
        * - **Root Nodes**
          - 730
        * - **Leaf Nodes**
          - 2171
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 233
        * - **Individuals**
          - 681
        * - **Properties**
          - 121

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 11
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.38
        * - **Depth Variance**
          - 2.09
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1771
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 282.92
        * - **Breadth Variance**
          - 244751.41
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 743
        * - **Taxonomic Relations**
          - 541
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 7.82
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MGED

    ontology = MGED()
    ontology.load("path/to/MGED-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
