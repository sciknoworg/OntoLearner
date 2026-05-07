

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Web and Internet
       * - **Category**
         - interoperability
       * - **Current Version**
         - 3.2.1
       * - **Last Updated**
         - 2020-12-31
       * - **Creator**
         - ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M)
       * - **License**
         - None
       * - **Format**
         - rdf
       * - **Download**
         - `Download Smart Applications REFerence ontology (SAREF) <https://saref.etsi.org/core/v3.2.1/>`_

Smart Applications REFerence ontology (SAREF)
========================================================================================================

SAREF is a comprehensive suite of interrelated ontologies that defines a shared model of consensus for enabling semantic interoperability across IoT solutions and smart applications from diverse providers and industry sectors [#saref-portal]_. It provides a standardized vocabulary for describing smart devices, their capabilities, interactions, services, properties, states, measurements, and relationships in Internet of Things (IoT) and smart environments such as smart homes, smart buildings, smart cities, industry, agriculture, energy, and health [#saref-portal]_ [#saref-core]_. SAREF captures essential IoT concepts including devices, sensors, actuators, services, properties, and the relationships between them, facilitating machine-to-machine communication, automation, and semantic interoperability [#saref-core]_. The SAREF suite is published by ETSI and provides common terminology that allows data and services from different IoT platforms, applications, and manufacturers to be integrated and understood [#saref-portal]_. SAREF supports semantic data spaces by enabling interoperable descriptions of devices, measurements, properties, services, and their relationships across heterogeneous IoT ecosystems [#saref-core]_.

**Example Usage**: Annotate an IoT device deployment with SAREF terms describing the device type, such as ``smart thermostat``, ``light bulb``, or ``motion sensor``; its capabilities, such as temperature measurement or brightness control; the services it offers, such as remote adjustment or scheduling; and its relationships to control systems, spaces, and user preferences [#saref-core]_ [#saref-portal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 804
        * - **Total Edges**
          - 1720
        * - **Root Nodes**
          - 14
        * - **Leaf Nodes**
          - 376
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 129
        * - **Individuals**
          - 10
        * - **Properties**
          - 89

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
          - 0.07
        * - **Depth Variance**
          - 0.06
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 7.50
        * - **Breadth Variance**
          - 42.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 10
        * - **Taxonomic Relations**
          - 88
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 10.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SAREF

    ontology = SAREF()
    ontology.load("path/to/SAREF-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#saref-portal] ETSI. n.d.
   "SAREF Ontology."
   Available at:
   `https://saref.etsi.org/ <https://saref.etsi.org/>`_

.. [#saref-core] ETSI. 2025.
   "SAREF Core Ontology."
   Available at:
   `https://saref.etsi.org/core/v4.1.1/ <https://saref.etsi.org/core/v4.1.1/>`_
