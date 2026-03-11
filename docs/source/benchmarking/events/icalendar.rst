

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

iCalendar is an Internet standard and RDF vocabulary for exchanging calendar and scheduling data across applications using a standardized representation (.ics and RDF views). It models core scheduling concepts such as Events, To-Dos, Recurrence Rules, Attendees, Time Zones, and Alarms, enabling interoperable representation of meetings, recurring appointments, and calendar invitations. While the original iCalendar format (.ics) is a text standard widely implemented in client applications (Google Calendar, Outlook), the iCalendar vocabulary expresses these concepts in RDF to support Semantic Web integration, richer linking, and automated reasoning. Key characteristics include explicit recurrence modelling, timezone-aware datatypes, and support for invitations and participation roles. Common applications include calendar synchronization, meeting scheduling services, automated reminders, and semantic linking of event metadata with external datasets.

**Example usage**: represent a weekly team meeting as an Event with a RRULE for weekly recurrence, linked Attendee agents with roles (organizer, participant), and timezone-aware start/end datetimes. The vocabulary can be combined with other ontologies (e.g., FOAF for people) to enrich event descriptions and support advanced calendar automation.

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
