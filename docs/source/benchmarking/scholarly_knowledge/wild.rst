

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2020-06-10
       * - **Creator**
         - Tobias Käfer
       * - **License**
         - DBpedia License
       * - **Format**
         - ttl
       * - **Download**
         - `Download Workflows in Linked Data (WiLD) <https://databus.dbpedia.org/ontologies/purl.org/wild--vocab/2020.06.10-210552>`_

Workflows in Linked Data (WiLD)
========================================================================================================
WiLD is an ontology for describing, specifying, monitoring, and executing workflows in Linked Data environments [#wild-home]_ [#wild-paper]_. It provides a structured vocabulary for representing workflow models, workflow instances, activities, execution order, data flow, and dependencies between workflow components [#wild-paper]_. WiLD focuses on workflows whose components interact through read-write Linked Data interfaces, making workflow descriptions machine-readable and suitable for semantic web applications [#wild-paper]_. The ontology supports the formal representation of workflow structure and execution semantics, helping systems document, exchange, monitor, and reuse workflow descriptions in a consistent way [#wild-home]_ [#wild-paper]_. By providing a linked data-based workflow model, WiLD can support reproducibility, automation, workflow sharing, and semantic integration of computational or data-processing processes [#wild-paper]_.

**Example Usage**: Represent a bioinformatics data-processing pipeline using WiLD terms to describe sequential workflow steps such as quality control, alignment, and variant calling, together with input datasets, execution order, tool or service invocations, intermediate data, and output data products. This enables workflow documentation, semantic search, monitoring, reproducibility, and reuse across Linked Data-based workflow systems [#wild-home]_ [#wild-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 50
        * - **Total Edges**
          - 91
        * - **Root Nodes**
          - 21
        * - **Leaf Nodes**
          - 9
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 16
        * - **Individuals**
          - 4
        * - **Properties**
          - 0

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
          - 0.58
        * - **Depth Variance**
          - 0.33
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 22
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 15.00
        * - **Breadth Variance**
          - 84.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 4
        * - **Taxonomic Relations**
          - 9
        * - **Non-taxonomic Relations**
          - 4
        * - **Average Terms per Type**
          - 2.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import WiLD

    ontology = WiLD()
    ontology.load("path/to/WiLD-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#wild-home] WiLD. n.d.
   "WiLD - Workflows in Linked Data."
   Available at:
   `https://purl.org/wild <https://purl.org/wild>`_

.. [#wild-paper] Käfer, Tobias, and Andreas Harth. 2018.
   "Specifying, Monitoring, and Executing Workflows in Linked Data Environments."
   *The Semantic Web -- ISWC 2018*.
   Available at:
   `https://arxiv.org/pdf/1804.05044 <https://arxiv.org/pdf/1804.05044>`_
