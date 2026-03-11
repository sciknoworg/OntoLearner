

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - General
       * - **Current Version**
         - 1.25-20240924T0027Z-unstable(1.26)
       * - **Last Updated**
         - 24.09.2024
       * - **Creator**
         - Federico Bianchini, Hervé Ménager, Jon Ison, Matúš Kalaš
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download The ontology of data analysis and management (EDAM) <https://terminology.tib.eu/ts/ontologies/edam>`_

The ontology of data analysis and management (EDAM)
========================================================================================================

EDAM is a domain ontology that formalizes concepts, operations, and data types used in computational data analysis and data management across biological sciences and related domains. It provides structured vocabulary for describing bioinformatics analysis workflows, computational operations (alignment, clustering, prediction), data types, data formats, and the relationships between analysis steps. EDAM comprises four main sections: Topic (research domains and concepts), Operation (analysis/processing operations), Data (data types and identifiers), and Format (computational data formats and standards). The ontology is designed for usability by diverse stakeholders including bioinformaticians, tool developers, and researchers, with a relatively simple hierarchical structure to facilitate adoption. EDAM supports standardization of bioinformatics tool descriptions, workflow definitions, and dataset annotations, enabling automated tool discovery and workflow composition.

**Example Usage**: Annotate a bioinformatics tool or service with EDAM terms for Input data (e.g., EDAM:data_0006 for sequence alignment), Operation (e.g., EDAM:operation_0496 for pairwise sequence alignment), Output format (e.g., EDAM:format_1929 for FASTA), and research Topic (e.g., EDAM:topic_0199 for sequence analysis).

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 12367
        * - **Total Edges**
          - 36215
        * - **Root Nodes**
          - 176
        * - **Leaf Nodes**
          - 8223
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3513
        * - **Individuals**
          - 0
        * - **Properties**
          - 12

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 10
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.75
        * - **Depth Variance**
          - 4.24
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 635
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 196.55
        * - **Breadth Variance**
          - 31795.52
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 7916
        * - **Non-taxonomic Relations**
          - 1314
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EDAM

    ontology = EDAM()
    ontology.load("path/to/EDAM-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
