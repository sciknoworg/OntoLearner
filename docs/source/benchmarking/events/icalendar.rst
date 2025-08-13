

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Events
       * - **Category**
         - Calendar and Scheduling
       * - **Current Version**
         - 1.14
       * - **Last Updated**
         - 2004/04/07
       * - **Creator**
         - Dan Connolly, W3C, Libby Miller, ASemantics
       * - **License**
         - Open Publication License
       * - **Format**
         - rdf
       * - **Download**
         - `Download iCalendar Vocabulary (iCalendar) <https://www.w3.org/2002/12/cal/>`_

iCalendar Vocabulary (iCalendar)
========================================================================================================

iCalendar is an Internet standard for exchanging calendar and scheduling data across different applications     and platforms using a standardized text-based format (.ics). It enables interoperability for events, tasks,     and scheduling, supporting features like recurring events, invitations, and time zone adjustments.     While widely used in applications like Google Calendar and Outlook, its complexity and partial implementations     pose challenges, leading to efforts to integrate it with Semantic Web technologies     for enhanced data linking and automation.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 496
        * - **Total Edges**
          - 1271
        * - **Root Nodes**
          - 4
        * - **Leaf Nodes**
          - 93
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 54
        * - **Individuals**
          - 0
        * - **Properties**
          - 49

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
          - 0.60
        * - **Depth Variance**
          - 0.24
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 6
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 5.00
        * - **Breadth Variance**
          - 1.00
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

    from ontolearner.ontology import iCalendar

    ontology = iCalendar()
    ontology.load("path/to/iCalendar-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
