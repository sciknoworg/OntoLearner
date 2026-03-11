.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 4.0
       * - **Last Updated**
         - 2013-07-01
       * - **Creator**
         - http://oxgiraldo.wordpress.com
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download SMART Protocols Ontology: Document Module (SP-Document) <https://github.com/SMARTProtocols/SMART-Protocols>`_

SMART Protocols Ontology: Document Module (SP-Document)
========================================================================================================

SMART Protocols Ontology: Document Module is an ontology designed to represent metadata used to report an experimental protocol. It provides a structured vocabulary for representing experimental protocols, metadata, and related data, supporting both theoretical and experimental research in experimental protocol documentation.

The ontology employs a class-based modeling approach, defining classes for different types of experimental protocols, metadata, and related data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. SP-Document supports the integration of data from various sources, promoting interoperability and data-driven research in experimental protocol documentation.

Typical applications of SP-Document include the development of new experimental protocol documentation methods, the optimization of experimental protocol management practices, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, SP-Document enhances collaboration and innovation in the field of experimental protocol documentation.

**Example Usage**:
Annotate an experimental protocol with SP-Document terms to specify protocol types, metadata, and related data, enabling semantic search and integration with experimental protocol documentation platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1489
        * - **Total Edges**
          - 3044
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 908
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 400
        * - **Individuals**
          - 45
        * - **Properties**
          - 43

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 9
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.96
        * - **Depth Variance**
          - 4.49
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 69
        * - **Minimum Breadth**
          - 8
        * - **Average Breadth**
          - 32.80
        * - **Breadth Variance**
          - 369.36
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 45
        * - **Taxonomic Relations**
          - 474
        * - **Non-taxonomic Relations**
          - 73
        * - **Average Terms per Type**
          - 2.65
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SPDocument

    ontology = SPDocument()
    ontology.load("path/to/SPDocument-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
