.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Manufacturing
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2020
       * - **Creator**
         - IOF Core Working Group
       * - **License**
         - MIT
       * - **Format**
         - rdf
       * - **Download**
         - `Download Industrial Ontology Foundry (IOF) <https://oagi.org/pages/Released-Ontologies>`_

Industrial Ontology Foundry (IOF)
========================================================================================================

The Industrial Ontology Foundry (IOF) Core Ontology is a foundational ontology for the manufacturing industry, capturing concepts and relationships common across multiple manufacturing domains. It is implemented in RDF and leverages the Basic Formal Ontology (BFO) as its upper-level framework, while also incorporating terms from other domain-independent and mid-level ontologies. IOF provides a standardized vocabulary for describing manufacturing processes, equipment, materials, products, and organizational structures. The ontology is designed to ensure consistency and interoperability across various domain-specific reference ontologies published by the IOF, supporting integration of manufacturing data from diverse sources. IOF enables advanced applications such as digital twins, smart manufacturing, supply chain optimization, and industrial automation. By providing a common semantic foundation, IOF facilitates data sharing, analytics, and knowledge management in the manufacturing sector.

**Example Usage**:
Annotate a smart factory system with IOF terms to describe production lines, machines, materials, and process steps, enabling integration with enterprise resource planning (ERP) and manufacturing execution systems (MES).

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1442
        * - **Total Edges**
          - 2686
        * - **Root Nodes**
          - 13
        * - **Leaf Nodes**
          - 716
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 212
        * - **Individuals**
          - 0
        * - **Properties**
          - 51

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 36
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 7.89
        * - **Depth Variance**
          - 35.71
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 117
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 24.32
        * - **Breadth Variance**
          - 922.11
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 87
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import IOF

    ontology = IOF()
    ontology.load("path/to/IOF-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
