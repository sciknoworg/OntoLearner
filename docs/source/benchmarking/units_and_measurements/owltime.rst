

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

OWL-Time is an OWL-2 DL ontology of temporal concepts, for describing the temporal properties of resources     in the world or described in Web pages. The ontology provides a vocabulary for expressing facts     about topological (ordering) relations among instants and intervals, together with information about durations,     and about temporal position including date-time information. Time positions and durations may be expressed     using either the conventional (Gregorian) calendar and clock, or using another temporal reference system     such as Unix-time, geologic time, or different calendars.

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
