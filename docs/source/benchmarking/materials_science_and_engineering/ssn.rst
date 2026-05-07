.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Sensor Networks
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2017-04-17
       * - **Creator**
         - W3C/OGC Spatial Data on the Web Working Group
       * - **License**
         - http://www.w3.org/Consortium/Legal/2015/copyright-software-and-document
       * - **Format**
         - ttl
       * - **Download**
         - `Download Semantic Sensor Network Ontology (SSN) <https://github.com/w3c/sdw-sosa-ssn/tree/482484fe2edc1ba8aa7f19214a72bdb77123e833>`_

Semantic Sensor Network Ontology (SSN)
========================================================================================================

The Semantic Sensor Network (SSN) ontology is an ontology for describing sensors, observations, procedures, features of interest, samples, observed properties, and actuators [#ssn-w3c]_. SSN includes a lightweight, self-contained core ontology called SOSA - Sensor, Observation, Sample, and Actuator which provides elementary classes and properties for modelling observation, sampling, and actuation activities [#ssn-w3c]_.

SSN and SOSA support a modular architecture with different scopes and degrees of axiomatization, enabling use across applications such as satellite imagery, scientific monitoring, industrial and household infrastructures, social sensing, citizen science, observation-driven ontology engineering, and the Web of Things [#ssn-w3c]_. By providing a standardized vocabulary, SSN supports semantic annotation, interoperability, data integration, querying, and reuse of sensor and observation data across sensor-network and data-management platforms [#ssn-w3c]_.

**Example Usage**:
Annotate a sensor network dataset with SSN/SOSA terms to specify sensors, observations, procedures, features of interest, samples, observed properties, actuators, and results, enabling semantic search and integration with sensor-network management and Web of Things platforms [#ssn-w3c]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 551
        * - **Total Edges**
          - 1643
        * - **Root Nodes**
          - 22
        * - **Leaf Nodes**
          - 106
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 22
        * - **Individuals**
          - 9
        * - **Properties**
          - 38

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
          - 0.15
        * - **Depth Variance**
          - 0.13
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 22
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 13.00
        * - **Breadth Variance**
          - 81.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 93
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SSN

    ontology = SSN()
    ontology.load("path/to/SSN-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#ssn-w3c] W3C and OGC. 2017.
   "Semantic Sensor Network Ontology."
   W3C Recommendation.
   Available at:
   `https://www.w3.org/TR/vocab-ssn/ <https://www.w3.org/TR/vocab-ssn/>`_
