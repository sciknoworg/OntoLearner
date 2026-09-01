

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

iCalendar is an Internet standard and RDF vocabulary for exchanging
calendar and scheduling data across applications using standardized
representations such as iCalendar files and RDF views
[#ical-rdf-note]_ [#ical-rfc]_. It models core scheduling concepts such
as events, to-dos, recurrence rules, attendees, time zones, and alarms,
enabling interoperable representation of meetings, recurring
appointments, and calendar invitations [#ical-rdf-note]_ [#ical-rfc]_.
While the original iCalendar format is a text-based standard widely
implemented in calendar clients, the iCalendar vocabulary expresses
these concepts in RDF to support Semantic Web integration, richer
linking, and machine-processable event data [#ical-rdf-note]_
[#ical-w3c]_. Key characteristics include explicit recurrence modeling,
timezone-aware date and time representation, and support for
invitations and participation roles [#ical-rdf-note]_ [#ical-rfc]_.
By providing a shared semantic framework for calendar and scheduling
data, the vocabulary supports calendar synchronization, meeting
scheduling services, automated reminders, and semantic linking of event
metadata with external datasets [#ical-rdf-note]_ [#ical-w3c]_.

**Example Usage**: Represent a weekly team meeting as an event with a
recurrence rule for weekly repetition, linked attendee agents with
roles such as organizer and participant, and timezone-aware start and
end datetimes. The vocabulary can also be combined with other
ontologies, such as FOAF for people, to enrich event descriptions and
support advanced calendar automation [#ical-rdf-note]_ [#ical-rfc]_.

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

References
----------

.. [#ical-rdf-note] Connolly, D., and Miller, L. 2005.
   "RDF Calendar - An Application of the Resource Description Framework
   to iCalendar Data."
   W3C Note, 29 September 2005.
   Available at:
   `https://www.w3.org/2002/12/cal/report1173.html <https://www.w3.org/2002/12/cal/report1173.html>`_

.. [#ical-w3c] W3C. n.d. "RDF Calendar Workspace."
   Available at:
   `https://www.w3.org/2002/12/cal/ <https://www.w3.org/2002/12/cal/>`_

.. [#ical-rfc] Desruisseaux, B. 2009.
   "Internet Calendaring and Scheduling Core Object Specification
   (iCalendar)."
   RFC 5545.
   Available at:
   `https://www.rfc-editor.org/rfc/rfc5545 <https://www.rfc-editor.org/rfc/rfc5545>`_
