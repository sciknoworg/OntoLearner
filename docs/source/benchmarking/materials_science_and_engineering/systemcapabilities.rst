.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science, Engineering, Systems
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2017-05-14
       * - **Creator**
         - W3C/OGC Spatial Data on the Web Working Group
       * - **License**
         - W3C Software and Document License
       * - **Format**
         - owl
       * - **Download**
         - `Download System Capabilities Ontology (SystemCapabilities) <https://terminology.tib.eu/ts/ontologies/SSNSYSTEM>`_

System Capabilities Ontology (SystemCapabilities)
========================================================================================================

The System Capabilities Ontology (SystemCapabilities) is designed to describe system capabilities, operating ranges, and survival ranges in materials science and engineering. It provides a structured vocabulary for representing the capabilities and limitations of systems, supporting both theoretical and experimental research in materials science.

The ontology employs a class-based modeling approach, defining classes for different types of systems, capabilities, and ranges, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. SystemCapabilities supports the integration of data from various sources, promoting interoperability and data-driven research in materials science.

Typical applications of SystemCapabilities include the development of new systems with specific capabilities, the optimization of system performance, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, SystemCapabilities enhances collaboration and innovation in the field of materials science.

**Example Usage**:
Annotate a materials science project with SystemCapabilities terms to specify system types, capabilities, and ranges, enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 137
        * - **Total Edges**
          - 268
        * - **Root Nodes**
          - 14
        * - **Leaf Nodes**
          - 47
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 25
        * - **Individuals**
          - 3
        * - **Properties**
          - 8

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.22
        * - **Depth Variance**
          - 0.17
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 9.00
        * - **Breadth Variance**
          - 25.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 45
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SystemCapabilities

    ontology = SystemCapabilities()
    ontology.load("path/to/SystemCapabilities-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
