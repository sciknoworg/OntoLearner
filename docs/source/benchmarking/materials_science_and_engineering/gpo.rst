.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Simon Stier
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download General Process Ontology (GPO) <https://github.com/General-Process-Ontology/ontology>`_

General Process Ontology (GPO)
========================================================================================================

The General Process Ontology (GPO) is a domain ontology developed to model processes in materials science and engineering, as well as other scientific and industrial domains. GPO provides a structured vocabulary for representing holistic processes that transform inputs (matter, energy, information) into outputs (products, byproducts, waste) using tools such as devices and algorithms. The ontology supports decomposition of processes into sub-processes, capturing predecessor and successor relationships, and enabling detailed modeling of workflows, manufacturing, and experimental procedures. GPO facilitates semantic annotation of process data, supporting interoperability, data integration, and advanced analytics across research, industry, and regulatory platforms. By providing a standardized framework, GPO enables lifecycle assessment, process optimization, and knowledge sharing in multidisciplinary projects. The ontology is actively maintained and extended to incorporate new process types, technologies, and application domains.

**Example Usage**:
Annotate a manufacturing workflow with GPO terms to specify process steps, input and output materials, tools used, and process dependencies, enabling semantic search and integration with process management systems.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 548
        * - **Total Edges**
          - 923
        * - **Root Nodes**
          - 99
        * - **Leaf Nodes**
          - 270
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 187
        * - **Individuals**
          - 0
        * - **Properties**
          - 17

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.41
        * - **Depth Variance**
          - 1.20
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 223
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 76.14
        * - **Breadth Variance**
          - 5799.55
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GPO

    ontology = GPO()
    ontology.load("path/to/GPO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
