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

The Time Ontology in OWL (OWL-Time) is an OWL ontology for representing temporal concepts, relationships, and properties in Semantic Web and Linked Data applications [#owltime-w3c]_ [#owltime-ogc]_. It provides a standardized vocabulary for describing temporal entities, including instants and intervals, as well as durations, temporal positions, date-time descriptions, and ordering relations between temporal entities [#owltime-w3c]_. OWL-Time supports multiple temporal reference systems, allowing temporal positions and durations to be expressed using the Gregorian calendar and clock, Unix time, geologic time, or other temporal reference systems and calendars [#owltime-w3c]_. The ontology is used to annotate temporal aspects of resources in datasets, event logs, web pages, knowledge graphs, and other Web resources [#owltime-w3c]_ [#owltime-ogc]_. By providing a common semantic framework, OWL-Time facilitates temporal reasoning, event sequencing, temporal ordering, and integration of time-based data across domains [#owltime-w3c]_ [#owltime-ogc]_. OWL-Time is maintained as a W3C/OGC standard for describing temporal properties of resources on the Web [#owltime-w3c]_ [#owltime-ogc]_.

**Example Usage**:
Annotate an event dataset with OWL-Time terms to specify event start and end times, durations, temporal positions, and temporal relationships such as ``before``, ``after``, or ``during``. This enables temporal reasoning, event ordering, timeline visualization, and integration of temporal information in knowledge graphs [#owltime-w3c]_ [#owltime-ogc]_.

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

References
----------

.. [#owltime-w3c] W3C. 2022.
   "Time Ontology in OWL."
   W3C Candidate Recommendation Draft.
   Available at:
   `https://www.w3.org/TR/owl-time/ <https://www.w3.org/TR/owl-time/>`_

.. [#owltime-ogc] Open Geospatial Consortium. n.d.
   "Time Ontology in OWL."
   Available at:
   `https://www.ogc.org/standards/time-ontology-in-owl/ <https://www.ogc.org/standards/time-ontology-in-owl/>`_
