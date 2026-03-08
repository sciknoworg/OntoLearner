.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Units and Measurements
       * - **Category**
         - Temporal Reasoning
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 15 November 2022
       * - **Creator**
         - World Wide Web Consortium
       * - **License**
         - W3C Software Notice and Document License
       * - **Format**
         - ttl
       * - **Download**
         - `Download Time Ontology in OWL (OWL-Time) <https://www.w3.org/TR/owl-time/>`_

Time Ontology in OWL (OWL-Time)
========================================================================================================

The Time Ontology in OWL (OWL-Time) is a comprehensive ontology for representing temporal concepts, relationships, and properties in semantic web and linked data applications. It provides a standardized vocabulary for describing time instants, intervals, durations, temporal positions, and topological relations (e.g., before, after, during) among temporal entities. OWL-Time supports multiple temporal reference systems, including the Gregorian calendar, Unix time, geologic time, and custom calendars, enabling flexible modeling of temporal data. The ontology is widely used for annotating temporal aspects of resources in scientific datasets, event logs, web pages, and knowledge graphs. By providing a common framework, OWL-Time facilitates temporal reasoning, event sequencing, and integration of time-based data across domains. The ontology is maintained by the World Wide Web Consortium (W3C) and is continuously updated to support new temporal modeling requirements.

**Example Usage**:
Annotate an event dataset with OWL-Time terms to specify event start and end times, durations, and temporal relationships (e.g., "event A before event B"), enabling temporal reasoning and timeline visualization in knowledge graphs.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 700
        * - **Total Edges**
          - 1132
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 532
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 23
        * - **Individuals**
          - 17
        * - **Properties**
          - 58

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 0
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.00
        * - **Depth Variance**
          - 0.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 0
        * - **Minimum Breadth**
          - 0
        * - **Average Breadth**
          - 0.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 17
        * - **Taxonomic Relations**
          - 66
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 8.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OWLTime

    ontology = OWLTime()
    ontology.load("path/to/OWLTime-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
