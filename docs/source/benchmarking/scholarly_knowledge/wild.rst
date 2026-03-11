

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

WiLD is a specialized ontology for formal semantic description and representation of computational workflows and scientific data processing pipelines using linked data and semantic web technologies. It provides standardized vocabulary for describing workflow components including workflow steps, data flows, tool/service invocations, and their interdependencies in a machine-readable format. WiLD enables interoperable workflow specification and sharing across diverse scientific computing platforms and workflow management systems by providing uniform semantic representations. The ontology captures essential workflow metadata including execution parameters, input/output specifications, and constraints, supporting workflow automation and optimization. WiLD facilitates reproducible science by enabling systematic documentation of computational methods and data processing procedures in linked data formats.

**Example Usage**: Represent a bioinformatics data processing pipeline using WiLD terms to describe sequential workflow steps (quality control, alignment, variant calling), input datasets, tool invocations (with parameters), and output data products to enable workflow reproducibility and reuse.

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
