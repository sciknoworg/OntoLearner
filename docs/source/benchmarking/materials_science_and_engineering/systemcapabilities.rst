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

The System Capabilities Ontology (SystemCapabilities) is an ontology module designed to describe system capabilities, operating ranges, and survival ranges [#systemcapabilities-w3c]_ [#systemcapabilities-bioregistry]_. It provides a structured vocabulary for representing what a system is capable of doing under specified conditions, including capability properties, operating properties, survival properties, operating ranges, and survival ranges [#systemcapabilities-w3c]_.

SystemCapabilities is part of the SSN/SOSA ontology framework and is used to describe capabilities and limitations of systems such as sensors and actuators [#systemcapabilities-w3c]_. The ontology supports semantic annotation, interoperability, data integration, and reuse of system-related information across sensor, engineering, and data-management applications [#systemcapabilities-w3c]_.

**Example Usage**:
Annotate a sensor or engineering system with SystemCapabilities terms to specify its measurement capability, operating range, survival range, accuracy, frequency, latency, or environmental limits, enabling semantic search and integration with sensor-network and engineering data platforms [#systemcapabilities-w3c]_.

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

References
----------

.. [#systemcapabilities-w3c] W3C and OGC. 2017.
   "Semantic Sensor Network Ontology: System capabilities, operating ranges, and survival ranges."
   W3C Recommendation.
   Available at:
   `https://www.w3.org/TR/vocab-ssn/#System-capabilities <https://www.w3.org/TR/vocab-ssn/#System-capabilities>`_

.. [#systemcapabilities-bioregistry] Bioregistry. n.d.
   "System capabilities, operating ranges, and survival ranges ontology."
   Registry entry.
   Available at:
   `https://bioregistry.io/ssn.system <https://bioregistry.io/ssn.system>`_
